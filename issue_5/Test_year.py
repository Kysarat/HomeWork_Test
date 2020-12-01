from unittest.mock import patch
from year_now import what_is_year_now
import pytest


def test_year():
    """
    Тест на проверку даты, введённой YYYY-MM-DD - 2020-03-01
    """
    data = {"currentDateTime": "2020-11-05"}
    with patch('year_now.json.load', return_value=data):
        year = what_is_year_now()
    exp_year = 2020
    assert exp_year == year


def test_data():
    """
    Тест на проверку даты, введённой DD.MM.YYYY - 01.03.2020
    """
    data = {"currentDateTime": "05.11.2020"}
    with patch('year_now.json.load', return_value=data):
        year = what_is_year_now()
    exp_year = 2020
    assert exp_year == year


def test_wrong_data():
    """
    Тест на дату, введённую с ошибкой
    Должно быть DD.MM.YYYY
    На вход поступает DD-MM-YYYY
    """
    data = {"currentDateTime": "05-11-2020"}
    with patch('year_now.json.load', return_value=data):
        with pytest.raises(ValueError):
            what_is_year_now()


def test_wrong_year():
    """
    Тест на дату, введённую с ошибкой
    Должно быть YYYY-MM-DD
    На вход поступает YYYY.MM.DD
    """
    data = {"currentDateTime": "2020.11.05"}
    with patch('year_now.json.load', return_value=data):
        with pytest.raises(ValueError):
            what_is_year_now()


def test_index():
    """
    Тест, которые не сможет обратиться к datetime_str
    для разделения индекса
    """
    data = {"currentDateTime": "2020"}
    with patch('year_now.json.load', return_value=data):
        with pytest.raises(IndexError):
            what_is_year_now()
