hpmeter
=======

A script for generating HP meters (for games). The gradient function is probably useful for other things as well.

(From the pydoc)
FUNCTIONS
---------
###pct2color(pct, map, verbose=0)
    
Generate a color based on a gradient map and a percentage.
        
The gradient map is a dictionary of arrays of the structure:

    map[index] = [ r, g, b, ],
    map[index] = [ r, g, b, ],

where "index" is a number between 0 and 100. The map can contain as many values as necessary to define the required gradient.

#### Example 1:
    map[0]   = [ 0,   0, 0, ], #0% black
    map[100] = [ 255, 0, 0, ], #100% red (black)
    pct2color( 75, map ) # returns [ 191, 0, 0, ] # 75% red
#### Example 2:
    map[0] = [255, 0, 0, ] #Red
    map[35] = [255, 153, 0, ] #Orange
    map[60] = [255, 255, 0, ] #Yellow
    map[100] = [ 0, 255, 0, ] #Green
    pct2color( 50, map) # returns [255, 153, 0] #ffd600
    
###tuple2hex(tup)
Convert a tuple of RGB values into a hex color code.
#### Example:
    tuple2hex( [ 255, 0, 255, ], ) # returns "#FF00FF"
