import lab5

if __name__ == "__main__":
    john = lab5.Person("John", 22, "male")
    michael = lab5.Person("Michael", 34, "male")
    
    try:
        john.set_age(25)
    except Exception as error:
        print("have one error:", error)
    
    print(michael.know_gender())
    
    try:
        print(michael.go_to_walk(10))
    except Exception as error:
        print("have one error:", error)
        
    print(john.get_name() + "'s age - " + str(john.get_age()))