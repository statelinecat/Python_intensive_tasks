def convert_minutes_to_dhm(total_minutes):
    """Преобразует минуты в формат 'дни:часы:минуты'"""
    hours = total_minutes // 60
    remaining_minutes = total_minutes % 60

    days = hours // 24
    remaining_hours = hours % 24

    return f"{days}:{remaining_hours}:{remaining_minutes}"


def get_positive_input(prompt):
    """Запрашивает ввод, пока не будет введено положительное число"""
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Ошибка: число должно быть неотрицательным. Попробуйте ещё раз.")
        except ValueError:
            print("Ошибка: введите целое число. Попробуйте ещё раз.")


# Основная программа
total_minutes = get_positive_input("Введите количество минут: ")
print("Результат:", convert_minutes_to_dhm(total_minutes))