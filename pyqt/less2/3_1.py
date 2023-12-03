class BellTower:
    def __init__(self, *data):
        self.bell_list = [i for i in data]

    def append(self, bell):
        self.bell_list.append(bell)

    def sound(self):
        for i in self.bell_list:
            print(i.sound())
        print('...')


class BigBell:
    def __init__(self):
        self.ding = True

    def sound(self):
        if self.ding:
            self.ding = False
            return 'ding'
        self.ding = True
        return 'dong'


class LittleBell:
    def sound(self):
        return 'ding'