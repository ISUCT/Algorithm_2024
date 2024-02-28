class Lisitca:
    def __init__(fox, name: str, color: str, age: int):
        fox.name = name
        fox.color = fox.set_color(color)
        fox.age = fox.set_age(age)


    def set_name(fox, name):
        fox.name = name
    def set_color(fox, color: str) -> str:
        colors = ['оранжевый', 'белый', 'красный', 'серый', 'бурый']
        if color in colors:
            fox.color = color
            return color
        else:
            raise ValueError('цвет указан неверно')
    def set_age(fox, age: int) -> int:
        if 0 <= age <= 30:
            fox.age = age
            return age
        else:
            raise ValueError('возраст указан неверно')


    def fox_inf(fox):
        return f' имя {fox.name}\n цвет {fox.color}\n возраст {fox.age}'
    
    def voice(fox, voice):
        return f'лисица {fox.name} говорит {voice}'

    def calling(fox):
        return f'вы подозвали лисицу {fox.name}, которая имеет цвет окраса {fox.color}'
