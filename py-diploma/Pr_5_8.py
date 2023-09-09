s=int(input("Enter Number to check wheather palindrome or not:"))
os=s
rn=0
while s>0:
    n=s%10
    rn=(rn*10)+n
    s//=10
if os==rn:
    print("The Number is Palindrome")
else:
    print("The Number is not Palindrome")