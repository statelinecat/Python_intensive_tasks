def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

print("Конвертер расстояний: км ↔ мили")
print("1. Километры в мили")
print("2. Мили в километры")

while True:
    try:
        choice = int(input("Выберите вариант (1 или 2): "))
        if choice in (1, 2):
            break
        print("Ошибка: введите 1 или 2")
    except ValueError:
        print("Ошибка: введите число")

while True:
    try:
        value = float(input("Введите расстояние: "))
        if value >= 0:
            break
        print("Ошибка: расстояние не может быть отрицательным")
    except ValueError:
        print("Ошибка: введите число")

if choice == 1:
    result = km_to_miles(value)
    print(f"{value} км = {result:.2f} миль")
else:
    result = miles_to_km(value)
    print(f"{value} миль = {result:.2f} км")