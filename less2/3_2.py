class BellTower:
    def __init__(self, *data):
        self.bell_list = [i for i in data]

    def append(self, belli):
        self.bell_list.append(belli)

    def sound(self):
        for i in self.bell_list:
            i.sound()
        print('...')


class Bell:

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def print_info(self):
        if self.args or self.kwargs:
            answer = [f'{i}: {self.kwargs[i]}' for i in sorted(self.kwargs.keys())]
            if self.args:
                if self.kwargs:
                    print(', '.join(answer), '; ', ', '.join(self.args), sep='')
                else:
                    print(', '.join(self.args))
            else:
                print(', '.join(answer))
        else:
            print('-')


class BigBell(Bell):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ding = True

    def sound(self):
        if self.ding:
            self.ding = False
            print('ding')
        else:
            self.ding = True
            print('dong')


class LittleBell(Bell):
    def sound(self):
        print('ding')