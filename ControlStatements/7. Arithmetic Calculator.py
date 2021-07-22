#Program to build arithmetic calculator in R
print("1) For Addition.")
print("2) For Subtraction.")
print("3) For Division.")
print("4) For multiplication.")
n1=input("Enter first number:")
n2=input("Enter second number:")
choice=input("Enter your choice:")
n1=int(n1)
n2=int(n2)
choice=int(choice)
if(choice==1):
    add=(n1+n2)
    print("sum=",add)
elif(choice==2):
    sub=(n1-n2)
    print("sub=",sub)
elif(choice==3):
    div=n1/n2
    print("Division=",div)
elif(choice==4):
    mul=n1*n2
    print("mul=",mul)
else:
    print("wrong choice")
