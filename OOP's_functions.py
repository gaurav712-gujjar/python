class A:
    def func(self): #Instance_Method
        print("Calling First Instance Method")

    @staticmethod
    def func2():  #Static_Method
        print("Calling func2 Which will be Static_method")

    @classmethod
    def func3(cls): #Class_Method
        print("Calling func3 Which will be class_method :", cls)


#static use if we do'nt want to create memory address for the object
#cls reference class
a1=A()
a1.func()
a1.func2()  #object access static
A.func2()   #class also access it
A.func3()   #class_method