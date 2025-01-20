from PyQt6.QtWidgets import (
    QSizePolicy, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QSpinBox, QCheckBox,
    QWidget, QMessageBox
)
from PyQt6.QtGui import QPainter
import random
import string
from PyQt6.QtCore import Qt
from entities.label import Label
from entities.button import Button
from widgets.main_title import MainTitle
from helpers.ui.ui_helpers import bindWidgetToLayout
from widgets.filters import Filters
from widgets.results import Results
from typing import Callable


class CentralWidget(QWidget):
    def __init__(self, parent, generate_password_func: Callable, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Центральный виджет")
        self.setGeometry(100, 100, 400, 200)
        self.setParent(parent)

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(70, 70, 70, 70)


        self.title = MainTitle(self.layout, text="Генератор случайных паролей")

        # Store the generate_password_func for later use
        self.generate_password_func_callback = generate_password_func

        self.main_content = QWidget()
        self.main_content_layout = QHBoxLayout()
        self.main_content.setLayout(self.main_content_layout)

        self.main_content_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)


        self.layout.addWidget(self.main_content)

        # Filters
        self.filters = Filters(self.main_content_layout)

        self.main_content_layout.addStretch()

        # Results
        self.results = Results(self.main_content_layout, self.generate_password_func)

        
        
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

        self.layout.addWidget(self.description)

    

        self.setLayout(self.layout)

    
    def generate_password_func(self):
        
        return self.generate_password_func_callback(
            password_length=self.filters.password_length.value(),
            use_numbers=self.filters.include_numbers.isChecked(),
            use_uppercase=self.filters.include_uppercase.isChecked(),
            use_lowercase=self.filters.include_lowercase.isChecked(),
            use_symbols=self.filters.include_symbols.isChecked()
        )