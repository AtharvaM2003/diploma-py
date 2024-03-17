from tokenize import String


l=[]
T=("Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine")
num=input("Enter Number: ")
for i in num:
    j =int(i)
    l.append(T[j])
print(l)