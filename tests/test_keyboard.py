import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_str(keyboard):
    assert str(keyboard) == "Dark Project KD87A"


def test_change_lang(keyboard):
    assert str(keyboard.language) == "EN"
    keyboard.change_lang()  # ��������� ��������� �� RU
    assert str(keyboard.language) == "RU"  # ��������� ���� ����������
    keyboard.change_lang().change_lang()  # ������ ���������� ���� ����������
    assert str(keyboard.language) == "RU"  # ��� ������� ���������, ���������� RU


def test_raises(keyboard):
    with pytest.raises(AttributeError):  # ������, �������������� ������ EN � RU
        keyboard.language = 'CH'
