numbers = list(map(float, input("Введите список чисел через пробел: ").split()))

for num in numbers:
    if num < 0:
        break  # Выход из цикла при обнаружении отрицательного числа
    print(num, end=" ")  # Вывод положительных чисел