#Prgram to print fibonacci series
a,b=input("Enter first two numbers of fibonacci series:").split()
a=int(a)
b=int(b)
n=int(input("Enter length of fibonacci series"))
print("Fibonacci Series is")
print(a)
print(b)
for j in range(3,n+1):
    c=a+b
    print(c)
    a=b
    b=c
