s=int(input("Enter Number to reverse:"))
rn=0
while s>0:
    n=s%10
    rn=(rn*10)+n
    s//=10
print("The Reverse Number is",rn)