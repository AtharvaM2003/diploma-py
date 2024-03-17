def prime(num):
    x=0
    for i in range (2,num):
        if num%i==0:
            x=0
            break
        else:
            x=1
    return x
num=int(input("Enter Number: "))
num=abs(num)
y=prime(num)
if (y==1):
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime number")

