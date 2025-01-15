from PyQt6.QtWidgets import QWidget, QLayout


def bindWidgetToLayout(layout: QLayout, widget: QWidget):
    layout.addWidget(widget)
    return widget