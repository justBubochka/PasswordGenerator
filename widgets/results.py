from PyQt6.QtWidgets import (
    QSizePolicy, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QSpinBox, QCheckBox,
    QWidget, QMessageBox, QLayout, QPushButton
)
import random
import string
from typing import List
from PyQt6.QtCore import Qt
from entities.label import Label
from entities.button import Button
from widgets.main_title import MainTitle
from helpers.ui.ui_helpers import bindWidgetToLayout
from entities.copyText import CopyText



class Results(QWidget):
    def __init__(
            self, 
            layout: QLayout,
            generate_password_func_callback
        ):
        super().__init__()

        self.generate_password_func_callback = generate_password_func_callback
        self.passwords: List = None

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setLayout(self.layout)
        
        self.generated_passwords: List[CopyText] = []
        for i in range(8):
            generated_password_output = CopyText(
                    layout = self.layout, 
                    text = ''
                )
            self.generated_passwords.append(
                generated_password_output
            )
        

        self.generate_button = Button(self.layout, text="Сгенирировать")
        self.generate_button.clicked.connect(self.generate_password_func)

        bindWidgetToLayout(layout=layout, widget=self)

    def generate_password_func(self):
        self.passwords = self.generate_password_func_callback()
        if isinstance(self.passwords, list) and len(self.passwords) > 0:
            for i in range(8):
                self.generated_passwords[i].text.setText(self.passwords[i])
          

