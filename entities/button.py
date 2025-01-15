from PyQt6.QtWidgets import QLayout, QPushButton
from helpers.ui.ui_helpers import bindWidgetToLayout


class Button(QPushButton):
    def __init__(self, layout: QLayout, text: str):

        super().__init__(text)
        self.setFixedSize(212, 48)
    
        bindWidgetToLayout(layout=layout, widget=self)