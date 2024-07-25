from math import sqrt
from typing import Optional


def add_numbers(x_1: int, x_2: int) -> int:
    return x_1 + y_1


def calculate_square_root(number: float) -> float:
    return sqrt(number)


def calc(your_number):
    if your_number <= 0:
        return None
    result: Optional[str] = calculate_square_root(your_number)
    return ('Мы вычислили квадратный корень из введённого вами числа. )'
            f'Это будет: {result}')


x_1: int = 10
y_1: int = 5

print("Сумма чисел: ", add_numbers(x_1, y_1))

print(calc(25.5))
