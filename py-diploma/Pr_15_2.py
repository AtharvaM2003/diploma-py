class Student:
    def __init__(self):
        self.name = input("Enter your name:")
        self.cname = input("Enter your college name:")
        self.roll = int(input("Enter your roll number:"))
class Test(Student):
    def display(self):
        print("============ Student info is ==========")
        print("Name is : ", self.name)
        print("College Name is:", self.cname)
        print("Roll number is:", self.roll)
obj = Test()
obj.display()