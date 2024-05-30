class Fraction:
    def set_numerator(self, n):
        self.num = n

    def set_denominator(self, d):
        if d == 0:
            self.den = 1
        else:
            self.den = d

    def get_fraction(self):
        return self.num, self.den
    
    def get_decimal(self):
        return self.num/self.den
    
f1 = Fraction()
f1.set_numerator(4)
f1.set_denominator(10)
print(f1.get_fraction())
print(f1.get_decimal())

f2 = Fraction()
f2.set_numerator(9)
f2.set_denominator(0)
print(f2.get_fraction())
print(f2.get_decimal())