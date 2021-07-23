#Prgram to check Armstrong Number
n=int(input("Enter a number:"))
num=n
noofdigits=len(str(n))
sum=0
while(n>0):
    digit=n%10
    sum=sum+digit**noofdigits
    n=n//10
if(num==sum):
    print(num," is an Armstrong number")
else:
    print(num," is not an Armstrong number")
