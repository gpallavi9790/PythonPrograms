#Prgram to check whether a number entered is prime or not
a,b=input("Enter start and end of a range:").split()
a=int(a)
b=int(b)
print("All the prime number in the range",a," to ",b)
for j in range(a,b+1):
    count=0
    for i in range(1,j+1):
        if(j%i==0):
            count=count+1
    if(count==2):
        print(j)

