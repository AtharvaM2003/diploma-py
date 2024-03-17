def fun():
    St='Jaihind Polytechnic Kuran'
    uc=0
    lc=0
    for i in St:
        if i.islower():
            lc+=1
        elif i.isupper():
            uc+=1
    print("No of Upper Case :",uc)
    print("No of Lower Case :",lc)

fun()
