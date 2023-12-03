from typing import List


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

    def __eq__(self, other):
        return self.note == other

    def __gt__(self, other):
        return PITCHES.index(self.note) > PITCHES.index(other)

    def __ge__(self, other):
        return PITCHES.index(self.note) >= PITCHES.index(other)

    def __rshift__(self, other):
        index = (PITCHES.index(self.note) + other) % N
        return Note(note=PITCHES[index], is_long=self.is_long)

    def __lshift__(self, other):
        index = (PITCHES.index(self.note) - other) % N
        return Note(note=PITCHES[index], is_long=self.is_long)

    def get_interval(self, elem):
        if PITCHES.index(elem.note) > PITCHES.index(self.note):
            a = PITCHES.index(elem.note) - PITCHES.index(self.note)
        else:
            a = PITCHES.index(self.note) - PITCHES.index(elem.note)
        return INTERVALS[a]


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


class Melody:
    def __init__(self, notes: List[Note] = None):
        if notes is None:
            notes = []
        self.notes = notes

    def __str__(self):
        return ', '.join(str(i) for i in self.notes).capitalize()

    def __len__(self):
        return len(self.notes)

    def __rshift__(self, other):
        new_notes = []
        for i in self.notes:
            if str(i) in PITCHES:
                if PITCHES.index(str(i)) + other % N > N - 1:
                    new_notes = [str(i) for i in self.notes]
                    break
                else:
                    new_notes.append(Note.__rshift__(i, other))
            else:
                if LONG_PITCHES.index(str(i)) + other % N > N - 1:
                    new_notes = [str(i) for i in self.notes]
                    break
                else:
                    new_notes.append(Note.__rshift__(i, other))
        return Melody(notes=new_notes)

    def __lshift__(self, other):
        new_notes = []
        for i in self.notes:
            if str(i) in PITCHES:
                if PITCHES.index(str(i)) - other % N < 0:
                    new_notes = [str(i) for i in self.notes]
                    break
                else:
                    new_notes.append(Note.__lshift__(i, other))
            else:
                if LONG_PITCHES.index(str(i)) - other % N < 0:
                    new_notes = [str(i) for i in self.notes]
                    break
                else:
                    new_notes.append(Note.__lshift__(i, other))
        return Melody(notes=new_notes)

    def replace_last(self, note):
        self.notes[-1] = note

    def append(self, note):
        self.notes.append(note)

    def remove_last(self):
        self.notes.pop()

    def clear(self):
        self.notes.clear()


N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]
