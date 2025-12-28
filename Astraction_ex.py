from abc import ABC,abstractmethod

class System_Shutdown(ABC):
    @abstractmethod
    def Systen_Off(self):
        pass

class Light(System_Shutdown):
    def Systen_Off(self):
        print("Light OFF")

    def Fan_On(self ):
        print("Fan ON")

e1=Light()
e1.Fan_On()
e1.Systen_Off()