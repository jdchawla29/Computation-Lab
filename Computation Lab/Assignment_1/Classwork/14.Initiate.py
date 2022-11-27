class MEMS:
    def __init__(self, stream, batch):
        self.stream = stream 
        self.batch = batch 
    def identity(self):
        print ('student of', self.stream, self.batch)
student1=MEMS('physical_metallurgy', 'Btech')
student2=MEMS('process_metallurgy', 'Mtech')
student1.identity()
student2.identity()
print (student1.stream)