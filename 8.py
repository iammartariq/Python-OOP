class Int:
    def __init__(self, value = 0):
        self.value = value

    def set_value(self, value):
        self.value = value 

    def get_value(self):
        return self.value
    
    def add(self, addition):
        result = (self.value + addition.value)
        return Int(result)
    
    def display(self):
        print(self.value)

    
int1 = Int(5)
int2 = Int(10)
int3 = int1.add(int2)
int3.display()