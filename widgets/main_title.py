from PyQt6.QtWidgets import QLayout, QStyle
from PyQt6.QtCore import Qt
from entities.label import Label
from helpers.ui.ui_helpers import bindWidgetToLayout


class MainTitle(Label):
    def __init__(
            self, 
            layout: QLayout, 
            text: str
        ):

        super().__init__(layout, text)

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
