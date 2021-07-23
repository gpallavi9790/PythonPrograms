#Prgram to revrse a string
mystr=input("Enter a string:")
newstr=""
for i in range(len(mystr)-1,-1,-1):
   newstr+=mystr[i]
print("Original String=",mystr)
print("Reversed String=",newstr)


#Using Slicing Operator
#print(mystr[::-1])
