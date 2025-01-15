import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from widgets.central_widget import CentralWidget



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Окно приложения")
        self.setGeometry(200, 100, 1600, 800)
        self.initUI()
        self.generate_password()
        

    def initUI(self):
        self.centralWidget = CentralWidget(self) 
        self.setCentralWidget(self.centralWidget)


    def generate_password(self):
        pass



if __name__ == "__main__":

    app = QApplication(sys.argv)

    # Open the sqq styles file and read in the CSS-alike styling code
    with open('styles.qss', 'r') as f:
        style = f.read()
        # Set the stylesheet of the application
        app.setStyleSheet(style)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
