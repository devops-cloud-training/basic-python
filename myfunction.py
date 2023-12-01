# try:
def add(a,b=0):
    c=a+b
    return c

def subtract(a,b):
    c=a-b
    return c

def multiply(a,b):
    c=a*b
    return c

def divide(a,b):
    c=a/b
    return c

a= int(input("Enter the number for a:"))
b= int(input("Enter the number for b:"))
print(add(a,b))
print(add(a))
print(subtract(a,b))

c=int(input("Enter the number for c"))
d=int(input("Enter the number for d"))

print(add(c,d))
print(multiply(c,d))
print(divide(c,d))


# except ValueError:
#     print("Hey please enter the integer properly.")

