"""
TASK 1

Design a parent class called CFGStudent.

It should have general attributes like name, surname, age, email, student id
and methods to fetch student’s full name and student’s id.

Design a child class called NanoStudent, which  inherits from CFGStudent class.
This class should have exactly the same attributes as its parent class,
as well as an additional one called ‘specialization’ and course grades.

The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
in front of the id.

New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
You can use  it as a skeleton code for your classes OR adjust it and create your own.

SEE NOTES BELOW

"""
import random
class CFGStudent:

    def __init__(self, name, surname, age, email):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = self.generate_id()

    @staticmethod
    def generate_id():
        student_id = str(random.randint(1000, 10000))
        return student_id
        'create a random new id, which is any number between 1,000 and 10,000'
        'return id as a string'
        "Example '8754' "

    def get_id(self):
        return self.student_id
        'fetch student id'

    def get_fullname(self):
        full_name = self.name + " " + self.surname
        return full_name
        'your code goes here'


class NanoStudent(CFGStudent):

    def __init__(self, specialization, name, surname, age,email):
        super().__init__(name, surname, age, email)
        self.specialization = specialization
        self.course_grades = dict()

    @staticmethod
    def generate_id():
        student_id = 'NANO' + str(random.randint(1000, 10000))
        return student_id
        'create a random new id, which is a word NANO followed by any number between 1,000 and 10,000'
        'return id as a string'
        "Example 'NANO1234' "

    def add_new_grade(self, subject, grade):
        self.course_grades[subject] = grade
        'update course_grades container'
        "Example: pass in a task name and its grade, so that both are added to course_grades"

    def get_course_grades(self):
        return self.course_grades
        'fetch course grades container and its values'



############################################

# Example run

s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
print(s.get_fullname())
# returns 'Anna Smith'
print(s.student_id)
# returns '3868' or some other random number

cfg_s = NanoStudent('Software', name='Mia', surname='Papandopulu', age=20, email='mia@mail.com')
print(cfg_s.get_fullname())
# returns 'Mia Papandopulu'
print(cfg_s.get_id())
# returns 'NANO6180' or some other random number

cfg_s.add_new_grade('theory', 95)
cfg_s.add_new_grade('project', 78)
print(cfg_s.get_course_grades())
# returns {'theory': 95, 'project': 78}



"""
TASK 2

Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence 
and return the sum of all even Fibonacci numbers. See more details in the task description in 
your assessment paper. 
"""
def fibbonaci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibbonaci(n - 1) + fibbonaci(n - 2)

def even_fibonacci_sum(limit):
    limit = limit
    fib = fibbonaci(n=limit)
    if fib and limit:
        list_of_even = [fibbonaci(n) for n in range(limit) if fibbonaci(n) % 2 == 0]
        even_sum = sum(list_of_even)
    return even_sum

##### TESTS ####

print(even_fibonacci_sum(limit=10))  # should be 44
print(even_fibonacci_sum(limit=15))  # should be 188
print(even_fibonacci_sum(limit=1))   # should be 0





"""
TASK 3

Validate subsequence. Use suggested tests below to check
correctness of your solution. 
"""

def is_valid_subsequence(array, sequence):
    array_idx = 0
    sequence_idx = 0

    while array_idx < len(array) and sequence_idx < len(sequence):
        if array[array_idx] == sequence[sequence_idx]:
            sequence_idx += 1
        array_idx += 1

    if sequence_idx == len(sequence):
        return True
    else:
        return False

#### TESTS ####

array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]

print(is_valid_subsequence(array1, sequence1))  # FALSE


array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]

print(is_valid_subsequence(array2, sequence2))  # TRUE


array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]

print(is_valid_subsequence(array3, sequence3))  # TRUE



"""
TASK 4

WRITTEN ASSIGNMENT

Write a review on how 'class Employee' can be improved.
(See PDF document with the code example)
"""

"""
1) In the __init__ method, the object attributes should be named the same. For example, self.active_status = active_status
and self.id = id. 
2) The Employee class goes against the Single Responsibility Principle. This principle states that a class should do one job.
This Employee class is doing more than one job. The print_employee_report method is writing the information into a file. This 
should be a separate class or subclass as it is doing a different job. The save_employee and delete employee also go against 
the single responsibility principle. They have more than one responsibility in the method. To improve this, it can be divided 
into smaller methods or create a new class dedicated to saving/deleting.
3) The Employee class also goes against the Open-closed principle. If we were to pass another attribute in this class, for example
location and wanted to print this, we would have to modify the class instead of adding onto it. The open-closed principle 
allows us to extend the code instead of modifying the existing class. 
4) Exception handling can be used to catch errors in the code that could possibly crash the program.
6) The remove employee only deletes the id and name instead of all the attributes. The database will not be consistent 
therefore it's best if all the attributes were deleted.
7) 















"""






