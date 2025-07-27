a=10
b=20

def varcheck() :
    global a,b;
    a=15
    b=25;
    print('inside: ' ,a,b);

varcheck();
print('outside: ' , a,b);