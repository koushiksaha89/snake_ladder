from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self,
                 first_name, 
                 last_name, 
                 age,
                 address,
                 mobile_number):
        
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.mobile_number = mobile_number
