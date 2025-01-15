from PyQt6.QtWidgets import QLabel, QLayout, QStyle
from helpers.ui.ui_helpers import bindWidgetToLayout



class Title(QLabel):
    def __init__(
            self, 
            layout: QLayout, 
            text: str,
            styles: QStyle = None
        ):
        super().__init__()

        self.widget: QLabel = QLabel(text)
        self.widget.setStyleSheet(styles if styles else "font-size: 18px; font-weight: 400")

        bindWidgetToLayout(
            layout=layout, widget=self.widget
        )


    def get(self):
        return self.widget