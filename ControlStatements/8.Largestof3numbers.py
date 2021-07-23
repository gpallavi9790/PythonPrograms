#Program to print largest of three numbers
n1,n2,n3=input("Enter three numbers:").split(" ")
n1=int(n1)
n2=int(n2)
n3=int(n3)
if(n1>n2 and n1>n3):
    print(n1," is largest")
elif(n2>n1 and n2>n3):
    print(n2," is largest")
else:
    print(n3," is largest")
