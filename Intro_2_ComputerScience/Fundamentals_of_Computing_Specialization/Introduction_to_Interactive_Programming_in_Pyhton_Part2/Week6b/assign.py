# Use of the Student class

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
        
        
#################################################
# Student adds code where appropriate
        
# definition of function assign
def assign(students, name, pwd, project):
    for student in students:
        if student.get_name() == name and student.check_password(pwd):
            if project not in student.get_projects():
                student.add_project(project)
        

    
 
    
###################################################
# Testing code

# create some Student objects using Person object
joe = Student(Person("Joe", "Warren", 52), "TopSecret")
joe.add_project("Create practice exercises")
joe.add_project("Implement Minecraft")

scott = Student(Person("Scott", "Rixner", 29), "CodeSkulptor")
scott.add_project("Beat Joe at RiceRocks")

john = Student(Person("John", "Greiner", 47), "outdoors")


# create a list of students
profs = [joe, scott, john]

# test assign
print joe.get_projects()
assign(profs, "Joe Warren", "TopSecret", "Practice RiceRocks")
print joe.get_projects()

print john.get_projects()
assign(profs, "John Greiner", "OUTDOORS", "Work on reflexes")
print john.get_projects()
assign(profs, "John Greiner", "outdoors", "Work on reflexes")
print john.get_projects()



####################################################
# Output of testing code 

#['Create practice exercises', 'Implement Minecraft']
#['Create practice exercises', 'Implement Minecraft', 'Practice RiceRocks']
#[]
#[]
#['Work on reflexes']

