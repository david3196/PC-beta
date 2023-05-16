import sys
from PyQt5.QtWidgets import (QDialog,QWidget, QHBoxLayout, QLabel, QVBoxLayout, QGridLayout, QLineEdit, QPushButton)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize

from RegisterPage import RegisterDialog

def getErrorMessage():
    return "Mesaj de eroare!"

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 1000, 400)

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(main_layout)

        self.setStyleSheet("background: #1e1e1e;")

        image_layout = QHBoxLayout()
        image_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addLayout(image_layout)

        image_label = QLabel()
        image_label.setPixmap(QIcon("./login-img.png").pixmap(720, 400))
        image_layout.addWidget(image_label)

        login_layout = QVBoxLayout()
        main_layout.addLayout(login_layout)

        login_title = QLabel("Login")
        login_title.setFont(QFont("Arial", 24))
        login_title.setStyleSheet("color: white; font-weight: bold;")
        login_title.setAlignment(Qt.AlignCenter)
        login_layout.addWidget(login_title)

        login_layout.addStretch(1)

        error_message = QLabel()
        error_message.setFont(QFont("Arial", 11))
        error_message.setStyleSheet("color: white; background: #9b3535;")
        error_message.setAlignment(Qt.AlignCenter)
        error_message.setText(getErrorMessage())

        if getErrorMessage() != "":
            login_layout.addWidget(error_message)

        input_layout = QGridLayout()
        login_layout.addLayout(input_layout)

        username_label = QLabel("Username:")
        username_label.setStyleSheet("color: white;")
        username_edit = QLineEdit()
        username_edit.setStyleSheet("color: white;")
        input_layout.addWidget(username_label, 0, 0)
        input_layout.addWidget(username_edit, 0, 1)

        password_label = QLabel("Password:")
        password_label.setStyleSheet("color: white;")
        password_edit = QLineEdit()
        password_edit.setStyleSheet("color: white;")
        password_edit.setEchoMode(QLineEdit.Password)
        input_layout.addWidget(password_label, 1, 0)
        input_layout.addWidget(password_edit, 1, 1)

        login_layout.addStretch(1)

        login_button = QPushButton("Login")
        login_button.setFixedSize(100, 50)
        login_button.setStyleSheet("background: #0e5b0e; color: white; font-size: 20px; font-weight:bold;")
        login_button.setCursor(Qt.PointingHandCursor)
        login_button.clicked.connect(self.accept)

        login_button_layout = QHBoxLayout()
        login_button_layout.addStretch()
        login_button_layout.addWidget(login_button)
        login_button_layout.addStretch()

        login_layout.addLayout(login_button_layout)

        login_layout.addStretch(1)

        register_button = QPushButton("Create a new account")
        register_button.setStyleSheet("background: #151515; color: white;")
        register_button.setCursor(Qt.PointingHandCursor)
        login_layout.addWidget(register_button)
        
        register_button.clicked.connect(self.open_registration)

    def open_registration(self):
        register_dialog = RegisterDialog()
        register_dialog.exec_()