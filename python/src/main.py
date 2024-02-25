from __init__ import Person

if __name__ == '__main__':
    human_1 = Person(37, 'Сергей', 'муж')
    human_1.set_name('Константин')
    human_1.set_age(40)
    print(human_1.get_name(), human_1.get_age())
    human_2 = Person(18, 'Ульяна', 'жен')
    print(human_2.get_name(), human_2.get_age())
    human_2.death_person()
