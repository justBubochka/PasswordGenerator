import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from widgets.central_widget import CentralWidget



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Окно приложения")
        self.setGeometry(200, 200, 800, 400)
        self.centralWidget = CentralWidget(self) 
        self.setCentralWidget(self.centralWidget)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
