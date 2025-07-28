# f = lambda a,b : a*b;
# print(f(5,6));
from functools import reduce

nums=[3,4,5,54,2];

res1=list(filter(lambda n: n%2==0 ,nums));
print(res1);
res=list(map( lambda n : n*2  ,res1));
print(res);
res=(reduce( lambda a,b : a+b  ,res));
print(res);