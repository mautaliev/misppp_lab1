"""Тесты"""

from data_service_lib import DataService


def test_calc():
    x = 5
    assert DataService.calc(x) == -0.387
