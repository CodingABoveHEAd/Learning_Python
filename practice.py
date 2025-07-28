# a=10
# b=20

# def varcheck() :
#     global a,b;
#     a=15
#     b=25;
#     print('inside: ' ,a,b);

# varcheck();
# print('outside: ' , a,b);

f0=0;
f1=1;

n=int(input('Enter the range: '));

print(f0,end=" ");
for i in range (n):
    f2=f0+f1;
    f0=f1;
    f1=f2;
    print(f0,end=" ");