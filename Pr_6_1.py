#new list
list=[]
#items to take in list
noi=int(input("How many items you want to enter in list:"))
i=0
while i<noi:
    un=int(input("Enter Numbers in List : "))
    list.append(un)
    i+=1

print("The sum of number in list",sum(list))