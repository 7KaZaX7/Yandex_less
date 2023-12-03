class Note:
    def __init__(self, note, check=None):
        self.note = note
        self.check = check
        self.baze = {'до': 'до-о', 'ре': 'ре-э',
                     'ми': 'ми-и', 'фа': 'фа-а',
                     'соль': 'со-оль', 'ля': 'ля-а',
                     'си': 'си-и'}

    def __str__(self):
        if self.check:
            return self.baze[self.note]
        else:
            return self.note
