def Count(St):

    uc=0
    lc=0
    for i in St:
        if i.islower():
            lc+=1
        elif i.isupper():
            uc+=1
    return (uc,lc)
St=input("Enter String: ")
if St.isalpha:
    uc,lc=Count(St)
    print("No of Upper Case :",uc)
    print("No of Lower Case :",lc)


