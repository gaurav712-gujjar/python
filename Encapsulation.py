                         #-----PYTHON ENCAPSULATION------#

"""Encapsulation means combine the variable and method,
inside the class to provide data accessibility and security"""

#Encapsulation = Data Hiding + Controlled Access

class A:
    _a=10   #Protected
    __b=20  #Private

    def show(self):
        print("a=",self._a,"b=",self.__b)


obj=A()
obj.show()
#print(obj._a)      #Access outside by the help of class object
#print(obj.__b)     #Do not access outside
#print(obj._A__b)   #But with the help of this we access it