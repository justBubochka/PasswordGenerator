from PyQt6.QtWidgets import (
    QSizePolicy, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QSpinBox, QCheckBox,
    QWidget, QMessageBox, QLayout
)
import random
import string
from PyQt6.QtCore import Qt
from entities.label import Label
from entities.button import Button
from widgets.main_title import MainTitle
from helpers.ui.ui_helpers import bindWidgetToLayout


class Filters(QWidget):
    def __init__(
            self, 
            layout: QLayout
        ):
        super().__init__()

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.layout)

        
        self.password_wrapper = QWidget()
        self.password_wrapper_layout = QHBoxLayout()
        self.password_wrapper.setLayout(self.password_wrapper_layout)
        self.password_wrapper_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.layout.addWidget(self.password_wrapper)

        self.password_length_label = Label(self.password_wrapper_layout, "Длина пароля:")
        self.password_length = QSpinBox()
        self.password_length.setRange(4, 128)
        self.password_length.setValue(12)
        bindWidgetToLayout(
            layout=self.password_wrapper_layout, widget=self.password_length
        )

        self.include_numbers = QCheckBox("Цифры")
        self.include_numbers.setChecked(True)
        bindWidgetToLayout(
            layout=self.layout, widget=self.include_numbers
        )

        self.include_uppercase = QCheckBox("ПРОПИСНЫЕ БУКВЫ")
        self.include_uppercase.setChecked(True)
        bindWidgetToLayout(
            layout=self.layout, widget=self.include_uppercase
        )

        self.include_lowercase = QCheckBox("строчные буквы")
        self.include_lowercase.setChecked(True)
        bindWidgetToLayout(
            layout=self.layout, widget=self.include_lowercase
        )

        self.include_symbols = QCheckBox("Спец.символы")
        self.include_symbols.setChecked(True)
        bindWidgetToLayout(
            layout=self.layout, widget=self.include_symbols
        )





        bindWidgetToLayout(layout=layout, widget=self)

