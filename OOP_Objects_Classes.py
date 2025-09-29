class Student:

    student_count = 0   

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.student_count += 1  


s1 = Student("meshari", 16)
s2 = Student("reda", 15)
s3 = Student("fares", 17)

print(Student.student_count)
