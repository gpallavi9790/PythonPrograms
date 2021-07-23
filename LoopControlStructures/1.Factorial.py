#Prgram to print factorial of a number
a=input("Enter a number:")
a=int(a)
fact=1
for i in range(1,a+1):
    fact=fact*i
print("Factorial of ",a,"=",fact)
