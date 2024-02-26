import lab6
if __name__ == "__main__":
    print("struct Foxes")
    foxy = lab6.Fox("Foxy", 5 ,"red")
    try:
        foxy.set_age(5)
    except Exception as error:
        print("have one error", error)
    foxy.new_fox()
