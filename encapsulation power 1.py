class Power:
    base = 0
    exponent = 0
    
    def find_power(self, b, e):
        self.base = b
        self.exponent = e
        return self.base**self.exponent
    
    def set_base(self, b):
        if b >=0:
            self.base = b
    
    def get_base(self):
        return self.base
    
    def set_exponent(self, e):
        if e>= 0:
            self.exponent = e
        
    def get_exponent(self):
        return self.exponent
    
p = Power()
p.set_base = 2
p.set_exponent = 3
result = p.find_power()
print(result)