class Fox:
    def __init__(self, name, age, gender):
        self._name = name
        self._gender = gender
        self.set_age(age) 
        self._age = age 

    def get_name(self):
        return self._name

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def set_age(self, age):
        if age >= 0 and age <=33:
            self._age = age 
        else:
            raise Exception('Foxes do not live that long')
    
    def displayfox(self):
        print("Name:", self._name, "\n"
                "Age:", self._age, "\n"
                "Gender:", self._gender, "\n"
                """
                  ████                                        ████                
                ▓▓▓▓▓▓▓▓                                    ▓▓▓▓▓▓██              
              ██▓▓▓▓▓▓▓▓██                                ██▓▓▓▓▓▓▓▓██            
            ██▓▓▓▓▓▓▓▓▓▓██                                ██▓▓▓▓▓▓▓▓▓▓██          
            ██▓▓▓▓▓▓▓▓▓▓██                                ██▓▓▓▓▓▓▓▓▓▓██          
          ██▓▓▓▓▓▓  ▓▓▓▓▓▓██                            ██▓▓▓▓▓▓░░▓▓▓▓▓▓██        
          ██▓▓▓▓▒▒  ▒▒▓▓▓▓██                            ██▓▓▓▓▒▒  ▒▒▓▓▓▓██        
          ██▓▓▓▓░░    ▓▓▓▓██                            ██▓▓██      ▓▓▓▓██        
          ██▓▓▓▓░░    ▓▓▓▓██                            ██▓▓██      ▓▓▓▓██        
        ██▓▓▓▓▓▓░░    ▓▓▓▓▓▓██                        ██▓▓▓▓██      ▓▓▓▓▓▓██      
        ██▓▓▓▓░░░░    ░░▓▓▓▓██                        ██▓▓▓▓        ░░▓▓▓▓██      
        ██▓▓▓▓░░░░    ░░▓▓▓▓▓▓██                    ██▓▓▓▓▓▓░░    ░░░░▓▓▓▓██      
        ██▓▓▓▓░░░░  ░░  ▓▓▓▓▓▓████████████████████████▓▓▓▓▓▓░░░░  ░░░░▓▓▓▓██      
        ██▒▒▒▒░░░░░░  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒██▒▒▒▒▒▒▒▒░░▒▒░░░░▒▒▒▒██      
        ██▒▒▒▒░░▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░▒▒▒▒██      
        ██▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒  ░░▒▒▒▒██      
    ██████▒▒▒▒  ▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░▒▒▒▒██████  
    ██░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ██  
    ██  ░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░  ██  
    ██  ▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒  ██  
      ██  ▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒  ██    
      ██  ▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒  ██    
  ████░░██░░▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒  ██  ████
  ██░░██░░  ▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒  ░░██  ██
  ██  ░░██  ▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒  ██    ██
  ██        ▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒        ██
    ██      ▒▒▒▒▒▒▒▒░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░▒▒▒▒▒▒▒▒      ██  
      ██      ▒▒▒▒▒▒▒▒░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░▒▒▒▒▒▒▒▒░░    ██    
        ██░░    ▒▒▒▒▒▒▒▒██████░░░░░░░░░░░░░░░░░░░░░░░░██████▒▒▒▒▒▒▒▒      ██      
    ██████████    ▒▒▒▒▒▒▒▒████░░░░░░░░░░░░░░░░░░░░░░░░████▒▒▒▒▒▒▒▒░░  ██████████  
  ██    ░░    ██  ▒▒▒▒▒▒▒▒▒▒████░░░░░░░░░░░░░░░░░░░░████▒▒▒▒▒▒▒▒▒▒  ██        ░░██
    ██        ░░    ▒▒▒▒▒▒▒▒▒▒██▒▒▒▒░░░░░░░░░░░░▒▒▒▒██▒▒▒▒▒▒▒▒▒▒    ░░      ░░██  
      ██████        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒        ██████    
          ████      ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒        ▓▓██        
            ████████    ▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒    ████████          
                    ████░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░████                  
                        ██  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ██                      
                          ██  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ██                        
                            ██  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░██                          
                              ██░░▒▒▒▒▓▓▒▒▒▒▓▓▒▒▒▒  ██                            
                              ██  ▒▒▒▒▓▓▒▒▓▓▓▓▒▒▒▒  ██                            
                                ██░░▒▒▓▓▓▓▓▓▓▓▒▒░░██                              
                                ██    ████████    ██                              
                                  ▓▓  ████████  ██                                
                                  ▒▒▒▒▒▒░░▒▒▒▒██▒▒                                
                                    ░░██░░████                     
                  """)



