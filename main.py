"""
Файл main.py для вызова всех функций (шаг 9)
"""

from functions import (
    divide,
    square_root,
    convert_to_int,
    safe_division,
    calculate_percentage,
    string_length,
    multiply_elements,
    validate_and_process_data,
    check_positive_number,
    open_file,
    parse_int,
    calculate_square_area,
)

if __name__ == "__main__":
    try:
        print(divide(10, 0))
        print(square_root(-4))
        print(convert_to_int("abc"))
        print(safe_division(10, 0))
        print(calculate_percentage(-5, 10))
        print(string_length(123))
        print(multiply_elements([1, "two", 3], 2))
        validate_and_process_data(150)
        print(check_positive_number(-1))
        open_file("non_existent_file.txt")
        print(parse_int("not_a_number"))
        print(calculate_square_area(-10))
    except Exception as e:
        print(f"Ошибка в main: {e}")
