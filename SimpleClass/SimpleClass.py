import math

class ComplexNumber:
    '''This is a simple class.'''
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def abs(self):
        return math.sqrt(self.real * self.real + self.imag * self.imag)
        

c1 = ComplexNumber()
c2 = ComplexNumber(1, 2)
c3 = ComplexNumber(1, 1)
print(c1)
print(c2.add(c3))
print(c2.add(c3).abs())
