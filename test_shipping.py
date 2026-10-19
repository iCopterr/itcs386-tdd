
import pytest
from shipping import shipping_fee


# Rule 1: Weight must be greater than 0
# Bug: Rule 1 is violated because zero weight is accepted.
def test_zero_weight_is_rejected():
    with pytest.raises(ValueError):
        shipping_fee(0)


def test_negative_weight_is_rejected():
    with pytest.raises(ValueError):
        shipping_fee(-1)



@pytest.mark.parametrize("weight, expected", [
    (0.5, 40),  # Rule 2
    (1.0, 40),  # Bug: Rule 2, exactly 1 kg must cost 40
    (1.5, 60),  # Rule 3
    (3.0, 60),  # Rule 3
    (5.0, 60),  # Rule 3
    (5.2, 70),  # Bug: Rule 4, round extra weight up
    (6.0, 70),  # Rule 4
    (6.5, 80),  # Bug: Rule 4, round extra weight up
])
def test_shipping_fee(weight, expected):
    assert shipping_fee(weight) == expected

