# a=10
# b=20

# def varcheck() :
#     global a,b;
#     a=15
#     b=25;
#     print('inside: ' ,a,b);

# varcheck();
# print('outside: ' , a,b);


def factorial(num):
    if num==0:
        return 1;
    return num*factorial(num-1);


res=factorial(4);
print(res);