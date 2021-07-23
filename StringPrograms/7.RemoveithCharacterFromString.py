#Prgram to remove i'th character from a string
mystr="Pallavi Gupta"
# Removing char at pos 3
# using replace, removes all occurences
newstr = mystr.replace('l', '')
print ("The string after removal of i'th character (all occurences): " + newstr)
  
# Removing 1st occurrence of 
# if we wish to remove it.
newstr = mystr.replace('l', '', 1)
print ("The string after removal of i'th character : " + newstr)
