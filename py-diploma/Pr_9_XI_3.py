d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
d3={}

for i in d1.keys():
    for j in d2.keys():
        if i==j:
            d3.update({i:d1[i]+d2[i]})
            break
        else:
            if i not in d3:
                d3.update({i:d1[i]})
            if j not in d3:
                d3.update({j:d2[j]})
        
print(d3)