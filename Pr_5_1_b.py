from numpy import spacing


i=1
sp=2
st=1
while i<=5:
    if i<3:
        print(" "*sp,"*"*st)
        sp-=1;st+=2
    if i>=3:
        print(" "*sp,"*"*st)
        sp+=1;st-=2
    i+=1
    