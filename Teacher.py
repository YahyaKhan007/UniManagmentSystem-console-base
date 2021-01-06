from Person import Person

class Teacher(Person):
    
    def __init__(self, p_name= '', p_cnic= '1234567890987', p_id= 1, salary= 0):
        super(Teacher, self).__init__(p_name, p_cnic, p_id)
        self.Salary = salary

    @property            
    def Salary(self):
        return self.__salary
    
    @Salary.setter
    def Salary(self, salary):
        self.__salary = salary