#program to swap using third variable
a,b=input('enter two values:').split()
a=int(a)
b=int(b)
print("before interchange:")
print("a=",a)
print("b=",b)
temp=a
a=b
b=temp
print("after interchange:")
print("a=",a)
print("b=",b)
