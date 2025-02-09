#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class animal"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Abstract base class dog"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Abstract base class cat"""
    def sound(self):
        return "Meow"
