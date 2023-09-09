da={}
dd={}
d={'a':80,'b':15,'d':10,'e':20,'c':40}
l=[i for i in d.values()]
la=sorted(l)
ld=sorted(l,reverse=True)
for i in la:
    for j in d.keys():
        if i ==d[j]:
            da.update({j:i})
            break
print("The Dictionary in ascending order",da)
for i in ld:
    for j in d.keys():
        if i ==d[j]:
            dd.update({j:i})
            break
print("The Dictionary in ascending order",dd)