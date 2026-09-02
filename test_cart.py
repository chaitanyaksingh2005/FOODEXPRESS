from cart import cart_total, apply_discount


def test_cart_total():
    items = [
        {"price": 100, "qty": 2},
        {"price": 50, "qty": 1},
    ]

    assert cart_total(items) == 250


def test_apply_discount():
    assert apply_discount(1000, 10) == 900


def test_invalid_discount():
    try:
        apply_discount(1000, 101)
        assert False
    except ValueError:
        assert True
