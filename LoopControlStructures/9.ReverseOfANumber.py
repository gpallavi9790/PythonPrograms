#Prgram to print reverse of a number
n=int(input("Enter a number:"))
num=n
rev=0
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("Reverse of ",num, "=",rev)
