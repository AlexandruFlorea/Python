from math import gcd


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.denom = bottom

    def __str__(self):
        return f"{self.num}/{self.denom}"

    def __add__(self, other):
        new_num = self.num * other.denom + self.denom * other.num
        new_denom = self.denom * other.denom
        common_divisor = gcd(new_num, new_denom)

        return Fraction(new_num // common_divisor, new_denom // common_divisor)

    def __sub__(self, other):
        new_num = self.num * other.denom - self.denom * other.num
        new_denom = self.denom * other.denom
        common_divisor = gcd(new_num, new_denom)

        return Fraction(new_num // common_divisor, new_denom // common_divisor)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_denom = self.denom * other.denom
        common_divisor = gcd(new_num, new_denom)

        return Fraction(new_num // common_divisor, new_denom // common_divisor)

    def divide(self, other):
        new_num = self.num * other.denom
        new_denom = self.denom * other.num
        common_divisor = gcd(new_num, new_denom)

        return Fraction(new_num // common_divisor, new_denom // common_divisor)

    def inverse(self):
        return f"{self.denom}/{self.num}"


my_f1 = Fraction(20, 30)
my_f2 = Fraction(4, 8)
my_f3 = Fraction(1, 2)

print(my_f1 + my_f2 + my_f3)
print(my_f1 - my_f2 + my_f3)
print(my_f1 * my_f2 + my_f3)
print(my_f1.divide(my_f2))
print(my_f3.inverse())
