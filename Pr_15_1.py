class Employee:
    __name = ""
    __department = ""
    __salary = 0
    def setData(self,name, department, salary):
        self.__name = name
        self.__department = department
        self.__salary = salary
    def showData(self):
        print("Name      :", self.__name)
        print("Department:", self.__department)
        print("Salary    :", self.__salary)
def main():
    emp = Employee()
    emp.setData('Atharva', 'Computer', 100000)
    emp.showData()
if __name__ == "__main__":
    main()