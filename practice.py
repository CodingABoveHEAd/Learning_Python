class A:
    def mA(self):
     print('This is class A');

class B(A):
   def mB(self):
    print('This is class B');

class C(B):
   def mC(self):
    print('This is class C');

obj1=C();

obj1.mA();

