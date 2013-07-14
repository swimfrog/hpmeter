#!/usr/bin/python

"""
"""

import Image, ImageDraw
import argparse

def pct2color( pct, map, verbose=0 ):
    """
      Generate a color based on a gradient map and a percentage.

      The gradient map is a dictionary of arrays of the structure:
        map[index] = [ r, g, b, ],
        map[index] = [ r, g, b, ],
      where "index" is a number between 0 and 100. The map can contain as many values as necessary
      to define the required gradient.

      Example 1:
        map[0]   = [ 0,   0, 0, ], #0% black
        map[100] = [ 255, 0, 0, ], #100% red (black)
        pct2color( 75, map ) # returns [ 191, 0, 0, ] # 75% red

      Example 2:
        map[0] = [255, 0, 0, ] #Red
        map[35] = [255, 153, 0, ] #Orange
        map[60] = [255, 255, 0, ] #Yellow
        map[100] = [ 0, 255, 0, ] #Green
        pct2color( 50, map) # returns [255, 153, 0] #ffd600 -- an orangish-yellow
    """

    fpct=float(pct)

    # Find the key that's greater than the pct
    lo={}
    hi={}
    count=0
    ipct=fpct # "internal percent"=percentage of gradient between the two keys
    #import pdb; pdb.set_trace()

    # Populate hi[],lo[],ipct variables from gradient map struct.
    dkeys=map.keys()
    dkeys.sort()
    for k in dkeys:
        if pct == 0:
            lo=map[0]
            hi=map[0]
            ipct=0
            break
        elif k >= pct:
            lokey=dkeys[count-1]
            lo=map[lokey]
            hikey=dkeys[count]
            hi=map[hikey]
#            if pct in (24, 25, 26, 27,):
#                import pdb; pdb.set_trace()
            # Take the input percentage and figure out that percentage between the two closest keys
            ipct=(fpct-lokey)*100/(hikey-lokey)
            if ipct < 0:
                ipct=ipct*-1
            if verbose:
                print "pct=%s%% of gradient is ipct = %d%% between %d and %d" % (pct, ipct, lokey, hikey)
            break
        count += 1
   
    # Iterate over hi[], lo[] and populate an output tuple of color bytes.
    output=list()
    for x in (0, 1, 2,):
	#print "%s, %s" % (hi[x], lo[x])
        dist=hi[x]-lo[x]
        itp=0
        # Interpolate the color byte by multipying the absolute distance of each point
        # by the percent input value, then adding it to the lowest point.
        if dist < 0:
            # Invert the percentage:
            tipct=100-ipct
            itp=int((abs(dist)*(tipct/100))-min(lo[x], hi[x]))
        else:
            itp=int((abs(dist)*( ipct/100))+min(lo[x], hi[x]))
        #print "index %s at pct %d%% interpolated from %d, %d (dist=%d) as %d" % (x, ipct, hi[x], lo[x], dist, itp)
        output.append(itp)

    buffer=tuple2hex(output)
    if verbose:
        print "pct %d hi %s, lo %s interpolated as %s" % (pct, hi, lo, buffer)
        
    return buffer

def tuple2hex( tup ):
    """
      Convert a tuple of RGB values into a hex color code.

      Example:
        tuple2hex( [ 255, 0, 255, ], ) # returns "#FF00FF"
    """

    buffer="#"
    for x in range(len(tup)):
        # Strip off the hex offset and zero-pad.
        buffer += hex(tup[x]).lstrip("0x").zfill(2)
    return buffer


if __name__ == '__main__':
    """
      Generate an HP meter. You supply the number of states, and the script generates that number of
      PNG-format images. The meter is drawn as a sort of colored progress bar, where the color
      corresponds to the percentage.
    """

    argp = argparse.ArgumentParser()
    argp.add_argument( 'range', type=int, help="Range of hpmeters to generate")
    argp.add_argument( '--width', type=int, default=100, help="Width in pixels of output HP meter images. Default is 100")
    argp.add_argument( '--height', type=int, default=15, help="Height in pixels of output HP meter images. Default is 15")
    argp.add_argument( '--output', default="hpmeter", help="Output filename prefix. Default is \"hpmeter\"")
    argp.add_argument( '--verbose', action='count', help="Be verbose.")
    args = argp.parse_args()

    map = {}
    map[0] = [255, 0, 0, ] #Red
    map[35] = [255, 153, 0, ] #Orange
    map[60] = [255, 255, 0, ] #Yellow
    map[100] = [ 0, 255, 0, ] #Green
    
    #BUG: Only works when width=100.
    
    for x in range(args.range):
        colorhex = pct2color(x, map, args.verbose)
        im = Image.new('RGB', (args.width, args.height))
        im.putalpha(100)
        draw = ImageDraw.Draw(im)
        draw.rectangle(((0,0),(x,args.height)), fill=colorhex, outline=colorhex )
        im.save(("%s%s.png") % ( args.output, x, ), "PNG")

