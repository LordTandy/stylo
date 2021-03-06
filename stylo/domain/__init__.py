from ._factory import define_domain

RealDomain = define_domain("RealDomain", "x,y,r,t")

from .rectangular import RectangularDomain  # noqa: F401
from .square import SquareDomain, UnitSquare  # noqa: F401
