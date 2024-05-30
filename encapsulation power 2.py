class Power:
    base = 0
    exponent = 0
    def find_power(self, base, exponent):
        self.base = base
        self.exponent = exponent
        return self.base**self.exponent
    
p = Power()
# p.base = 2
# p.exponent = 3
result = p.find_power(-2,3)
print(result)