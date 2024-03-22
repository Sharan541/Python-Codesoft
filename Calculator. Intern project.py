import math as m


def add(p, q):
    return p + q

def subtract(p, q):
    return p - q

def multiply(p, q):
    return p * q

def divide(p, q):
    if q == 0:
        return "Cannot divide by zero"
    else:
        return p / q
def power(p,q):
    return p**q


print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Square Root ")

while True:
    choice = int(input("Enter choice: "))

    if choice in (1,2,3,4,5):
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        if choice ==1:
            print("Result:", add(n1, n2))
        elif choice ==2:
            print("Result:", subtract(n1, n2))
        elif choice ==3:
            print("Result:", multiply(n1, n2))
        elif choice ==4:
            print("Result:", divide(n1, n2))
        elif choice==5:
            print("Result:",power(n1,n2))
    elif choice==6:
        n=int(input("Enter the number:"))
        print("Result:",n**0.5)
    else:
        print("Invalid input")  

 
 