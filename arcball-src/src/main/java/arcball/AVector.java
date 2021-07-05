
/* 
 * Copyright (c) 2012-21 Martin Prout
 * 
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see @see <a href="http://www.gnu.org/licenses">http://www.gnu.org/licenses</a>.
 */

package arcball;

/**
 * A lighter weight vector class
 */
 
public final class AVector {

    /**
     * publicly accessible float
     */
    public float x;
    /**
     * publicly accessible float
     */
    public float y;
    /**
     * publicly accessible float
     */
    public float z;

    /**
     * Default Constructor
     */
    public AVector() {
        this.x = 0f;
        this.y = 0f;
        this.z = 0f;
    }

    /**
     * Parameterized constructor
     *
     * @param x float     
     * @param y float
     * @param z float
     */
    public AVector(float x, float y, float z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    /**
     * Copy constructor
     * @param v1 AVector
     */
    public AVector(AVector v1) {
        this.x = v1.x;
        this.y = v1.y;
        this.z = v1.z;
    }

    /**
     * Normalize this vector (and sensibly return it) 
     * @return this AVector normalized
     */
    public AVector normalize() {
        double orig_dist = Math.sqrt(x * x + y * y + z * z);
        this.x /= orig_dist;
        this.y /= orig_dist;
        this.z /= orig_dist;
        return this;
    }

    static float dot(AVector v1, AVector v2) {
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z;
    }

    static AVector mult(AVector v, float scalar) {
        return new AVector(v.x * scalar, v.y * scalar, v.z * scalar);
    }

    static AVector sub(AVector v1, AVector v2) {
        return new AVector(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z);
    }

    /**
     *
     * @param v AVector
     * @return a new AVector cross product
     */
    public AVector cross(AVector v) {
        return new AVector(y * v.z - v.y * z, z * v.x - v.z * x, x * v.y - v.x * y);
    }
}


