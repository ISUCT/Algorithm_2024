class Mouse():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def NewMouse(self):
        if self.age <= 0 or self.age > 150:
            print("Wrong Age!!!")
        else:
            print("Создана мышка с полом "+ self.sex + " именем " + self.name + " и возрастом " + str(self.age))

            if self.name == "Mickey":
                print("""
                           .--,       .--,
                          ( (  \.---./  ) )
                           '.__/o   o\__.'
                              {=  ^  =}
                             >  '._.'  <
                 ___________.""-------"".____________
                |  o                            O    |
                |                                    |
                |  .  O Hello! I'm Mikkey Mouse =) o |
                |                                    |         __
                |                                    |     _.-'  '.
                |______________o__________o__________| .-~^        '~--'
                             ___)( )(___       '-.___.'
                            (((__) (__)))
                    """)
            elif self.name == "Minnie":
                print("""
                       .--,       .--,
                      ( (  \.---./  ) )
                       '.__/o   o\__.'
                          {=  ^  =}
                         >  '._.'  <
             ___________.""-------"".____________
            |  o                            O    |
            |                                    |
            |  . O  Hello! I'm Minnie Mouse ;) o |
            |                                    |         __
            |                                    |     _.-'  '.
            |______________o__________o__________| .-~^        '~--'
                         ___)( )(___       '-.___.'
                        (((__) (__)))
                    """)
            
