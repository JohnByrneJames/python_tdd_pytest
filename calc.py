class Calc:

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2

    def cm_to_inch(self, num1):
        return round(num1 / 2.54, 2)

    def modulus(self, num1, num2):
        return num1 % num2


simple_calc = Calc()

print(simple_calc.add(2, 2))
