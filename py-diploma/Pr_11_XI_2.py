def fact(num):
    f = 1
    if num < 0:
        print("Enter Positive number")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num+1):
            f = f*i
        return f

num = int(input("Enter a number: "))
facto=fact(num)
print(f"The factorial of {num} is {facto}")