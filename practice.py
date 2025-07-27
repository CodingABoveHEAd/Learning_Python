from math import sqrt,pow

#print('Hello world');
# x=5;
# x+=10;
# b=x;
# c=2+3j;
# #print(x);
# nums=[12,25,30,50,12];
# dic={1:'niloy',2:'adit',3:'ankon'};
# print(id(x));
# print(id(b));
# x+=1;
# #print(id(x));
# #print(type(c));

# p=25;
# pp=sqrt(p);
# print(pp);

# del dic[1];
#print(dic);
#print(dic.get(1));
# print(nums);




# age=int(input('enter your age: '));

# if age<20:
#     print('Teenage');
# elif age>=20 and age<45:
#  print('Young');

# else:
#     print('Old');


# i=1;

# fruits=['apple','banana','mango','pineapple'];

# for fruit in fruits:
#     print(fruit);

# for i in range(11,31,2):
#     print(i);
# else:
#     print('Reached the endpoint');

x=int(input('Enter the number: '));
i=2;
flag=0;
while i<x :
    if x%i==0:
        flag=1;
        break;
    else :
        i+=1;

if flag :
    print('not prime');
else :
    print('prime');




# while i<=5:
#     print('Niloy is a Joker');
#     i+=1;
