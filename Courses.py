class Course:
    
    def __init__(self, course_name= '', course_id= 1, course_credit= 1):

        self.course_name = course_name
        self.course_id = course_id
        self.course_credit = course_credit
        
    @property
    def course_name(self):
        return self.__name   
   
    @course_name.setter
    def course_name(self, name):
        for ch in name:
            if ch.isspace():
                continue
            elif not ch.isalpha():
                raise AttributeError("InValid Name")
                break
        else:
            self.__name = name
    
    @property
    def course_credit(self):
        return self.__credit
    
    @course_credit.setter
    def course_credit(self, credit):
        if credit < 0 or credit > 4:
            raise AttributeError("InValid Credit hour")
        else:
            self.__credit = credit
                    
    @property            
    def course_id(self):
        return self.__id
    @course_id.setter
    def course_id(self, id_num):
        if id_num < 0:
            raise AttributeError("InValid id")
        else:
            self.__id = id_num