class student:
    def __init__(self, name, roll):
        self.name =name
        self.roll= roll
        self.special = self.special()
    def show(self):
        print(self.name, self.roll)
    class special:
        def __init__(self):
            self.stream = 'corrosion'
            self.credit = 48
        def show(self):
            print(self.stream, self.credit)
S1 =student("Manish", 10456)
S1.special.stream ="physical_metallurgy"
S1.show()
S1.special.show()
print (S1.special.credit)