from PyQt6.QtWidgets import (
    QSizePolicy, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QSpinBox, QCheckBox,
    QWidget, QMessageBox
)
import random
import string
from PyQt6.QtCore import Qt
from entities.label import Label
from entities.button import Button
from widgets.main_title import MainTitle
from helpers.ui.ui_helpers import bindWidgetToLayout
from widgets.filters import Filters
from widgets.results import Results


class CentralWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setWindowTitle("Центральный виджет")
        self.setGeometry(100, 100, 400, 200)
        self.setParent(args[0])
        

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignJustify)

        self.title = MainTitle(self.layout, text="Генератор случайных паролей")

        self.main_content_layout = QHBoxLayout()
        self.main_content_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout.addLayout(self.main_content_layout)

        # Filters
        self.filters = Filters()

        # Results
        self.results = Results()


        self.main_content_layout.addWidget(self.filters)
        self.main_content_layout.addStretch()
        self.main_content_layout.addWidget(self.results)

        
        
        self.description = Label(
            self.layout, 
            """Генератор паролей - незаменимый помощник при регистрации нового аккаунта, когда нужно придумать сложный пароль, подходящий под критерии площадки. \nВыберите состав пароля и его длину, и система сгенерирует для Вас индивидуальную последовательность символов. \nОт вас требуется всего несколько кликов и программа поможет сгенерировать сразу несколько случайных надежных паролей на выбор.""",
            """
                font-size: 18px;
                font-family: Fira Sans, sans-serif;
                margin: 20px 0;
            """
        )
        self.description.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)


        self.setLayout(self.layout)
        