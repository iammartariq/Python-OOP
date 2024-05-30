class Student:

    __name = ""
    __roll = ""
    __marks = [0, 1, 2]

    def set_name(self, n):
        self.__name = n

    def set_roll(self, r):
        self.__roll = r

    def set_marks(self, m):
        self.__marks = m

    def get_name(self):
        return self.__name
    
    def get_roll(self):
        return self.__roll
    
    def get_marks(self):
        return self.__marks
    
    def avg(self):
        return(self.__marks[0] + self.__marks[1] + self.__marks[2])/3
    
    def show(self):
        print("marks:", self.__marks)
        print("name:",self.__name)
        print("roll number:", self.__roll)

s1 = Student()
s1.set_name("Ammar")
s1.set_roll("23132")
s1.set_marks([23, 23, 24])
data = s1.show()
result = s1.avg()
print(data)
print(result)
