#program to check whether entered value is 0, else print the value
value=input("Enter a value")
value=int(value)
if ( value == 0 ):
    print("The value you entered was zero.")
    print("Please try again.")
else:
    print("Value =", value)
