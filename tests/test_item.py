"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture

def item():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item):
    """ Подсчитывает общую стоимость смартфонов в магазине"""
    assert item.calculate_total_price() == 200000.0


def test_apply_discount(item):
    """Скидка"""
    Item.pay_rate = 0.8
    assert item.apply_discount() == 8000.0


def test_string_to_number():
    """Количество строк"""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_name():
    """Проверяет количество букв на названии товара"""
    Item.name = 'Смартфон'
    assert len(Item.name) < 10


def test_list_item_more(item):
    item.instantiate_from_csv()
    assert len(item.all) == 5
    assert item.all[0].name == 'Смартфон'


def test_string_to_number(item):
    assert isinstance(item.string_to_number(item.quantity), int)

