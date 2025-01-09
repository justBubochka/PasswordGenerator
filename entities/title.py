from PyQt6.QtWidgets import QLabel, QLayout
from helpers.ui.ui_helpers import CreateAndAddWidget


class Title(QLabel):
    def __init__(self, layout: QLayout, text: str):
        super().__init__()

        self.widget = CreateAndAddWidget(
            layout=layout, widget=QLabel(text)
        ).get()


    def get(self):
        return self.widget