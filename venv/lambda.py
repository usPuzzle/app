from functools import reduce
f= lambda a: a*a

b= f(4)
print(b)

def is_even(n):
    return n%2==0

nums=[3,2,6,8,4,6,2,9]

even=list (filter(lambda n: n%2==0,nums))

doubles = list (map(lambda n: n*2, even))

sum = reduce (lambda a,b: a+b, doubles )
print (even)
print (doubles)
print(sum)
print (__name__)