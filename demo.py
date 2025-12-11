#1.try 2.except 3.else 4.finaly 

try:
    number=int(input("type in a number:"))
    1/number
except ZeroDivisionError:
    print("cna divide by zero")
except ValueError:
    print("theres some wrong")
else:
    print("there is no error")
finally:
    print("this is the end")
