from math import sqrt
from unittest import result

message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'
print(message)


def CalculateSquareRoot(Number) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number: float) -> None:
    """Функция калькулятора."""
    if your_number <= 0:
        return
    result = CalculateSquareRoot(your_number)
    print(f"Мы вычислили квадратный корень из введённого вами числа. Это будет"
          f": {result}")


print(message)
calc(25.5)
