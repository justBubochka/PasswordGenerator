from PyQt6.QtWidgets import QLabel, QPushButton, QLayout, QWidget, QHBoxLayout
from PyQt6.QtCore import Qt
from helpers.ui.ui_helpers import bindWidgetToLayout
import pyperclip



class CopyText(QWidget):
    def __init__(
            self, 
            layout: QLayout, 
            text: str,
            styles: str = None
        ):
        super().__init__()

        if styles is not None:
            self.setStyleSheet(styles)

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.text = QLabel(text)
        self.copyButton = QPushButton("Copy")

        layout.addWidget(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.copyButton)

        self.copyButton.clicked.connect(self.button_was_clicked)
        


        bindWidgetToLayout(
            layout=layout, widget=self
        )


    def button_was_clicked (self):
        self.writeTextToBuffer(self.text.text())

        
    def writeTextToBuffer(self, name):
        pyperclip.copy(name) #Копирует в буфер обмена информацию
        pyperclip.paste()