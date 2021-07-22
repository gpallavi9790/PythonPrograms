#Program to print age group of person by his/her age
age=input("Enter age:")
age=int(age)
if(age<18):
    print("You are child")
elif(age>30):
    print("You are old guy")
else:
    print("You are adult")
