#Prgram to check if a number is palindrome or not
n=int(input("Enter a number:"))
num=n
rev=0
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
if(rev==num):
    print(num," is a palindrome")
else:
    print(num," is not a palindrome")
