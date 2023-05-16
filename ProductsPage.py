import sys
from PyQt5.QtWidgets import (QMainWindow, QCheckBox, QToolBar, QAction, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QComboBox,
                            QScrollArea, QFrame, QSizePolicy, QLabel, QListWidget, QStackedLayout, QListWidgetItem)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QSize


class ProductsPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Magazin de produse digitale")
        self.setGeometry(100, 100, 1200, 800)

        self.app_data = [
            {
            "title": "App1",
            "price": "20",
            "revenue": "100",
            },
            {
            "title": "Game1",
            "price": "10",
            "revenue": "500",
            },
            {
            "title": "Tool1",
            "price": "30",
            "revenue": "300",
            },
            {
            "title": "App2",
            "price": "10",
            "revenue": "100",
            },
            {
            "title": "Game2",
            "price": "20",
            "revenue": "400",
            },
            {
            "title": "Tool2",
            "price": "30",
            "revenue": "400",
            },     
        ]

        #self.init_menu_bar()
        self.init_tool_bar()
        self.init_main_layout()

    
    def init_menu_bar(self):
        menu_bar = self.menuBar()

        steam_menu = menu_bar.addMenu("Steam")
        view_menu = menu_bar.addMenu("View")
        friends_menu = menu_bar.addMenu("Friends")
        games_menu = menu_bar.addMenu("Games")
        help_menu = menu_bar.addMenu("Help")

    def init_tool_bar(self):
        tool_bar = QToolBar()

        store_action = QAction("Store", self)
        store_action.triggered.connect(self.switch_to_store)

        library_action = QAction("Library", self)
        library_action.triggered.connect(self.switch_to_library)

        products_action = QAction("Products", self)
        products_action.setDisabled(True)

        tool_bar.addAction(store_action)
        tool_bar.addAction(library_action)
        tool_bar.addAction(products_action)

        for action in tool_bar.actions():
            widget = tool_bar.widgetForAction(action)
            widget.setCursor(Qt.PointingHandCursor)

        tool_bar.setStyleSheet("""
        QToolButton { margin-right: 50px; color: white; font-size: 18px;  }
        QToolBar { background-color: #151515;}
        """)
        tool_bar.setFixedHeight(50)

        self.addToolBar(tool_bar)

    def init_main_layout(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        background = """
        background: #1e1e1e
        """
        self.setStyleSheet("QWidget { background: %s }" % background)
        main_widget.setStyleSheet(background)

        post_new_widget = QFrame()
        post_new_widget.setFrameShape(QFrame.StyledPanel)
        post_new_widget.setFrameShadow(QFrame.Raised)
        post_new_widget.setLineWidth(1)
        post_new_widget.setStyleSheet("border: 1px solid #151515; background: #0e5b0e;")

        post_new_layout = QHBoxLayout()
        post_new_layout.setSpacing(0)

        plus_label = QLabel("+")
        plus_label.setFont(QFont("Arial", 48))
        plus_label.setStyleSheet("color: white; border: 0px;")
        post_new_layout.addWidget(plus_label)
        post_new_layout.addStretch(1)

        post_new_text = QLabel("Post something new")
        post_new_text.setFont(QFont("Arial", 18))
        post_new_text.setStyleSheet("border: 0px; color: white; font-weight:bold;")
        post_new_layout.addWidget(post_new_text)

        post_new_widget.setLayout(post_new_layout)
        post_new_widget.setCursor(Qt.PointingHandCursor)
        post_new_layout.addStretch(1)
        main_layout.addWidget(post_new_widget)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        products_widget = QWidget()
        products_layout = QVBoxLayout(products_widget)

        for app in self.app_data:
            product_widget = self.create_product_widget(app)
            products_layout.addWidget(product_widget)
        
        scroll_area.setWidget(products_widget)
        main_layout.addWidget(scroll_area)

        self.setCentralWidget(main_widget)


    def create_product_widget(self, app):
        product_widget = QFrame()
        product_widget.setFrameShape(QFrame.StyledPanel)
        product_widget.setFrameShadow(QFrame.Raised)
        product_widget.setLineWidth(1)
        product_widget.setStyleSheet("border: 1px solid #CCCCCC;")

        product_layout = QHBoxLayout()

        name_label = QLabel(app["title"])
        name_label.setStyleSheet("font-weight: bold; font-size: 18px; border: 0px; color: white;")

        price_and_revenue_layout = QVBoxLayout()
        price_label = QLabel("Price: ${}".format(app["price"]))
        price_label.setStyleSheet("font-weight: bold; font-size: 18px; border: 0px; color: white;")
        price_and_revenue_layout.addWidget(price_label)

        revenue_label = QLabel("Revenue: ${}".format(app["revenue"]))
        revenue_label.setStyleSheet("font-weight: bold; font-size: 18px; border: 0px; color: white;")
        price_and_revenue_layout.addWidget(revenue_label)

        edit_button = QPushButton("EDIT")
        edit_button.setStyleSheet("font-size: 18px; color: white; background: #151515;")
        edit_button.setFixedSize(80, 80)
        edit_button.setCursor(Qt.PointingHandCursor)

        product_layout.addWidget(name_label)
        product_layout.addStretch(1)
        product_layout.addLayout(price_and_revenue_layout)
        product_layout.addStretch(4)
        product_layout.addWidget(edit_button)
        product_widget.setLayout(product_layout)

        return product_widget


    def switch_to_store(self):
        from StorePage import StorePage

        self.store_page = StorePage()
        self.store_page.show()
        self.hide()

    def switch_to_library(self):
        from LibraryPage import LibraryPage

        self.library_page = LibraryPage()
        self.library_page.show()
        self.hide()

