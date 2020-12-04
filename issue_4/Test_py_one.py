from one_hot import fit_transform
import pytest


def test_base():
    """
    Проверка на равенство полученных значений с ожидаемым выводом функции
    """
    capitals = ['Moscow', 'New York', 'Moscow', 'London']
    transformed_cities = fit_transform(capitals)
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert transformed_cities == exp_transformed_cities


def test_numbers():
    """
    Проверка работы функции на получение списка из чисел
    """
    words = [0, 1, 3, 2, 4]
    transformed_words = fit_transform(words)
    exp_str = [
        (0, [0, 0, 0, 0, 1]),
        (1, [0, 0, 0, 1, 0]),
        (3, [0, 0, 1, 0, 0]),
        (2, [0, 1, 0, 0, 0]),
        (4, [1, 0, 0, 0, 0]),
    ]
    assert transformed_words == exp_str


def test_exception():
    """
    Проверка на исключение функции без параметров
    """
    with pytest.raises(TypeError):
        fit_transform()


def test_integer():
    """
    Проверка на исключение функции, получающей на вход цифру
    """
    number = 2
    with pytest.raises(TypeError):
        fit_transform(number)


def test_empty():
    """
    Проверка вывода функции, получающей на вход пустой список
    """
    city = []
    assert fit_transform(city) == []
