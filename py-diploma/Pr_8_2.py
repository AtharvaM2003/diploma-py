
s1={10,20,40,60,50}
s2={10,30,50,80,70}

print("Both Set intersection=",s2.intersection(s1))
print("Both Set union=",s2.union(s1))
print("Both Set diffrence=",s2.difference(s1))
print("Both Set symmetric difference=",s2.symmetric_difference(s1))
s1.clear()
print("After set clear:",s1)