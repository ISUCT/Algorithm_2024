import fox

if __name__ == "__main__":
    alissa = fox.Fox("Alissa", 0, "female")
    
    try:
        alissa.set_age(12)
    except Exception as error: 
        print("Error:", error)

    print(alissa.displayfox())  
