#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

// ----------------------
// SHADERTOY UNIFORMS  -
// ----------------------

uniform vec3      iResolution;           // viewport resolution (in pixels)
uniform float     iTime;                 // shader playback time (in seconds)
uniform vec4      iMouse;                // mouse pixel coords. xy: current (if MLB down), zw: click
uniform sampler2D iChannel0;

void mainImage( out vec4 fragColor, in vec2 fragCoord );

void main() {
    mainImage(gl_FragColor,gl_FragCoord.xy);
}

// ------------------------------
//  SHADERTOY CODE BEGINS HERE  -
// ------------------------------


// Dave Hoskins
// https://www.shadertoy.com/view/4djSRW
float hash13(vec3 p3)
{
	p3  = fract(p3 * .1031);
    p3 += dot(p3, p3.zyx + 31.32);
    return fract((p3.x + p3.y) * p3.z);
}

// Inigo Quilez
// https://www.iquilezles.org/www/articles/distfunctions/distfunctions.htm
float smin( float d1, float d2, float k ) {
    float h = clamp( 0.5 + 0.5*(d2-d1)/k, 0.0, 1.0 );
    return mix( d2, d1, h ) - k*h*(1.0-h); }
float smoothing(float d1, float d2, float k) { return clamp( 0.5 + 0.5*(d2-d1)/k, 0.0, 1.0 ); }

// rotation matrix
mat2 rot(float a) { return mat2(cos(a),-sin(a),sin(a),cos(a)); }

#define repeat(p,r) (mod(p,r)-r/2.)

// taste of noise 7 by leon denise 2021/10/14
// result of experimentation with organic patterns
// using code from Inigo Quilez, David Hoskins and NuSan
// thanks to Fabrice Neyret for code reviews
// licensed under hippie love conspiracy

// global variable
float material;
float rng;

// sdf
float map (vec3 p)
{
    // time stretched with noise
    float t = iTime*1. + rng*0.9;

    // domain repetition
    float grid = 5.;
    vec3 cell = floor(p/grid);
    p = repeat(p,grid);

    // distance from origin
    float dp = length(p);

    // rotation parameter
    vec3 angle = vec3(.1,-.5,.1) + dp*.5 + p*.1 + cell;

    // shrink sphere size
    float size = sin(rng*3.14);

    // stretch sphere
    float wave = sin(-dp*1.+t+hash13(cell)*6.28)*.5;

    // kaleidoscopic iterated function
    const int count = 4;
    float a = 1.0;
    float scene = 1000.;
    float shape = 1000.;
    for (int index = 0; index < count; ++index)
    {
        // fold and translate
        p.xz = abs(p.xz)-(.5+wave)*a;

        // rotate
        p.xz *= rot(angle.y/a);
        p.yz *= rot(angle.x/a);
        p.yx *= rot(angle.z/a);

        // sphere
        shape = length(p)-0.2*a*size;

        // material blending
        material = mix(material, float(index), smoothing(shape, scene, 0.3*a));

        // add with a blend
        scene = smin(scene, shape, 1.*a);

        // falloff transformations
        a /= 1.9;
    }

    return scene;
}

// return color from pixel coordinate
void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    // reset color
    fragColor = vec4(0,0,0,1);
    material = 0.0;

    // camera coordinates
    vec2 uv = (fragCoord.xy - iResolution.xy * 0.5) / iResolution.y;
    vec3 eye = vec3(1,1,1.);
    vec3 at = vec3(0,0,0);
    vec3 z = normalize(at-eye);
    vec3 x = normalize(cross(z, vec3(0,1,0)));
    vec3 y = cross(x, z);
    vec3 ray = normalize(vec3(z + uv.x * x + uv.y * y));
    vec3 pos = eye;

    // camera control
    vec2 M = 6.28*(iMouse.xy-.5);
    ray.xz *= rot(M.x), pos.xz *= rot(M.x);
    ray.xy *= rot(M.y), pos.xy *= rot(M.y);

    // white noise
    vec3 seed = vec3(fragCoord.xy, iTime);
    rng = hash13(seed);

    // raymarch
    const float steps = 30.0;
    float index;
    for (index = steps; index > 0.0; --index)
    {
        // volume estimation
        float dist = map(pos);
        if (dist < 0.01)
        {
            break;
        }

        // dithering
        dist *= 0.9 + .1 * rng;

        // raymarch
        pos += ray * dist;
    }

    // ambient occlusion from steps count
    float shade = index/steps;

    // compute normal by NuSan (https://www.shadertoy.com/view/3sBGzV)
    vec2 off=vec2(.001,0);
    vec3 normal = normalize(map(pos)-vec3(map(pos-off.xyy), map(pos-off.yxy), map(pos-off.yyx)));

    // Inigo Quilez color palette (https://iquilezles.org/www/articles/palettes/palettes.htm)
    vec3 tint = .5+.5*cos(vec3(3,2,1)+material*.5+length(pos)*.5);

    // lighting
    float ld = dot(reflect(ray, normal), vec3(0,1,0))*0.5+0.5;
    vec3 light = vec3(1.000,0.502,0.502) * sqrt(ld);
    ld = dot(reflect(ray, normal), vec3(0,0,-1))*0.5+0.5;
    light += vec3(0.400,0.714,0.145) * sqrt(ld)*.5;

    // pixel color
    fragColor.rgb = (tint + light) * shade;

    // temporal buffer
    fragColor = max(fragColor, texture(iChannel0, fragCoord/iResolution.xy) - 0.01);
}

// ----------------------------
//  SHADERTOY CODE ENDS HERE  -
// ----------------------------
