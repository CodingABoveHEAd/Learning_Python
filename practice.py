class person:
    Class='2nd year';
    def __init__(self):
        self.name='niloy'
        self.age=23

    def update(self):
        self.name='niloy'

    def compare(self,other):
        return self.name==other.name
        
c1=person();
c2=person();

#print(c1.name);
c2.name='Nishan'
#print(c2.name);
c2.update();


c2.Class='3rd year';
print(c1.Class);

if c1.compare(c2):
    print('same');
else:
    print('different');

