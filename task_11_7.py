class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + {self.b}i'

    def __add__(self, other):
        return f'{self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        return f'{self.a * other.a - self.b * other.b} + {self.b * other.a + self.a * other.b}i'


com1 = ComplexNumber(1, 2)
print(com1)
com2 = ComplexNumber(3, 4)
print(com2)
print(com1 + com2)
print(com1 * com2)