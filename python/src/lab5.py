class Person:
    def __init__(self, name, age, gender):
        self._name = name    
        self.set_age(age)  
        self._age
        self._gender = gender
    
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def get_gender(self):
        return self._gender
    
    def set_age(self, age):
        if age > 0 and age < 122:
            self._age = age
        else:
            raise Exception("age is higher or lower than bound")
        
    def know_gender(self):
        return(self._name + "'s gender - " + self._gender)
	    
    def go_to_walk(self, time):
        if time <= 12 and time >= 0:
            return("At " + str(time) + " o'clock " + self._name + " goes for a walk.")
        else:
            raise Exception("time can't be more than 12 or less than 0")