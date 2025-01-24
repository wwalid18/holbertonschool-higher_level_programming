#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Prints all integers of a list, one integer per line using str.format().
    """
    for number in my_list:
        print("{:d}".format(number))
