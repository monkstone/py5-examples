 /* 
 * Copyright (c) 2011-20 Martin Prout
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
 *
*
 * @author sid
 */
public enum Constrain {

    /**
     * 
     */
    XAXIS(0),
    /**
     * 
     */
    YAXIS(1),
    /**
     * 
     */
    ZAXIS(2),
    /**
     * 
     */
    FREE(-1);
    private final int index;

    Constrain(int idx) {
        this.index = idx;
    }

    /**
     * 
     * @return int
     */
    public int index() {
        return index;
    }
}

