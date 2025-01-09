from PyQt6.QtWidgets import QWidget, QLayout


class CreateAndAddWidget:
    def __init__(self, layout: QLayout, widget: QWidget):
        self.layout = layout
        self.widget = widget
        self.layout.addWidget(self.widget)

    def get(self):
        return self.widget