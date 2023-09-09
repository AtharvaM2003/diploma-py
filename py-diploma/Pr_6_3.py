list=[]
noi=int(input("How many items you want to enter in list:"))
i=0
while i<noi:
    un=int(input("Enter Number in List : "))
    list.append(un)
    i+=1

print("The largest number in list is",max(list))