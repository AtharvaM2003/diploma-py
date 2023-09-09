sd= [{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VII":"S007"}]
s=set()

for i in sd:
    for k,v in i.items():
        s.add(v)
print(s)