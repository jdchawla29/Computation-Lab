class MEMS:
    def __init__(self):
        self.batch = "BTECH"
        self.year = 2008
        self.stream ="corrosion"
        self.credit =48
    def update(self):
        if self.stream == "Process_metallurgy":
            print ('course credit is', self.credit)
    def compare(self, other):
        if self.credit == other.credit:
            return True
student1=MEMS()
student2=MEMS()
student1.batch = "MTECH"
print(student1.batch)
student2.batch = "MTECH"
student2.year = 2020
student2.stream = "Process_metallurgy"
student2.update()
if student1.compare(student2):
    print("Same")