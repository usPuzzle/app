a=5
b=2

try:
    print("open")
    print(a/b)
    k=int(input("Unesi broj"))

except ZeroDivisionError as e:
    print("ne moze se deliti 0", e)
except ValueError as e:
    print("Invalid input")
except Exception as e:
    print("univerzalni eksepsn")
finally:
    print("close")
print("bye")