from PyQt6.QtWidgets import QLayout, QPushButton
from helpers.ui.ui_helpers import bindWidgetToLayout


class Button(QPushButton):
    def __init__(self, layout: QLayout, text: str, styles: str = None):

        super().__init__(text)
        # self.basic_styles = """
            
        # """

        # self.setStyleSheet(self.basic_styles + '; ' + styles if styles else self.basic_styles)
    
        bindWidgetToLayout(layout=layout, widget=self)