from fractions import Fraction

number = 9.75
fraction = Fraction(number).limit_denominator()  # Находим дробное представление

print(f"{number} ≈ {fraction.numerator}/{fraction.denominator}")