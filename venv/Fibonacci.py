
def Fibb(n):
    fibonaci = []
    a=0
    b=1
    fibonaci.append(a)
    fibonaci.append(b)
    for i in range (n-1):
        c=a+b
        a=b
        b=c
        fibonaci.append(c)

    return fibonaci

def recFact(n):
    if n==0:
        return 1
    else:
        return n*recFact(n-1)

m=int(input("Unesi ukupan broj F niza"))
print(Fibb(m))
print(recFact(m))