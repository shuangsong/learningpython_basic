#module

#import useful_tools

#print(useful_tools.rool_dice(10))

#we can import useful modules from external resources:
# google: list of python modules you can see a lot of modules that have been create for use.
'''
so where is the module stored?? all these external modules:
at right side of your pycharm software, open external libraries,
click python 3.7 then below Lib is the place where store those
modules.
you can google : python docx  have some installation instruction

open terminal to install

pip -- version

#pip install python module name
pip install python-docx
go to lib -site packages then you will find module you have installed

remove it
pip uninstall python module name
'''

#Class and object
class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
#so the class is the preview of what class of the student
#and the object is the actual, not template anymore.
#then create a new python file and
from Student import Student
student1 = Student("Jim", "business", 3.4, False)
print(student1.gpa)

