from Courses import Course
from Student import Student
from Teacher import Teacher

class Batch():
    
    def __init__(self, batch_id= 1, batch_name= None):
        
        self.batch_name = batch_name
        self.batch_id = batch_id 
        self.course = Course()
        self.teacher = Teacher()

        self.students = []
        
    @property            
    def batch_id(self):
        return self.__batch_id
    @batch_id.setter
    def batch_id(self, id_num):
        if type(id_num) == int:
            if id_num < 0:
                raise AttributeError("InValid batch id")
            else:
                self.__batch_id = id_num
        else:
            raise TypeError('InValid type')  
    @property
    def batch_name(self):
        return self.__batch_name   
    @batch_name.setter
    def batch_name(self, name):
        self.__batch_name = name
    