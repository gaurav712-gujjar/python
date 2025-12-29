                    #____CONSTRUCTOR____#

class HouseDesign:
    def __init__(self,x): #Constructor( __init__ function )
        #self is a local variable
        #print("Call Builder :",self)
        #self and the object(h1) are the same memory address
        #h1.color = "red"
        self.color = x  #instance variable


#HouseDesign()   To call constructor
h1= HouseDesign("pink")
print("Color h1 :",h1.color)


h2=HouseDesign("green")
print("Color h2 :",h2.color)