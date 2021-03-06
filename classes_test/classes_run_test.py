import class_test


def create_new_human(name='', second_name='', sensitivity=3):
    if len(name) >= sensitivity and len(second_name) >= sensitivity:
        new_human = class_test.Human()
        new_human.set_name(name)
        new_human.set_second_name(second_name)
        print(new_human.get_name(), new_human.get_second_name(), 'создан.')
    if len(name) < sensitivity:
        print(f'Длина указанного имени должна превышать {sensitivity} знака!')
    if len(second_name) < sensitivity:
        print(f'Длина указанной фамилии должна превышать {sensitivity} знака!')


def create_zarinchka():
    zarinchka = class_test.Human()
    zarinchka.set_second_name('Aloeva')
    zarinchka.set_name('Zarinchka')
    print(zarinchka.get_name(), zarinchka.get_second_name(), ': Хьюстон ПШШШШШШ!!!', sep='')


a = {'name': 'арун', 'second_name': 'АЛОЕВ', 'sensitivity': 4}

create_zarinchka()
create_new_human(**a)
