s1=int(input("Enter marks of the subject EDE: "))
s2=int(input("Enter marks of the subject ETI: "))
s3=int(input("Enter marks of the subject PWP: "))
s4=int(input("Enter marks of the subject MAD: "))
s5=int(input("Enter marks of the subject MGT: "))
avg=(s1+s2+s3+s4+s5)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80) & (avg<90):
    print("Grade: B")
elif(avg>=70) & (avg<80):
    print("Grade: C")
elif(avg>=60) & (avg<70):
    print("Grade: D")
else:
    print("Grade: F")