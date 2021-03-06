class Human:
    """Человек"""
    name = ''
    sec_name = ''

    def __init__(self):
        print('Создан новый человек.')

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_second_name(self, sec_name):
        self.sec_name = sec_name

    def get_second_name(self):
        return self.sec_name

    def is_human(self):
        if isinstance(self, Human):
            return True
        else:
            return False
