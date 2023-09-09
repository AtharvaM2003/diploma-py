#new list
list=[]
#items to take in list
noi=int(input("How many items you want to enter in list:"))
i=0
mul=1
while i<noi:
    un=int(input("Enter Number in List : "))
    list.append(un)
    i+=1
for i in list:
    mul*=i
print("The Multiplication of number in list",mul)
