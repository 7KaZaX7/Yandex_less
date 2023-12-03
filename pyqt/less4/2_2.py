from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QApplication

class MorseCode(QWidget):
    def __init__(self):
        super().__init__()
        self.alphabet_buttons = {}
        self.result = QLineEdit()
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        for letter in alphabet:
            button = QPushButton(letter)
            button.resize(button.sizeHint())
            button.clicked.connect(lambda state, l=letter: self.add_morse_code(l))
            self.alphabet_buttons[letter] = button
            layout.addWidget(button)
        
        layout.addWidget(self.result)
        
    def add_morse_code(self, letter):
        morse_code = self.get_morse_code(letter)
        self.result.setText(self.result.text() + morse_code)
        
    def get_morse_code(self, letter):
        morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',   
         'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
         'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••'}
        return morze[letter]

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    
    window = MorseCode()
    window.show()
    
    sys.exit(app.exec_())