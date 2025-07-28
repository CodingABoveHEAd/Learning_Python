class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap=self.laptop()

    def show(self):
        print(self.name, self.roll);
        self.lap.show()

    class laptop:

        def __init__(self):
            self.brand='HP'
            self.cpu='ryzen7'
            self.ram=8

        def show(self):
            print(self.brand,self.cpu,self.ram)

    
s1=student('niloy',117);
s2=student('nishan',116);

lap1=s1.lap

s1.show();