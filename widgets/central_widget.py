from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from entities.title import Title
from entities.button import Button


class CentralWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setWindowTitle("Центральный виджет")
        self.setGeometry(100, 100, 400, 200)
        self.setParent(args[0])
        

        self.layout = QVBoxLayout()

        self.title = Title(self.layout, text="Генератор случайных паролей").get()
        self.generateButton = Button(self.layout, text="Сгенирировать").get()
        
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet("font-size: 20px; font-weight: bold;")

        self.setLayout(self.layout)
