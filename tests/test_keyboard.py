import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_str(keyboard):
    assert str(keyboard) == "Dark Project KD87A"


def test_change_lang(keyboard):
    assert str(keyboard.language) == "EN"
    keyboard.change_lang()  # Изменение раскладки на RU
    assert str(keyboard.language) == "RU"  # Изменённый язык клавиатуры
    keyboard.change_lang().change_lang()  # Дважды изменяется язык клавиатуры
    assert str(keyboard.language) == "RU"  # При двойном изменение, возвращает RU


def test_raises(keyboard):
    with pytest.raises(AttributeError):  # Ошибка, поддерживается только EN и RU
        keyboard.language = 'CH'
