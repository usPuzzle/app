#matrix multiplication
#kada ovako uvezem biblioteku svaka fja npr array ce se pozivati kao numpy
from numpy import *
def matrix_mul(a,b):
    k=a.shape[0]
    c = zeros([k, k])
    l=b.shape[1]
    m=a.shape[1]
    print(k,l,m)
    #c=zeros([k,k])
    #print
    sum=0
    for i in range(k):
        for j in range(l):
            for z in range(m):
                sum=sum + a[i][z]*b[z][j]
                print(sum)
            c[i][j]=sum
            sum=0

    return c


m= int(input ("Unesi broj redova u matrici"))
n= int(input ("Unesi broj kolona u matrici"))

a=zeros([m,n])
b=zeros([m,n])

for i in range(m):
    for j in range(n):
        print("Unesi [", i, '][', j, "] element matrice A: ", end= "")
        a[i][j] = int(input())

for i in range(m):
    for j in range(n):
        print("Unesi [", i, '][', j, "] element matrice B: " , end= "")
        b[i][j] = int(input())


b=b.transpose()
print(a)
print(b)

c=matrix_mul(a,b)
a=matrix(a) #mora da se pretvori u matricu da bi radilo mnozenje, ovako mnozi samo elemnete niza
b=matrix(b)
d= a*b
print(c)
print(d)

