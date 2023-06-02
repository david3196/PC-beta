import sys
from PyQt5.QtWidgets import (QMainWindow, QCheckBox, QToolBar, QAction, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QComboBox,
                            QScrollArea, QFrame, QSizePolicy, QLabel, QListWidget, QStackedLayout, QListWidgetItem)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QSize


class RaportPage(QMainWindow):
    def __init__(self, product_data):
        super().__init__()

        self.setWindowTitle("Magazin de produse digitale")
        self.setGeometry(100, 100, 600, 600)

        self.product_data = product_data
        self.init_main_layout()

    def init_main_layout(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)

        background = """
        background: #1e1e1e
        """
        self.setStyleSheet("QWidget { background: %s }" % background)
        main_widget.setStyleSheet(background)

        title_label = QLabel("Raport "+ self.product_data["title"])
        title_label.setFont(QFont("Arial", 20))
        title_label.setStyleSheet("color: white; font-weight: bold;")
        title_label.setAlignment(Qt.AlignCenter)

        main_layout.addWidget(title_label)

        scroll_area = QScrollArea()
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedHeight(500)
        
        scroll_widget = QWidget()
        scroll_layout = QHBoxLayout(scroll_widget)

        text_label = QLabel(self.product_data["raport"])
        text_label.setStyleSheet("color: white;")
        text_label.setWordWrap(True)
        font = QFont()
        font.setPointSize(10)
        text_label.setFont(font)
        scroll_layout.addWidget(text_label)
        scroll_layout.setAlignment(Qt.AlignTop)
        scroll_area.setWidget(scroll_widget)
        main_layout.addWidget(scroll_area)

        self.setCentralWidget(main_widget)

    

    