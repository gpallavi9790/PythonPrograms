#program to swap using Python Multiple Assignment
a,b=input('enter two values:').split()
a=int(a)
b=int(b)
print("before interchange:")
print("a=",a)
print("b=",b)
a,b=b,a
print("after interchange:")
print("a=",a)
print("b=",b)
