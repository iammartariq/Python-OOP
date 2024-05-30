class Tracker:
    count = 0
    def __init__(self):
        Tracker.count += 1
        self.serial_no = Tracker.count

    def report(self):
        print(self.serial_no)

t1 = Tracker()
t1.report()
t2 = Tracker()
t2.report()
t3 = Tracker()
t3.report()
print(t1.__dict__, t2.__dict__, t3.__dict__)