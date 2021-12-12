import pytest

import stonks.margin as pkg


def test_margin_ok():
    pkg.Margin(2)
    pkg.Margin(4)


def test_margin_asserts_on_bad_leverage():
    with pytest.raises(AssertionError):
        pkg.Margin(0)


def test_margin_asserts_on_bad_m_value():
    with pytest.raises(AssertionError):
        pkg.Margin(2, 2)
