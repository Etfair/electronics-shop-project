"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture

def item1():
    return Item("Смартфон", 10000, 20)



def test_calculate_total_price(item1):
    """ Подсчитывает общую стоимость смартфонов в магазине"""
    assert item1.calculate_total_price() == 200000.0


def test_apply_discount(item1):
    """"""
    Item.pay_rate = 0.8
    assert item1.apply_discount() == 8000.0