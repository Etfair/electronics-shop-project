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
    """Скидка"""
    Item.pay_rate = 0.8
    assert item1.apply_discount() == 8000.0


def test_string_to_number():
    """Количество строк"""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_instantiate_from_csv():
    """Количество товара"""
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_name():
    """Проверяет количество букв на названии товара"""
    Item.name = 'Смартфон'
    assert len(Item.name) < 10

def test_long_name():
    """Проверяет длинные названия товаров"""
    Item.name = 'СуперСмартфон'
    assert len(Item.name) > 10
    assert len(Item.name) == 13


def test_list_item_more():
    Item.instantiate_from_csv()
    item2 = Item.all[1]
    assert item2.name == 'РќРѕСѓС‚Р±СѓРє'
