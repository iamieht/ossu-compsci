# Use of Person class

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
    
# implementation of average_age
def average_age(person_list, current_year):
    average_age = 0.0
    for person in person_list:
        average_age += person.age(current_year)
        
    return average_age / len(person_list)
    


###################################################
# Testing code

joe = Person("Joe", "Warren", 1961)
john = Person("John", "Greiner", 1966)
stephen = Person("Stephen", "Wong", 1960)
scott = Person("Scott", "Rixner", 1987)  

instructors = [joe, john, stephen, scott]
print average_age(instructors, 2013)

instructors.pop() # get rid of Scott and his bogus age
print average_age(instructors, 2013)


####################################################
# Output of testing code 

#44.5
#50.6666666667