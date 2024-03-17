
list1=[10,20,70,90]
list2=[20,80,70,12]
cl=[]
i=0
j=0
for i in list1:
    for j in list2:
        if i==j:
            cl.append(i)
print("The common List is:",cl)

