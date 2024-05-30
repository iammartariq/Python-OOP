class Employee:
    name = ""
    ID = 1
    designation = ""
    basic_salary = 0.0

    def find_salary(self, ded, bon):
        self.deduction = ded
        self.bonus = bon
        return self.basic_salary - ded + bon

E1 = Employee()
E1.name = "Ammar"
E1.ID = 21564
E1.designation = "Teacher"
E1.basic_salary = 30000
Salary = E1.find_salary(2300, 1500)
print("name:", E1.name)
print("salary:", Salary)