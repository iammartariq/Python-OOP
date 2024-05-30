class Time:
    def __init__(self, h = 0, m = 0, s = 0):
        self.hour = h
        self.minute = m
        self.second = s

    def print_time(self):
        print(self.hour, ":", self.minute, ":", self.second, sep = "")

    def add_time(self, t):
        self.second += t.second
        if self.second >= 60:
            self.second -= 60
            self.minute += 1

        self.minute += t.minute
        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1

        self.hour += t.hour
        if self.hour >= 24:
            self.hour -= 24

t1 = Time(23, 44, 30)
t1.print_time()

t2 = Time(2, 4, 30)
t2.print_time()

t1.add_time(t2)
t1.print_time()