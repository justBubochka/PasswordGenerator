from PyQt6.QtWidgets import QLayout, QStyle
from entities.title import Title
from helpers.ui.ui_helpers import bindWidgetToLayout


class FirstLabel(Title):
    def __init__(
            self, 
            layout: QLayout, 
            text: str,
            styles: QStyle = None
        ):
        super().__init__()

        self.widget: Title = Title(layout, text, styles)
        # self.styles = styles
        self.widget.setStyleSheet(styles if styles else "font-size: 18px; font-weight: 400")

        bindWidgetToLayout(
            layout=layout, widget=self.widget
        )


    def get(self):
        return self.widget