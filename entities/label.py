from PyQt6.QtWidgets import QLabel, QLayout, QStyle
from PyQt6.QtCore import Qt
from helpers.ui.ui_helpers import bindWidgetToLayout



class Label(QLabel):
    def __init__(
            self, 
            layout: QLayout, 
            text: str
        ):
        super().__init__(text)

        bindWidgetToLayout(
            layout=layout, widget=self
        )