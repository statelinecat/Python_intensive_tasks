while True:
    try:
        number = int(input("Введите целое число: "))
        break
    except ValueError:
        print("Ошибка! Введите целое число. Попробуйте ещё раз.")

if number % 5 == 0:
    print(f"✓ {number} кратно 5")
else:
    print(f"✗ {number} не кратно 5 (остаток {number % 5})")