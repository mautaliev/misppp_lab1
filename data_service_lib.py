"""
Лабораторная 1. Вариант 5.
Решил попробовать написать на питоне, намного ближе этот язык
"""

__author__ = 'Мауталиев С. И.'

import math


class DataService:
    @staticmethod
    def calc(x: float) -> float:
        if math.cos(x) == 0:
            raise ValueError("Недопустимое значение x, так как cos(x) равен 0.")
        numerator = math.log(abs(math.cos(x)))
        denominator = math.log(1 + x ** 2)
        if denominator == 0:
            raise ValueError("Знаменатель равен 0, выражение не может быть вычислено.")
        z = numerator / denominator
        return round(z, 3)
