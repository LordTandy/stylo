from stylo.domain import SquareDomain
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
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.r = r

    @property
    def domain(self):
        return SquareDomain(-1, 1)

    @property
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

def circle(x0, y0, r, *args, **kwargs):
    """
    Mathematically a circle can be defined as the set of all
    points :math:`(x, y)` that satisfy

    .. math::

        (x - x_0)^2 + (y - y_0)^2 = r^2

    This function returns another function which when given
    a point :code:`(x, y)` will return :code:`True` if that
    point is in the circle

    Parameters
    ----------

    x0 : float
        This is the x coordinate of the circle's center
    y0 : float
        This is the y coordinate of the circle's center
    r : float
        This represents the radius of the ellipse
    pt : float, optional
        Represents the thickness of the lines of the circle.
        Default: 0.2
    fill : bool, optional
        Fill the circle rather than outline it
        Default: False
        **Note:** If fill is true, this function will ignore the value
        of pt

    Returns
    -------

    function:
        A function in 2 arguments :code:`(x, y)` that returns
        :code:`True` if that point is in the circle defined by the
        above parameters
    """

    return ellipse(x0, y0, 1, 1, r, *args, **kwargs)


def between(lower, value, upper):
    """
    A simple function which provides a shorthand
    for checking if a given value is between some lower
    and upper bound

    Parameters
    ----------
    lower : float
        The lower bound to check
    value : float
        The value you want checked
    upper: float
        The upper bound to check

    Returns
    -------
    bool
        :code:`True` if :code:`lower <= value` and
        :code:`value <= upper`. :code:`False` otherwise
    """
    return lower <= value <= upper


def rectangle(x0, y0, width, height, pt=0.2, fill=False):
    """
    It's quite simple to define a rectangle, simply pick a
    point :math:`(x_0,y_0)` that you want to be the center
    and then two numbers which will represent the width and
    height of the rectangle.

    Parameters
    ----------

    x0 : float
        Represents the x-coordinate of the rectangle's center
    y0 : float
        Represents the y-coordinate of the rectangle's center
    width : float
        Represents the width of the rectangle
    height : float
        Represents the height of the rectangle
    pt : float, optional
        Represents the thickness of the lines of the rectangle.
        Default: 0.2
    fill : bool, optional
        Fill the rectangle rather than outline it
        Default: False
        **Note:** If fill is true, this function will ignore the value
        of pt

    Returns
    -------

    function
        A function in 2 arguments :code:`(x, y)` that returns :code:`True`
        if the point is in the rectangle defined by the above parameters
    """
    left = x0 - (width / 2)
    right = x0 + (width / 2)
    top = y0 + (height / 2)
    bottom = y0 - (height / 2)

    def rectangle(x, y):

        if left <= x <= right and bottom <= y <= top:
            return True

        return False

    if fill:
        return rectangle

    def small(x, y):

        if left + pt <= x <= right - pt and bottom + pt <= y <= top - pt:
            return True

        return False

    def rectangle_pt(x, y):

        if rectangle(x, y) and not small(x, y):
            return True

        return False

    return rectangle_pt


def square(x0, y0, size, *args, **kwargs):
    """
    It's quite simple to define a square, simply pick a
    point :math:`(x_0,y_0)` that you want to be the center
    and then a number which will represent the size of the
    square.

    Parameters
    ----------

    x0 : float
        Represents the x-coordinate of the square's center
    y0 : float
        Represents the y-coordinate of the square's center
    size : float
        Represents the size of the square
    pt : float, optional
        Represents the thickness of the lines of the square.
        Default: 0.2
    fill : bool, optional
        Fill the square rather than outline it
        Default: False
        **Note:** If fill is true, this function will ignore the value
        of pt

    Returns
    -------

    function
        A function in 2 arguments :code:`(x, y)` that returns :code:`True`
        if the point is in the square defined by the parameters above
    """
    return rectangle(x0, y0, size, size, *args, **kwargs)
