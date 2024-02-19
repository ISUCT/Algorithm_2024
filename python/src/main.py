import lab6
if __name__ == '__main__':
    user_1 = (lab6.Phone(89567431302, 'MTS', 'Russia'))
    user_1.set_provider('Tele 2')
    user_1.set_number(89012237788)
    print(user_1.get_provider(), user_1.get_number())

    user_2 = lab6.Phone(38245743897, 'EstoniaCom', 'Estonia')
    print(user_2.get_provider(), user_2.get_country())