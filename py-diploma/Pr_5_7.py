s=int(input("Enter Number to perform sum of digit:"))
os=s
sum=0
while s>0:
    n=s%10
    sum=sum+n
    s//=10
print("The sum of digits is",sum)  
