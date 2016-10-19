"""
draw_barcode.py: Draw barcode representing a ZIP code using Turtle graphics
Authors: Rishika Krishna

CIS 210 assignment 3, part 2, Fall 2016.
"""
import argparse # Used in main program to obtain 5-digit ZIP code from command
                # line
import time     # Used in main program to pause program before exit
import turtle   # Used in your function to print the bar code

## Constants used by this program
SLEEP_TIME = 30 # number of seconds to sleep after drawing the barcode
ENCODINGS = [[1, 1, 0, 0, 0],   # encoding for '0'
             [0, 0, 0, 1, 1],   # encoding for '1'
             [0, 0, 1, 0, 1],   # encoding for '2'
             [0, 0, 1, 1, 0],   # encoding for '3'
             [0, 1, 0, 0, 1],   # encoding for '4'
             [0, 1, 0, 1, 0],   # encoding for '5'
             [0, 1, 1, 0, 0],   # encoding for '6'
             [1, 0, 0, 0, 1],   # encoding for '7'
             [1, 0, 0, 1, 0],   # encoding for '8'
             [1, 0, 1, 0, 0]    # encoding for '9'
            ]
SINGLE_LENGTH = 25  # length of a short bar, long bar is twice as long

def compute_check_digit(digits):
    """
    Compute the check digit for use in ZIP barcodes
    args:
        digits: list of 5 integers that make up zip code
    returns:
        check digit as an integer
    """
    sum = 0
    for i in range(len(digits)):            # these digits must already 
        sum = sum + digits[i]               # be in list form before 
    check_digit = 10 - (sum % 10)           # this function is called upon
    if (check_digit == 10):
        check_digit = 0
    return check_digit

def draw_bar(my_turtle, digit):
    """
    Draw a singular barcode line
    args:
        my_turtle:  Turtle object to draw with
        digit: a single digit, often called upon 
               by referenicing an item in ENCODINGS
    returns:
        None
        (turtle graphic of a line length of height
        SINGLE_LENGTH or 2 * SINGLE_LENGTH)
    """
    my_turtle.left(90)
    if digit == 0:
        length = SINGLE_LENGTH
    else:
        length = 2 * SINGLE_LENGTH
    my_turtle.forward(length)
    my_turtle.up()
    my_turtle.backward(length)
    my_turtle.right(90)
    my_turtle.forward(10)
    my_turtle.down()

def draw_zip(my_turtle, zip):
    """
    Converts an integer to a zip code using turtle.
    Includes a check digit and 
    the final barcode starts and ends with frame bars. 
    args:
        my_turtle:  Turtle object to draw with
        zip: integer between 1 and 99999
    returns:
        None
        (a representative barcode is made using turtle graphics)
    """
    draw_bar(my_turtle, 1)              # barcode starts with 1 (Start)  
    
    for i in str(zip):                  # zip to barcode
        digit = int(i)
        for digit in ENCODINGS[digit]:
            draw_bar(my_turtle, digit)  
    
    zip_list = []
    zip_str = str(zip)
    for i in zip_str:                   # loop to create a LIST of integers
        digit = int(i)                  # that make up the zip code
        zip_list.append(digit)
    check = compute_check_digit(zip_list)
    for digit in ENCODINGS[check]:
        draw_bar(my_turtle, digit)      # the check digit
    
    draw_bar(my_turtle, 1)              # barcode ends with 1 (Stop)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ZIP", type=int)
    args = parser.parse_args()
    zip = args.ZIP
    if zip <= 0 or zip > 99999:
        print("zip must be > 0 and < 100000; you provided", zip)
    else:
        my_turtle = turtle.Turtle()
        draw_zip(my_turtle, zip)
        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    main()