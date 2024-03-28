from computer import Computer

if __name__ == "__main__":
    my_computer = Computer()
    my_computer.name = "First PC"
    my_computer.set_hard_drive_capacity(256)  

    print(f"{my_computer.name} has a hard drive capacity of {my_computer.get_hard_drive_capacity()} GB.")