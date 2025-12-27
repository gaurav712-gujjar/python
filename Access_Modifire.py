class A:
    var=10
    _var2=20    #protected

class B:
    def info(self):
        print("b value :",A._var2)


a1=B()
#a1.info()

class Company:
    __salary=5000       #private  __salary => _Company__salary
    def info(self):
        print("variable access :",self.__salary)


c1=Company()
#print(c1.info())
#c1.info()

