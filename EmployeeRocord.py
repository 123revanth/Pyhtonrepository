from unicodedata import name
from xml.dom.minidom import CharacterData


class Person(object):
    def __init__(self, name, idnumber, salary, post):
        self.name = name
        self.idnumber = idnumber
        self.salary = salary
        self.post = post

    def display(self):
        print("Name: {}".format(self.name))
        print("idnumber: {}".format(self.idnumber))
        print("Salary: {}".format(self.salary))
        print("post: {}".format(self.post))

a = Person("Rishi", 880345, 1000, "Floor cleaner")
b = Person("Revanth Jallipalli", 100002, 1300000000, "cheif technical officer")

a.display()
print("________________________________-")
b.display()




    
 
