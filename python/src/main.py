import lab5pyt
if __name__ == '__main__':
    comp = (lab5pyt.Comp(1024, 'Kingston', 'HDD'))
    comp.set_name('Hollow Purple')
    comp.set_value(512)
    print(comp.get_value(), comp.get_name(), comp.get_type())
