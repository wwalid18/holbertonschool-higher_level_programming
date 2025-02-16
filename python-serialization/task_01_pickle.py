#!/usr/bin/env python3
import pickle
"""class to create a custom object"""


class CustomObject:
    """Class to create a custom object"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object and save it to a file"""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Serialization error: {e}")

    @classmethod
    def deserialize(cls, filename):
        """Deserialize the object from a file"""
        with open(filename, "rb") as file:
            return pickle.load(file)

