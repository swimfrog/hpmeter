hpmeter
=======

A script for generating HP meters (for games). I originally made this script to help my nephew with a game he was making while taking a class at DigiPen. The pct2color function might come in handy for other things down the line.

USAGE
-----

    usage: hpmeter.py [-h] [--width WIDTH] [--height HEIGHT] [--output OUTPUT] [--verbose] range

    positional arguments:
      range            Range of hpmeters to generate

    optional arguments:
      -h, --help       show this help message and exit
      --width WIDTH    Width in pixels of output HP meter images. Default is 100
      --height HEIGHT  Height in pixels of output HP meter images. Default is 15
      --output OUTPUT  Output filename prefix. Default is "hpmeter"
      --verbose        Be verbose.

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
    pct2color( 50, map) # returns [255, 153, 0] #ffd600 -- an orangish-yellow
    
###tuple2hex(tup)
Convert a tuple of RGB values into a hex color code.
#### Example:
    tuple2hex( [ 255, 0, 255, ], ) # returns "#FF00FF"
