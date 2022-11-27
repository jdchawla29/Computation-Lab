class student:
    dept = 'MEMS'
    def __init__(self, m1, m2, m3, m4):
        self.m1=m1
        self.m2 =m2
        self.m3=m3
        self.m4 =m4
    def avg(self):
        return (self.m1+self.m2+ self.m3+self.m4)/4
S1= student(36, 28, 39, 47)
S2=student(87,98, 99, 92)
print (S1.avg())
print (S2.avg())