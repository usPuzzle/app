from numpy import *
"""
from array import *
vals = array('i', [5,9,-8,4,2])

newArr = array(vals.typecode, (a*a for a in vals))

for e in newArr:
    print(e)

arr = array('i', [])

n = int(input("Unesi broj clanova niza"))

for i in range (n):
    x = int(input("Unesi element niza"))
    arr.append(x)

print(arr)

val = int(input("Unesi broj za pretrgu"))

k =0
for e in arr:
    if e==val:

        print(k)
        break

    k=k+1
print (arr.index(val))


arr = array([1,2,3,4,5.0])
arr1 = linspace(0,16,10)
arr2 = arange(1,15,2)
arr3=logspace(1,40,5)
arr4=zeros(5)
#arr5=ones(5,int)

#print (arr3)
#print('%.2f'%arr3[4])


arr1= array([1,2,3,4,5])
arr2 = array([6,1,9,3,2])

arr3=arr1 + arr2
# print(arr3)
"""
#dvodimenzionalni niz
arr= array([
    [1,2,3,7,8,9],
    [4,5,6,10,11,12]
])

arr1=arr.flatten()
arr2 = arr1.reshape(3,4)

#print(matrix1.ndim)
#print(matrix1.shape)
#print(matrix1.size)
#print(arr2)

m = matrix(arr)
m1= matrix('1 2 3; 4 5 6; 7 8 9')
m2= matrix('1 2 3; 4 5 6; 7 8 9')
m3=m1*m2

print (m)
print(m1)
print(m1.max())
print(m3)