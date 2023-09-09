bit=int(input("Enter Bits: "))
mb= bit/(8*1024*1024)
gb=bit/(8*1024*1024*1024)
tb=bit/(8*1024*1024*1024*1024)


print("MegaByte= {:.4f}".format(mb))
print("\nGegaByte= {:.5f}".format(gb))
print("\nTeraByte= {:.7f}".format(tb))
