#! /usr/bin/env python3

"A script for calculating the area of a rectangle."

import sys

def area_of_rectangle(height, width=None):
    """
    Returns the area of a rectangle.
    """
    if width is None:
        width = height
    
    area = height * width
    return area

if __name__ == '__main__':
    if (len(sys.argv) < 2) or (len(sys.argv) > 3):
        message = (
                "{script_name}: Expecting one or two command-line arguments:\n"
                "\tthe height of a square or the height and width of a "
                "rectangle".format(script_name = sys.argv[0]))
        sys.exit(message)

    try:
        height = float(sys.argv[1])
        
        if len(sys.argv) == 3:
            width = float(sys.argv[2])
        else:
            width = None 

        area = area_of_rectangle(height, width)

        actual_width = width if width is not None else height

        message = "The area of a {h} X {w} rectangle is {a}".format(
                h = height,
                w = actual_width,
                a = area)
        print(message)
        
    except ValueError:
        sys.exit("Error: Please provide numeric values (e.g., 7 or 7.5).")
