from abc import ABC, abstractmethod
from Address import Address
class Person(ABC):
    
    def __init__(self, p_name= '', p_cnic= '', p_id= 1):  

        self.__cnic = None
        self.p_name = p_name
        self.p_cnic = p_cnic
        self.p_id = p_id      
        self.fullAddress = Address()

    @property
    def p_name(self):
        return self.__name 
    @p_name.setter
    def p_name(self, name):
        for ch in name:
            if ch.isspace():
                continue
            elif not ch.isalpha():
                raise AttributeError("InValid Value")
                break
        else:
            self.__name = name    
    
    @property
    def p_cnic(self):
        return self.__cnic   
    @p_cnic.setter
    def p_cnic(self, cnic):
        if len(cnic) == 13:
            self.__cnic = cnic
        else:
            raise AttributeError('length must be 13')
                
    @property            
    def p_id(self):
        return self.__id
    @p_id.setter
    def p_id(self, Id):
        if Id < 0:
            raise AttributeError("Id smaller than 0")
        else:
            self.__id = Id