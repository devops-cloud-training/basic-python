a=50
b=10

c=a+b

# Arithmetic operator

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**2)

# Logical operator
a=True
b=False

print(a and b)
print(a or b)
print(not a)

# Assignment operator

a=10
print(a)
b=20
print(b)
c=a+b
print(c)
c+=20 # c=c+20
print(c)
c-=10 # c = c-10
print(c)
c*=5   # c = c*10
print(c)
c/=5 # c = c/5
print(c)
c//=5 # c = c//5
print(c)
c**=5 # c = c**5
print(c)
c%=5 # c = c%5
print(c)

# comparison operator

a=10
b=20

print(a==b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a!=b)

# bitwise operator

a=5
# 00000101 00000001
# 00010100
# 11111010

b=2
#010
# 000
# 111
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a>>2)
print(a<<2)

#special operators

a=5
b=10
#identity and membership operator
print(a is b)
print(a is not b)

a="sathish"
b="a"
print(b in a)
print(b not in a)

a=[1,2,3,4,5,6,7,78]
b="4"
print(b in a)
print(b not in a)