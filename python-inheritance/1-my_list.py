#!/usr/bin/python3
"""
>>> MyList = __import__('1-my_list').MyList
"""


class MyList(list):
    """A subclass of list that includes a method to print a sorted version."""
    
    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
