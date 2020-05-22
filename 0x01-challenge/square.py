#!/usr/bin/python3
"""Square Module"""


class Square():
    """Defines a square"""
    width = 0
    height = 0

    def __init__(self, size=0):
        "Initializes square class attributes"
        square.width = size
        square.height = size

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """Perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String representation of a Square"""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = square(size=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
