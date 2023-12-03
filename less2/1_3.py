class Note:
    def __init__(self, note, is_long=None):
        self.note = note
        self.is_long = is_long
        self.baze = {'до': 'до-о', 'ре': 'ре-э',
                     'ми': 'ми-и', 'фа': 'фа-а',
                     'соль': 'со-оль', 'ля': 'ля-а',
                     'си': 'си-и'}

    def __str__(self):
        if self.is_long:
            return self.baze[self.note]
        else:
            return self.note


class LoudNote(Note):
    def __str__(self):
        return super().__str__().upper()


class DefaultNote(Note):
    def __init__(self, note='до', is_long=None):
        super().__init__(note, is_long)


class NoteWithOctave(Note):
    def __init__(self, note, okt, is_long=None):
        super().__init__(note, is_long)
        self.okt = okt

    def __str__(self):
        return f'{super().__str__()} ({self.okt})'


PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]