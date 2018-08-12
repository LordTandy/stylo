import numpy as np

from stylo.domain import SquareDomain, UnitSquare
from stylo.drawable.drawable import Drawable


class Ellipse(Drawable):
    """An ellipse.

    Mathematically we can define an ellipse to be the set
    of points :math:`(x, y)` which satisfy:

    .. math::

        \\frac{(x - x_0)^2}{a^2} + \\frac{(y - y_0)^2}{b^2} \\leq r^2

    where:

    - :math:`(x_0, y_0)` is the center of the ellipse
    - :math:`a` is known as the semi major axis, larger values make the
      ellipse more elongated in the :math:`x`-direction
    - :math:`b` is known as the semi minor axis, larger values make the
      ellipse more elongated in the :math:`y`-direction
    - :math:`r` is the "radius" of the ellipse and controls the overall
      size of the ellipse
    """

    def __init__(self, x, y, a, b, r):
        super().__init__()
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.r = r

    def default_domain(self):
        return SquareDomain(-1, 1)

    def shape(self):

        r = self.r * self.r
        a = self.a
        b = self.b
        x0 = self.x
        y0 = self.y

        def ellipse(x, y):
            xc = x - x0
            yc = y - y0

            return (xc * xc) / a + (yc * yc) / b <= r

        return ellipse


class Circle(Ellipse):
    """
    Mathematically a circle can be defined as the set of all
    points :math:`(x, y)` that satisfy

    .. math::

    (x - x_0)^2 + (y - y_0)^2 = r^2

    This function returns another function which when given
    a point :code:`(x, y)` will return :code:`True` if that
    point is in the circle
    """

    def __init__(self, x, y, r):
        super().__init__(x, y, 1, 1, r)


class Rectangle(Drawable):
    """
    It's quite simple to define a rectangle, simply pick a
    point :math:`(x_0,y_0)` that you want to be the center
    and then two numbers which will represent the width and
    height of the rectangle.
    """

    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def default_domain(self):
        return UnitSquare()

    def shape(self):

        left = self.x - (self.width / 2)
        right = self.x + (self.width / 2)
        top = self.y + (self.height / 2)
        bottom = self.y - (self.height / 2)

        def rectangle(x, y):
            xs = np.logical_and(left < x, x < right)
            ys = np.logical_and(bottom < y, y < top)

            return np.logical_and(xs, ys)

        return rectangle


class Square(Rectangle):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
