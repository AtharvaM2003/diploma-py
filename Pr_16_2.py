
class Password(Exception):
    pass
try:
    i_num =input("Enter a password: ")
    psw = 'Snehaja'
    if i_num !=psw:
        raise Password
except Password:
    print("Password is not Correct,Try again!")
else:
    print("Password is Correct!")