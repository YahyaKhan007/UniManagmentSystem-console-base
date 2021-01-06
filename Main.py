from DemoDB import DemoDB
from Batch import Batch
from Student import Student

if __name__=='__main__':

    __db = DemoDB()
    __db.Existing_Records()
  
    while True:
        print('\t\t1 --> Add new Batch\n\t\t2 --> All Records\n\t\t3 --> Existing Records'
        '\n\t\t4 --> Search Student\n\t\t5 --> Modify Student Record in Existing Batch\n\t\t6 --> Exit', end='    ')
        ch = input()
        if ch == '1':
            batch = Batch()
            #       Batch  Info
            while True:
                try:
                    batch.batch_id = int(input('Enter Batch ID -  '))
                except ValueError as err:
                    print(err,'\nTry Again')
                except AttributeError as err:
                        print(err, '\nTry Again')
                else:
                    break

            while True:
                try:        
                    batch.batch_name = input('Batch Number -  ')
                except AttributeError as err:
                    print(err, '\nTry again')
                else:
                    break

                                            #       Course Info
            while True:
                try:
                    batch.course.course_name = input('Enter Course Name -  ')
                except AttributeError as err:
                    print(err, '\nTry Again') 
                else:
                    break
            while True:
                try:
                    batch.course.course_credit = int(input("Enter Credit Hours for Course -  "))
                except ValueError as err:
                    print('\nTry Again')
                except AttributeError as err:
                    print(err, '\nTry Again')
                else: 
                    break

            while True:    
                try:
                    batch.course.course_id = int(input('Enter Course Id - '))
                except ValueError as err:
                    print('\nTry Again')
                except AttributeError as err:
                    print(err, '\nTry again')
                else:
                    break

                    #       Teacher Info
            while True:
                try:
                    batch.teacher.p_name= input('Enter Teacher Name -  ')
                except AttributeError as err:
                    print(err, '\nTry again')
                else:
                    break

            while True:
                try:
                    batch.teacher.p_cnic = input('Enter teacher CNIC =  ')
                except AttributeError as err:
                    print(err, '\nTry again')
                else:
                    break
            
            while True:
                try:
                    batch.teacher.p_id = int(input('Enter Teacher Id -  '))
                except ValueError as err:
                    print('\nTry Again')
                except AttributeError as err:
                    print(err, '\nTry again')
                else:
                    break
            while True:
                try:
                    batch.teacher.Salary = int(input("Enter salary -  "))
                except ValueError as err:
                    print('\nTry Again')
                except AttributeError as err:
                    print(err, '\nTry again')
                else:
                    break           
            #       Student Info
            student = Student()
            while True:
                try:
                    student.p_name = input("Enter Student name -  ")
                except AttributeError as err:
                    print(err, '\nTry again')
                else:
                    break

            while True:
                try:
                    student.p_cnic = input('Entre Student CNIC -  ')
                except AttributeError as err:
                    print(err, '\nTry again')
                else:
                    break

            while True:
                try:
                    student.fullAddress.City = input("Enter Birth City -  ")
                except AttributeError as err:
                    print(err, '\nTry again')
                else:
                    break
            
            while True:
                try:
                    student.p_id = int(input('Enter Student  Id -  '))
                except ValueError as err:
                    print('\nTry Again')
                except AttributeError as err:
                    print(err, '\nTry again')
                else:
                    break
            while True:
                try:
                    student.CGPA = float(input('Enter CGPA -  '))
                except ValueError as err:
                    print('\nTry Again')
                except AttributeError as err:
                    print(err, '\nTry again')
                else:
                    break
            
            while True:
                try:
                    student.Fee = int(input('Enter Fee -  '))
                except ValueError as err:
                    print('\nTry Again')
                except AttributeError as err:
                    print(err, '\nTry again')
                else:
                    break

            batch.students.append(student)

            print(__db.add_New_Batch(batch))

        elif ch == '2':
                result = __db.display_Records()
                print(result)

        elif ch == '3':
            result = __db.display_Records()
            print(result)

        elif ch == '4':
            result = __db.search_student(input('Enter Name of the Student -  '))
            if not result[1]:
                print('\n\t\t\t\tNo one Found !')
                print('\t\t\t\t--------------')
            else:
                print(result[0])


        elif ch == '5':
            batches, find, loc = __db.update_Record(input('Enter Batch Name -  '))
            if find:
                while True:
                    ch = input("Modify Student Record -  ")
                    if ch.startswith('y') or ch.startswith("Y"):
                        batches[loc].students[0].p_name = input("Enter updated Name -  ")
                        batches[loc].students[0].p_id = int(input("Enter updated ID -  "))
                        batches[loc].students[0].p_cnic = input("Enter updated CNIC -  ")
                        batches[loc].students[0].Fee = int(input("Enter updated Fee -  "))
                        batches[loc].students[0].fullAddress.City = input("Enter updated City -  ")
                        batches[loc].students[0].CGPA = float(input("Enter updated GPA -  "))

                        print(__db.update(batches))
                    break

        elif ch == '6':
            break

    
