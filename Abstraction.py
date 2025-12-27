'''Abstraction means hiding the complex implementation details
and showing only the essential features to the user.
-------------------------------------------
Why do we need Abstraction?
• To reduce complexity
• To increase security
• To make code clean and easy to use
• To hide internal logic from the user
-------------------------------------------
Abstract Class (Simple Definition)
An abstract class is a class that cannot be instantiated (you cannot create its object).
It is used to provide a template or blueprint for other classes.'''

'''Abstract Method (Simple Definition)
An abstract method is a method that has a definition (name) but no body.
The child class must override this method.'''

from abc import ABC, abstractmethod

#RBI_loan-->abstract class
class RBI_loan(ABC):
    amount = 5000

    @abstractmethod #(Decorator)
    def interest(self): #Abstract method
        pass

#h1 = RBI_loan()     #Can't create object of abstract class

class HDFC_loan(RBI_loan):
    tenure = 10

    #without implement function(abstractmethod) of parent class child not show any data
    #it is compulsory to implement in child class
    def interest(self):
        print("HDFC have 8% interest")

h1=HDFC_loan()
h1.interest()
