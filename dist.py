#!/usr/bin/python
#
# Author: Jun Kang Chin 3/11/2014
#
import sys
import traceback
import getopt
from math import cos, radians, sqrt
R = 6371 #km
def equirectangular_approx(pt_1, pt_2):
    """Use of equirectangular approx

    Advantages: Uses way less trig operations compared to haversine and
    spherical law of consines, which allows for better performance with
    acceptable accuracy for short driving distances.
    Disadvantage: Less accurate for long distances and arounds the poles

    Based on:
    http://www.movable-type.co.uk/scripts/latlong.html
    """
    lat_1, long_1 = pt_1
    lat_2, long_2 = pt_2
    x = radians(long_2 - long_1) * cos(radians(lat_1 + lat_2) / 2)
    y = radians(lat_2 - lat_1)
    dist = R * sqrt(x * x + y * y) 
    return dist

def find_detour(a, b, c, d, dist_func=equirectangular_approx):
    """Returns the shorter of the detour distances the drivers
    would need to take to pick-up and drop-off the other driver.
    
    :param a: Starting coordinate of driver A
    :param b: Destination coordinate of driver A
    :param c: Starting coordinate of driver B
    :param d: Destination coordinate of driver B
    :dist_func: Distance function. Default is equirectangular_approx as it's
                performant and accurate for short driving distances
    :returns Distance in km
    """
    a_detour_dist = dist_func(a, c) + dist_func(c, b)
    b_detour_dist = dist_func(c, a) + dist_func(a, d)
    return min(a_detour_dist, b_detour_dist)

def usage():
    """Prints usage string
    """
    usage_str = \
"""Calculates the lesser of the detours distances between two
different rides and returns the results in km.

dist.py pt_a pt_b pt_c pt_d

Arguments:
    Coordinates expressed in latitude and longitude comma-separated signed
    decimal degree pairs: <lat>,<log>
    
    pt_a -- Starting coordinates of ride A
    pt_b -- Destination coordinates of ride A
    pt_c -- Starting coordinates of ride B
    pt_d -- Destination coordinates of ride B


Example:
./dist.py 0.0,0.0 1.0,1.0 -1.0,-1.0 -2.0,-2.0
"""
    print usage_str

def parse_args():
    argv = sys.argv
    if len(argv) > 1:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
            # Got the option to print usage, so do so.
            if opts:
                usage()
            else:
                # Validate that exactly 4 args are passed in
                if len(args) != 4:
                    print ("Incorrect number of arguments: %s. "
                            "Was expecting 4" % args)
                else:
                    # Further parse the arguments into lat/long float tuples
                    coord_list = []
                    for coord in args:
                        lat, long = coord.split(',')
                        coord_list.append((float(lat), float(long)))
                    return coord_list
        except Exception, ex:
            # Print usage for any exceptions
            usage()
            print ex
            print traceback.format_exc()
    else:
        usage()

def main():
    coord_list = parse_args()
    if not coord_list:
        sys.exit(1)
    else:
        try:
            print find_detour(*coord_list)
        except Exception, ex:
            print "Failed to find detour: %s" % ex
            print "%s" % traceback.format_exc()

if __name__ == "__main__":
    main()
