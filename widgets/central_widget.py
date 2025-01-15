from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PyQt6.QtCore import Qt
from entities.label import Label
from entities.button import Button
from widgets.main_title import MainTitle


class CentralWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setWindowTitle("Центральный виджет")
        self.setGeometry(100, 100, 400, 200)
        self.setParent(args[0])
        

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignJustify)

        self.title = MainTitle(self.layout, text="Генератор случайных паролей")
        self.passwordLengthLabel = Label(self.layout, "Длина пароля:")

        
        self.generateButton = Button(self.layout, text="Сгенирировать")
        
        self.description = Label(
            self.layout, 
            """Генератор паролей - незаменимый помощник при регистрации нового аккаунта, когда нужно придумать сложный пароль, подходящий под критерии площадки. \nВыберите состав пароля и его длину, и система сгенерирует для Вас индивидуальную последовательность символов. \nОт вас требуется всего несколько кликов и программа поможет сгенерировать сразу несколько случайных надежных паролей на выбор.""",
            """
                font-size: 18px;
                font-family: Fira Sans, sans-serif;
                margin: 20px 0;
            """
        )
        self.description.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)


        self.setLayout(self.layout)
