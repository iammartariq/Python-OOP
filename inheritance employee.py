class Employee:
    def __init__(self, hwr, hw):
        self.hwr = hwr
        self.hw = hw

    def find_pay(self):
        return self.hwr * self.hw
    
    def display(self):
        print("Hourly wage rate:", self.hwr)
        print("Hours worked:", self.hw)
        print("Salary:", self.find_pay())

class Salesman(Employee):
    def __init__(self, hwr, hw, ts):
        super().__init__(hwr, hw)
        self.ts = ts

    def set_ts(self, ts):
        self.ts = ts

    def get_ts(self):
        return self.ts

e1 = Employee(600, 40)
e1.display()

e2 = Salesman(250, 40, 1000)
e2.display()
e2.get_ts()
