import sys
import string
import secrets
from PyQt6.QtWidgets import QApplication, QMainWindow
from widgets.central_widget import CentralWidget
from typing import Callable



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Окно приложения")
        self.setGeometry(200, 100, 1600, 800)
        self.initUI()

        

    def initUI(self):
        self.centralWidget = CentralWidget(self, self.generate_password) 
        self.setCentralWidget(self.centralWidget)   


    def generate_password(self, password_length: int, use_numbers: bool, use_uppercase: bool, use_lowercase: bool, use_symbols: bool):
        sequence = ""
        # sequence_rules
        if (password_length < 8):
            return
        if (use_numbers):
            sequence += string.digits
        if (use_uppercase):
            sequence += string.ascii_uppercase
        if (use_lowercase):
            sequence += string.ascii_lowercase
        if (use_symbols):
            sequence += string.punctuation

        passwords = []
        if (use_numbers is False and use_uppercase is False and use_lowercase is False and use_symbols is False):
            return passwords
        
        password = ''
        while True and len(passwords) < 8:
            password = ''
            password = password.join(secrets.choice(sequence) for i in range(password_length))

            if (
                (any(c.islower() for c in password) if use_lowercase is True else True) 
                and (any(c.isupper() for c in password) if use_uppercase is True else True) 
                and (sum(c.isdigit() for c in password) >= 3 if use_numbers is True else True)
            ):
                passwords.append(password)
            if len(passwords) == 8:
                break
        return passwords



if __name__ == "__main__":

    app = QApplication(sys.argv)

    # Open the sqq styles file and read in the CSS-alike styling code
    with open('styles.qss', 'r') as f:
        style = f.read()
        # Set the stylesheet of the application
        app.setStyleSheet(style)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
