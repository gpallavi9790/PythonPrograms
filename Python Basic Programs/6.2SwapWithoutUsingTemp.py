#program to swap without using third variable
a,b=input('enter two values:').split()
a=int(a)
b=int(b)
print("before interchange:")
print("a=",a)
print("b=",b)
a=a+b
b=a-b
a=a-b
print("after interchange:")
print("a=",a)
print("b=",b)
