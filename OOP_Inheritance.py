                #__Inheritance__#

class TataMotors:
    no_vechile=2000
    revenue=("400 cr")

    def info(self):
        print("vehicle are :",self.no_vechile,self.revenue)

class TataHarrier(TataMotors):
    price="25 lakh"

    def info_harrier(self):
        print("this is harrier information")
        """by the help of this function it call the parent method/function
        and access it"""
        super().info()



t1 = TataHarrier()
t1.info_harrier()
