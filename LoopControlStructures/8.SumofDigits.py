#Prgram to print sum of digits of a number
n=int(input("Enter a number:"))
num=n
sum=0
while(n>0):
    digit=n%10
    sum=sum+digit
    n=n//10
print("Sum of digits of ",num, "=",sum)
