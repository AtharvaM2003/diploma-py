n=int(input("Enter the Number: "))
if n<=0:
    print("Enter Positive Number")
else:
    sum=0
    while (n > 0):
        sum += n
        n -= 1
    print("The sum of natural number is", sum)
