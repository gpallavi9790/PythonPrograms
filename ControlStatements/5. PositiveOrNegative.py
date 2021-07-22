#program to check whether entered value is zero, positive or negative
value=input("Enter a value")
value=int(value)
if ( value == 0 ):
    print("The value you entered was zero..") 
else:
    if ( value < 0 ):
        print(value, " is negative") 
    else:
    	print(value, " is positive")
