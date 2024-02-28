from __init__ import Character

if __name__ == '__main__':
    char = Character('Alduin', 'Berserk', 20)
    print(char.get_name(), char.get_clas(), char.get_lvl())
    char.set_lvl(30)
    char.set_clas('Hunt')
    print(char.get_name(), char.get_clas(), char.get_lvl())