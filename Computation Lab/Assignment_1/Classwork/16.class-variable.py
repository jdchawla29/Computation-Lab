class MEMS:
    year =2020
    def __init__(self):
        self.roll=10957 
        self.name= "Arpit"
student1 =MEMS()
student2 =MEMS()
student2.name ="Rohit"
student2.roll = 10958
print(student1.roll)
print(student2.roll)
print(MEMS.year)
MEMS.year = 2018
print (MEMS.year)