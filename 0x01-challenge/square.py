#!/usr/bin/python3
"""Defines a square"""


class square():
    """Defines a square"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        "Initializes square class attributes"
        if (kwargs):
            values = kwargs.values()
            if (len(set(values)) == 1):
                for key, value in kwargs.items():
                    setattr(self, key, value)
            else:
                raise ValueError('width and height must be equal')

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """Perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String representation of a Square"""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
