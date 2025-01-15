from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from entities.label import Label
from entities.button import Button
from widgets.main_title import MainTitle


class CentralWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setWindowTitle("Центральный виджет")
        self.setGeometry(100, 100, 400, 200)
        self.setParent(args[0])
        

        self.layout = QVBoxLayout()

        self.title = MainTitle(self.layout, text="Генератор случайных паролей")
        self.passwordLengthLabel = Label(self.layout, "Длина пароля:")

        
        self.generateButton = Button(self.layout, text="Сгенирировать")


        self.setLayout(self.layout)
