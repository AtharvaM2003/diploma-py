class Values:
    def display(self,i=0,c='c'):
        print("Values Are: ",i,c)
    def display(self,c='c',i=0):
        print("Values Are: ",c,i)
obj=Values()

obj.display('avm',45)
obj.display(75,'avm')