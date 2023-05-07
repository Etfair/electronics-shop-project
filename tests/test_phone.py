import pytest
from src.phone import Phone
from src.item import Item


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_magic_methods(phone):
    """
    Тест магических методов для phone
    """
    assert str(phone) == 'iPhone 14'
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_add(phone):
    """
    Тест количества товара
    """
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone == 25
    assert phone + phone == 10


def test_setter(phone):
    """
    Тест количества сим
    """
    assert phone.number_of_sim == 2
    phone.number_of_sim = 0
    assert phone.number_of_sim == ValueError