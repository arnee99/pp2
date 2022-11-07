# A Python program to demonstrate inheritance
 
class Person(object):
   
  # Constructor
  def __init__(self, name, id):
    self.name = name
    self.id = id
 
  # To check if this person is an employee
  def Display(self):
    print(self.name, self.id)
 
 
# Driver code
emp = Person("Satyam", 102) # An Object of Person
emp.Display()

class Emp(Person):
   
  def Print(self):
    print("Emp class called")
     
Emp_details = Emp("Mayank", 103)
 
# calling parent class function
Emp_details.Display()
 
# Calling child class function
Emp_details.Print()