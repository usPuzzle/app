num = int(input("Unesi broj za proveru"))

for i in range (2,num):
    if num % i == 0:
        print ("Nije prost broj!")
        break
else:
        print("Prost broj")

print(__name__)