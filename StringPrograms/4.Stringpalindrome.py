#Prgram to revrse a string
mystr=input("Enter a string:")
revstr=""
for i in range(len(mystr)-1,-1,-1):
   revstr+=mystr[i]
if(mystr==revstr):
	print("Palindrome")
else:
	print("Not a palindrome")
