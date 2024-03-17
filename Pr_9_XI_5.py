from re import T
d={'a':80,'b':15,'d':10,'e':20,'c':40}
l=[v for v in d.values()]
l=sorted(l,reverse=True)
print(l[0:3])