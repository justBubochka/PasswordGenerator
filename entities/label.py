from PyQt6.QtWidgets import QLabel, QLayout
from PyQt6.QtCore import Qt
from helpers.ui.ui_helpers import bindWidgetToLayout



class Label(QLabel):
    def __init__(
            self, 
            layout: QLayout, 
            text: str,
            styles: str = None
        ):
        super().__init__(text)

        if styles is not None:
            self.setStyleSheet(styles)

        self.setAlignment(Qt.AlignmentFlag.AlignLeft)

        bindWidgetToLayout(
            layout=layout, widget=self
        )

        # print(self.text())