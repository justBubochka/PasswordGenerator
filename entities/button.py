from PyQt6.QtWidgets import QLayout, QPushButton
from helpers.ui.ui_helpers import CreateAndAddWidget


class Button(QPushButton):
    def __init__(self, layout: QLayout, text: str):

        self.widget = CreateAndAddWidget(
            layout=layout, widget=QPushButton(text)
        ).get()

    def get(self):
        return self.widget