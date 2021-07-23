#Prgram to check for symmetrical string
mystr=input("Enter a string:")
n=len(mystr)
mid=n//2
firsthalf=mystr[0:mid]
secondhalf=mystr[mid:n]
if(firsthalf==secondhalf):
   print("Symmetrical String")
else:
   print("Not a Symmetrical String")
