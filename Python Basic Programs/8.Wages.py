#Program to take hours and rate per hour and print gross pay
hours=input("Enter number of hours")
hours=int(hours)

rate=input("Enter rate per hour in Rs.")
rate=float(rate)

gross_pay=hours*rate

print("The gross pay =",gross_pay)
