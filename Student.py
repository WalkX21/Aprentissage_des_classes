class Student:
    def __init__(self, name, grade):
        self.name =name 
        self.grade = grade 
        self.course = "-"

    def print_info(self):
        print('Student : ' + str(self.name))
        print("average grade: " + self.grade)
        print("attending elective course: " + self.course)



    def elective_course(self):
        course = input('Enter the course :')
        self.course = course



student = Student('Darius', '4.8')
student.print_info()
student.elective_course()
student.print_info()
