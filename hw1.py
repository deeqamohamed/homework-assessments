"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.
"""

class CashRegister(object) :

    def __init__(self) :
        self.total_items = {'sweet potatoes': '1.20'}, \
                            {'oatmeal': '0.90'}, \
                            {'mango': '1.10'}
        self.total_price = 0
        self.item_count = 0

    def add_item(self, item, price):
        item = self.total_items.append()
        return item

    def apply_discount(self, price):
        discount = input('Do you have a voucher?')
        if discount == 'y':
            price = price * 0.8
        else:
            price = price

    def remove_item(self,price):
        self.total_price.pop(price)
        self.item_count -= 1

    def get_total(self):
        return self.total_price

    def show_items(self):
        return self.total_items

    def reset_register(self):
        self.total_price = 0
        self.items = 0


c1=CashRegister()
c1.add_item(item='grapes',price=1.10)

# # EXAMPLE code run:
#
# # ADD



"""
#
TASK 2

Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student.

"""

class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = {'Sociology': 80, 'French': 65, 'Chemistry':78}

class CFGStudent(Student):
    # create new methods that manage student's subects (add/remove new subject and its graade to the dict)
    def add_subject(self, subject, mark):
        self.subjects[subject] = mark

    def remove_subject(self, subject):
        self.subjects.pop(subject)
    # create a method to view all subjects taken by a student
    def view_subjects(self):
        print(self.subjects.keys())
    # create a method  (and a new variable) to get student's overall mark (use average)
    def view_mark(self):
        average_mark = float(sum(self.subjects.values())) / len(self.subjects)
        print (average_mark)


c1= CFGStudent('deeqa', 23, 123)
c1.add_subject('Art', 75)
c1.remove_subject('Sociology')
c1.view_subjects()
c1.view_mark()