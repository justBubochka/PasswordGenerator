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
            layout: QLayout = None,
        ):
        super().__init__()

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setLayout(self.layout)

        self.setFixedSize(400, 100)

        self.passwordLengthLabel = Label(self.layout, "Длина пароля:")
        self.passwordLength = QSpinBox()
        bindWidgetToLayout(
            layout=self.layout, widget=self.passwordLength
        )
