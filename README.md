# pyp5-examples
Experiments with py5, I'm not sure how much further I'm going here. Idea is excellent, and I may need to to explore jupyter notebooks as a new programming paradigm.
However things could be so much better with a radical re-write of processing.

Particular irritations:-

1. Processing `map` is not polyglot friendly (should be `remap` or similar).
2. PApplet is behemoth (py5 and ruby-processing have at least moved noise implementation out).
3. PVector is a mess, overloading Vec2D and Vec3D functionality (I'm happy with my java extensions here).
4. Processing4 is even more patched up than earlier versions, dead code and MacOS fixes abound.
5. Inner classes are mixed blessing (fortunately there's a meta-programming workaround for ruby-processing).
