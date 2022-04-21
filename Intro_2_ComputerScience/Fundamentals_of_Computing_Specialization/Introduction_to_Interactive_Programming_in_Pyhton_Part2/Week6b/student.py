# Implementation of Student class

# definition of Person class
class Person:
    
    def __init__(self, first, last, year):
        self.first_name = first
        self.last_name = last
        self.birth_year = year
        
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def age(self, current_year):
        return current_year - self.birth_year
    
    def __str__(self):
        return "The person's name is " + self.full_name() + ". Their birth year is " + str(self.birth_year)


#################################################
# Student adds code where appropriate

# definition of Student class
class Student:
    
    # the person parameter must be a Person object
    def __init__(self, person, pwd):
        self.person = person
        self.password = pwd
        self.projects = []
    
    # use the full_name method for Person    
    def get_name(self):
        return self.person.full_name()
    
    def check_password(self, pwd):
        return self.password == pwd
    
    def get_projects(self):
        return self.projects
    
    def add_project(self, project):
        self.projects.append(project)
        
 
    
###################################################
# Testing code

joe_person = Person("Joe", "Warren", 52)
joe_student = Student(joe_person, "TopSecret")

print joe_student.get_name()
print joe_student.check_password("qwert")
print joe_student.check_password("TopSecret")

print joe_student.get_projects()
joe_student.add_project("Create practice exercises")
print joe_student.get_projects()
joe_student.add_project("Implement Minecraft")
print joe_student.get_projects()


####################################################
# Output of testing code 

#Joe Warren
#False
#True
#[]
#['Create practice exercises']
#['Create practice exercises', 'Implement Minecraft']


