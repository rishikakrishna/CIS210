"""
Count the number of occurrences of each major code in a file.
Authors: Rishika Krishna
Credits: Consulted Vinitha Gadiraju about accessing indices properly in different contexts.

Input is a file in which major codes (e.g., "CIS", "UNDL", "GEOG")
appear one to a line. Output is a sequence of lines containing major code
and count, one per major.
"""

import argparse

def count_codes(majors_file):
    """
    Reads a file containing a list of arbitrarily ordered major codes
    and prints the output in alphabetical order by major code and lists frequency
    
    args:
        majors_file: external .txt file containing class' majors
    returns:
        a sequence of major codes, one per line, and lists frequency
    """
    majors = [ ]

    for line in majors_file:
        majors.append(line.strip())

    majors = sorted(majors)

    count = 1
    for major in range(1, len(majors)):
        if majors[major-1] == majors[major]:
            count += 1
        else:
            print(majors[major-1], count)
            count = 1
    print(majors[len(majors)-1], count)

def main( ):
    """
    Interaction if run from the command line.
    Usage:  python3 counts.py  majors_code_file.txt
    """
    parser = argparse.ArgumentParser(description="Count major codes")
    parser.add_argument('majors', type=argparse.FileType('r'),
                        help="A text file containing major codes, one major code per line.")
    args = parser.parse_args()  # gets arguments from command line
    majors_file = args.majors
    count_codes(majors_file)
    
    
if __name__ == "__main__":
    main( )