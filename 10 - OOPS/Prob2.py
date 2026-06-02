'''
1. Student Class - Create a class Student with:

Attributes:
name
roll_no
marks

Method:
display_info()

Expected Output:
Name: Sam
Roll No: 101
Marks: 85
'''

class student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno= rollno
        self.marks= marks
    
    def data(self):
        print(f'Name: {self.name} \nRoll no. {self.rollno} \nMarks: {self.marks} \n')

Saaiem = student('Saaiem', 221846, 99)
Tanishka = student('Tanishka', 421780, 95)
Rushmen = student('Sam', 473829, 90)

Saaiem.data()
Tanishka.data()
Rushmen.data()