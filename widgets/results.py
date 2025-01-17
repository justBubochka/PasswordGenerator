from PyQt6.QtWidgets import (
    QSizePolicy, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QSpinBox, QCheckBox,
    QWidget, QMessageBox, QLayout, QPushButton
)
import random
import string
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
        ):
        super().__init__()

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setLayout(self.layout)

        self.generated_password_output = CopyText(
            layout=self.layout, 
            text="НОВЫЙ ПАРОЛЬ"
        )

        # self.generate_button = QPushButton("Generate Password")
        # self.generate_button.clicked.connect(self.generate_password)

        

        self.generateButton = Button(self.layout, text="Сгенирировать")

        bindWidgetToLayout(layout=layout, widget=self)

