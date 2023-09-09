t=tuple()
n=int(input("Total number of values in tuple: "))
for i in range(n):
    a=input("Enter elements: ")
    t=t+(a,)
print(t)
count=t.count(a)
if count>1:
    print("The repeated value is:",a)
print("The Value of ",a," is repeated for ",count," times")