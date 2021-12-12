"""
Just a little something-something to remember the math around margin calculations
"""

from dataclasses import dataclass

_DEFAULTS = [1.0, 1.25, 1.5, 2.0]


@dataclass
class Margin:
    """
    Margin values that a broker might have
    """

    leverage: int

    # Below this you aren't given any more credit
    m0: float = None
    # This is where you get the margin warning (?)
    m1: float = None
    # This is where margin call happens
    m2: float = None
    # At this point your assets are liquidated. Good bye money ;)
    m3: float = None

    def __post_init__(self):

        assert 0 < self.leverage, f"Leverage ('{self.leverage}') needs to be > 0"

        # Default values here are from the book :)
        if self.m0 is None:
            self.m0 = 1 / (_DEFAULTS[0] * self.leverage)
        if self.m1 is None:
            self.m1 = 1 / (_DEFAULTS[1] * self.leverage)
        if self.m2 is None:
            self.m2 = 1 / (_DEFAULTS[2] * self.leverage)
        if self.m3 is None:
            self.m3 = 1 / (_DEFAULTS[3] * self.leverage)

        assert (
            1 > self.m0 > self.m1 > self.m2 > self.m3 > 0
        ), f"Margin points are supposed to be descending! Inttead got: [{self.m0}, {self.m1}, {self.m2}, {self.m3}]"
