#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent an empty rectangle.

    Attributes:
        number_of_instances = The number of Rectangle Instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.
        Args:
            width(int): The width of the rectangle
            height(int): The height of the rectangle
        """
        type(self).number_of_instances += 1
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get/Set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/Set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):

        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for x in range(self.__height):
            [rectangle.append('#') for y in range(self.__width)]
            if x != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)

    def __del__(self):
        """Print a message when an instance of Rectangle is being deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
