import pytest

from restaurant import Restaurant


def test_orders_in_line_default_equal_to_zero():
    restaurant = Restaurant("Pizzaria d'Italia")
    assert restaurant.orders_in_line == 0


def test_orders_in_line_default_value_for_orders_in_line_larger_than_zero():
    restaurat = Restaurant("Pizzaria d'Italia",1)
    assert restaurat.orders_in_line == 1


def test_orders_in_line_initial_value_less_than_zero():
    with pytest.raises(ValueError):
        Restaurant("Pizzaria d'Italia",-1)


def test_add_an_order_in_line():
    restaurant = Restaurant("Pizzaria d'Italia")
    restaurant.add_order_in_line()
    assert restaurant.orders_in_line == 1


def test_remove_order_in_line():
    restaurant = Restaurant("Pizzaria d'Italia", 5)
    restaurant.remove_order_in_line()
    assert restaurant.orders_in_line == 4


def test_remove_order_in_empty_list():
    restaurant = Restaurant("Pizzaria d'Italia")
    restaurant.remove_order_in_line()
    assert restaurant.orders_in_line == 0