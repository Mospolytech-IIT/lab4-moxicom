"""
Этот файл содержит пользовательские исключения
"""

class NegativeValueError(Exception):
    """Ошибка, если значение отрицательное"""
    pass

class ZeroValueError(Exception):
    """Ошибка, если значение равно нулю"""
    pass

class LargeValueError(Exception):
    """Ошибка, если значение слишком большое"""
    pass
