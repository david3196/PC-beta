import sys
from PyQt5.QtWidgets import (QDialog, QHBoxLayout, QLabel, QVBoxLayout, QGridLayout, QLineEdit, QPushButton, QCheckBox)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize

def getErrorMessage():
    return "Mesaj de eroare!"

class RegisterDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Create a new account")
        self.setGeometry(100, 100, 800, 400)

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(main_layout)

        self.setStyleSheet("background: #1e1e1e; color: white;")

        image_layout = QHBoxLayout()
        image_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addLayout(image_layout)

        image_label = QLabel()
        image_label.setPixmap(QIcon("./login-img.png").pixmap(720, 400))
        image_layout.addWidget(image_label)

        register_layout = QVBoxLayout()
        main_layout.addLayout(register_layout)

        register_title = QLabel("Create a new account")
        register_title.setFont(QFont("Arial", 23))
        register_title.setStyleSheet("margin-left: 20px; margin-right: 20px;")
        register_layout.addWidget(register_title)

        register_layout.addStretch(1)

        error_message = QLabel()
        error_message.setFont(QFont("Arial", 11))
        error_message.setStyleSheet("color: white; background: #9b3535;")
        error_message.setAlignment(Qt.AlignCenter)
        error_message.setText(getErrorMessage())

        if getErrorMessage() != "":
            register_layout.addWidget(error_message)

        input_layout = QGridLayout()
        register_layout.addLayout(input_layout)

        username_label = QLabel("Username:")
        username_edit = QLineEdit()
        input_layout.addWidget(username_label, 0, 0)
        input_layout.addWidget(username_edit, 0, 1)

        password_label = QLabel("Password:")
        password_edit = QLineEdit()
        password_edit.setEchoMode(QLineEdit.Password)
        input_layout.addWidget(password_label, 1, 0)
        input_layout.addWidget(password_edit, 1, 1)

        confirm_password_label = QLabel("Confirm password:")
        confirm_password_edit = QLineEdit()
        confirm_password_edit.setEchoMode(QLineEdit.Password)
        input_layout.addWidget(confirm_password_label, 2, 0)
        input_layout.addWidget(confirm_password_edit, 2, 1)

        email_label = QLabel("Email:")
        email_edit = QLineEdit()
        input_layout.addWidget(email_label, 3, 0)
        input_layout.addWidget(email_edit, 3, 1)

        register_layout.addStretch(1)

        terms_check = QCheckBox("I agree to the Terms and Conditions")
        register_layout.addWidget(terms_check)

        create_account_button = QPushButton("Create account")
        create_account_button.setFixedSize(150, 50)
        create_account_button.setStyleSheet("background: #0e5b0e; color: white; font-size: 15px; font-weight:bold;")
        create_account_button.setCursor(Qt.PointingHandCursor)

        create_account_button.clicked.connect(self.accept)

        create_account_button_layout = QHBoxLayout()
        create_account_button_layout.addStretch()
        create_account_button_layout.addWidget(create_account_button)
        create_account_button_layout.addStretch()

        register_layout.addLayout(create_account_button_layout)

