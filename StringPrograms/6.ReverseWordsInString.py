#Prgram to reverse words in a given string
mystr=input("Enter a string:")
# first split the string into words 
words = mystr.split(' ')
revstr=""
for i in range(len(words)-1,-1,-1):
   revstr+=words[i]+" "
print(revstr)
