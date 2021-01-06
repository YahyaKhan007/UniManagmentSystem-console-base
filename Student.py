from Person import Person
class Student(Person):
    
    def __init__(self, p_name= '', p_cnic= '1234567890987', p_id= 1, cgpa= 1, fee= 0):
        
        super(Student, self).__init__(p_name, p_cnic, p_id)
        self.CGPA = cgpa
        self.Fee = fee
                     
    @property
    def CGPA(self):
        return self.__cgpa
    
    @CGPA.setter
    def CGPA(self, gpa):
        if gpa > 4.0 or gpa < 0:
            raise AttributeError("Invalid CGPA!")
        else:
            self.__cgpa = gpa
            
    @property
    def Fee(self):
        return self.__fee
    
    @Fee.setter
    def Fee(self, fee):
        if fee < 0:
            raise AttributeError("InValid Fee")
        else:
            self.__fee = fee
            