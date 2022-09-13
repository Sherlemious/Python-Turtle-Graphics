from turtle import *


def draw_polygon(n: int, l: float):
    """
    Draws a n-sided regular polygon

    :param n: number of sides
    :param l: side length
    """

    for _ in range(n):
        fd(l)
        rt(360 / n)


# Draw a Square
draw_polygon(4, 100)
