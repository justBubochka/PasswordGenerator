from PyQt6.QtWidgets import QLayout, QPushButton
from helpers.ui.ui_helpers import bindWidgetToLayout


class Button(QPushButton):
    def __init__(self, layout: QLayout, text: str):

        self.widget = QPushButton(text)
        bindWidgetToLayout(layout=layout, widget=self.widget)

    def get(self):
        return self.widget