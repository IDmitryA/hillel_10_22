from abc import ABC, abstractmethod
from random import choice


class Shape(ABC):
    @classmethod
    @abstractmethod
    def draw(cls):
        pass


class Rectangle(Shape):
    """This class shows schematic representation of rectangle"""

    @classmethod
    def draw(cls) -> None:
        print("----\n|  |\n----")


class Circle(Shape):
    """This class shows schematic representation of circle"""

    @classmethod
    def draw(cls) -> None:
        print(" --\n-  -\n --")


def get_shape() -> Shape:
    """
    This function returns any instance of a Shape class
    In our example it is Rectangle or Circle
    """
    options: list[Shape] = [Rectangle(), Circle()]
    return choice(options)


def main():
    """
    In Rectangle is used I'd like to see:

    ----
    |  |
    ----

    If Circle is used:
      --
     -  -
      --
    """
    shape: Shape = get_shape()
    shape.draw()


if __name__ == "__main__":
    main()
