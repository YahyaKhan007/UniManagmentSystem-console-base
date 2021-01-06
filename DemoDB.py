from Batch import Batch
from Student import Student

class DemoDB:
    
    def __init__(self):
        self.__batches = []

    def Existing_Records(self):
        batch = Batch()
        #    Batch
        batch.batch_id = 12
        batch.batch_name = '2020'
        #     Course
        batch.course.course_credit = 3
        batch.course.course_id = 112
        batch.course.course_name = 'AI'
        #     Teacher
        batch.teacher.p_name = 'Rizwan'
        batch.teacher.p_id = 122
        batch.teacher.Salary = 100000
        #      Student
        stud = Student()
        stud.p_name = 'Yahya'
        stud.p_cnic = '1730118001871'
        stud.p_id = 9487
        stud.fullAddress.Country = 'Pakistan'
        stud.fullAddress.City = 'Peshawar'
        stud.Fee = 38000
        stud.CGPA = 3.58

        batch.students.append(stud)

        self.__batches.append(batch)

    def display_Records(self):
        result = ''
        for obj in self.__batches:
            result += f'\t\t\t\t\t\t _________________________\n'
            result += f'\t\t\t\t\t\t|***  Batch  --->  {obj.batch_id} ***|\n'
            result += f'\t\t\t\t\t\t|_________________________|\n'
            result += f'\t\t\t\t Batch ID -->  {obj.batch_id}\n'
            result += f'\t\t\t\t Batch Name --> {obj.batch_name}\n'

            result += f'\t\t\t\t\t\t*** Course  ***\n'
            result += f'\t\t\t\t\t\t---------------\n'
            result += f'\t\t\t\t Course Name -->  {obj.course.course_name}\n'
            result += f'\t\t\t\t Course ID  --> {obj.course.course_id}\n'
            result += f'\t\t\t\t Course Credit Hours{obj.course.course_credit}'

            result += f'\n\t\t\t\t\t\t*** Teacher  ***\n'
            result += f'\t\t\t\t\t\t----------------\n'
            result += f'\t\t\t\t Teacher Name  -->  {obj.teacher.p_name}\n'
            result += f'\t\t\t\t Teacher ID  -->  {obj.teacher.p_id}\n'
            result += f'\t\t\t\t Teacher Salary  -->  {obj.teacher.Salary}\n'
            result += f'\t\t\t\t Teacher CNIC  --->  '
            for i in range(len(obj.teacher.p_cnic)):
                        if i == 5 or i == 12:
                            result += '-'
                            result += obj.teacher.p_cnic[i]
                        else:
                            result += obj.teacher.p_cnic[i]
            result += '\n'
            

            for stud in obj.students:
                result += f'\n\t\t\t\t\t\t*** Students  ***\n'
                result += f'\t\t\t\t\t\t-----------------\n'
                result += f'\t\t\t\t Student Name -->  {stud.p_name}\n'
                result += f'\t\t\t\t Student Id   -->  {stud.p_id}\n'
                result += f'\t\t\t\t Student CNIC -->  '
                for i in range(len(stud.p_cnic)):
                        if i == 5 or i == 12:
                            result += '-'
                            result += stud.p_cnic[i]
                        else:
                            result += stud.p_cnic[i]
                result += '\n'
                result += f'\t\t\t\t Student Adress   ---> { stud.fullAddress.City}\n'
                result += f'\t\t\t\t Student CGPA -->  {stud.CGPA}\n'
                result += f'\t\t\t\t Student Fee  -->  {stud.Fee}\n\n'

                result += f'\t\t\t\t'
                result += f'_*_*_*_*_*'*7
                result += f'\n'

        return result


    def add_New_Batch(self, obj):

        self.__batches.append(obj)
        return "\t\t\t\t\t****Batch Added****"

#       S E A R C H    S T U D E N T 
    
    def search_student(self, name):
        result = ''
        find  = False
        for obj in self.__batches:
            for stud in obj.students:
                if name == stud.p_name:
                    find = True
                    result += f'\t\t\t\t\t\t _________________________\n'
                    result += f'\t\t\t\t\t\t|***  Batch  --->  {obj.batch_id}  ***|\n'
                    result += f'\t\t\t\t\t\t|_________________________|\n'
                    result += f'\n\t\t\t\t\t\t*** Students Found  ***\n'
                    result += f'\t\t\t\t\t\t----------------------\n'
                    result += f'\t\t\t\t Student Name -->  {stud.p_name}\n'
                    result += f'\t\t\t\t Student Id   -->  {stud.p_id}\n'
                    result += f'\t\t\t\t Student CNIC -->  '
                    for i in range(len(stud.p_cnic)):
                        if i == 5 or i == 12:
                            result += '-'
                            result += stud.p_cnic[i]
                        else:
                            result += stud.p_cnic[i]
                    result += '\n'
                    result += f'\t\t\t\t Student Adress   ---> { stud.fullAddress.City}\n'
                    result += f'\t\t\t\t Student CGPA -->  {stud.CGPA}\n'
                    result += f'\t\t\t\t Student Fee  -->  {stud.Fee}\n\n'

                    result += f'\t\t\t\t'
                    result += f'_*_*_*_*_*'*7
                    result += f'\n'

        return (result, find)


    # def update_Record(self, b_name):
    #     find = False
    #     for loc in range(len(self.__batches)):
    #         if b_name == self.__batches[loc].batch_name:
    #             find = True
    #     return (self.__batches, find, loc)

    # def update(self, lst):
    #     self.__batches = lst

    #     return "Record Updated"
   