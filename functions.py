"""Этот файл содержит функции с различными обработками исключений"""

from custom_exceptions import NegativeValueError, ZeroValueError, LargeValueError

# Шаг 1 - Функции без обработчика исключений
def divide(a, b):
    """Возвращает результат деления, выбрасывает исключение при делении на ноль"""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно.")
    return a / b

def square_root(x):
    """Возвращает квадратный корень, выбрасывает исключение при отрицательном значении"""
    if x < 0:
        raise ValueError("Невозможно взять корень из отрицательного числа.")
    return x ** 0.5

# Шаг 2 - Функция с обработчиком исключения общего типа
def convert_to_int(value):
    """Преобразует значение к целому числу"""
    try:
        return int(value)
    except Exception as e:
        print(f"Ошибка при конвертации: {e}")
        return None

# Шаг 3 - Функция с обработчиком исключения общего типа и блоком finally
def safe_division(a, b):
    """Выполняет безопасное деление с обработкой исключений"""
    try:
        result = a / b
    except Exception as e:
        print(f"Ошибка при делении: {e}")
        result = None
    finally:
        if result is None:
            print("Возвращаем значение по умолчанию: 0")
            result = 0
    return result

# Шаг 4 - Функции с несколькими обработчиками исключений
def calculate_percentage(numerator, denominator):
    """Возвращает процентное значение, обрабатывает разные типы исключений"""
    try:
        if numerator < 0:
            raise NegativeValueError("Числитель не может быть отрицательным.")
        elif denominator == 0:
            raise ZeroValueError("Знаменатель не может быть равен нулю.")
        elif numerator > 1000:
            raise LargeValueError("Числитель слишком большой.")
        return (numerator / denominator) * 100
    except NegativeValueError as e:
        print(f"Ошибка: {e}")
    except ZeroValueError as e:
        print(f"Ошибка: {e}")
    except LargeValueError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Завершение работы функции calculate_percentage")

def string_length(s):
    """Возвращает длину строки, обрабатывает разные исключения"""
    try:
        if not isinstance(s, str):
            raise TypeError("Входное значение должно быть строкой.")
        if s == "":
            raise ValueError("Строка не может быть пустой.")
        if len(s) > 100:
            raise LargeValueError("Строка слишком длинная.")
        return len(s)
    except TypeError as e:
        print(f"Ошибка типа: {e}")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except LargeValueError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Завершение работы функции string_length")

def multiply_elements(elements, factor):
    """Умножает элементы списка на заданный множитель, обрабатывает исключения"""
    try:
        if not isinstance(elements, list):
            raise TypeError("Ожидается список.")
        for elem in elements:
            if not isinstance(elem, (int, float)):
                raise ValueError("Все элементы списка должны быть числами.")
        return [elem * factor for elem in elements]
    except TypeError as e:
        print(f"Ошибка типа: {e}")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    finally:
        print("Завершение работы функции multiply_elements")

# Шаг 5 - Функция с генерацией исключений и их обработкой
def validate_and_process_data(value):
    """Валидация и обработка данных с генерацией исключений"""
    try:
        if value < 0:
            raise NegativeValueError("Отрицательное значение недопустимо.")
        elif value == 0:
            raise ZeroValueError("Значение не может быть нулевым.")
        elif value > 100:
            raise LargeValueError("Значение слишком большое.")
        print(f"Значение {value} прошло валидацию")
    except NegativeValueError as e:
        print(f"Обработка ошибки: {e}")
    except ZeroValueError as e:
        print(f"Обработка ошибки: {e}")
    except LargeValueError as e:
        print(f"Обработка ошибки: {e}")
    finally:
        print("Завершение работы функции validate_and_process_data")

# Шаг 7 - Функция, выбрасывающая пользовательское исключение
def check_positive_number(number):
    """Проверяет, что число положительное, выбрасывает NegativeValueError при ошибке"""
    try:
        if number < 0:
            raise NegativeValueError("Число должно быть положительным.")
        return f"Число {number} положительное"
    except NegativeValueError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Завершение работы функции check_positive_number")

# Шаг 8 - Дополнительные функции
def open_file(file_path):
    """Открывает файл, демонстрация исключений при работе с файлами"""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("Файл не найден.")
    except IOError:
        print("Ошибка ввода-вывода при работе с файлом.")

def parse_int(value):
    """Парсинг целого числа, демонстрация исключений"""
    try:
        return int(value)
    except ValueError:
        print("Неверное значение: требуется целое число.")
    except TypeError:
        print("Неверный тип данных для парсинга.")

def calculate_square_area(side_length):
    """Рассчитывает площадь квадрата"""
    if side_length <= 0:
        raise ValueError("Длина стороны должна быть положительным числом.")
    return side_length * side_length
