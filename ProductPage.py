import sys
from PyQt5.QtWidgets import (QMainWindow, QCheckBox, QToolBar, QAction, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QComboBox,
                            QScrollArea, QFrame, QSizePolicy, QLabel, QListWidget, QStackedLayout, QListWidgetItem)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QSize

#todo
def GetUserType():
    return 1

def GetUserBalance():
    return 36.99

class ProductPage(QMainWindow):
    def __init__(self, product_data):
        super().__init__()

        self.setWindowTitle("Magazin de produse digitale")
        self.setGeometry(100, 100, 1200, 800)

        self.product_data = product_data

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

        user_type = GetUserType()

        store_action = QAction("Store", self)
        store_action.triggered.connect(self.switch_to_store)

        library_action = QAction("Library", self)
        library_action.triggered.connect(self.switch_to_library)

        management_action = QAction("Management", self)
        management_action.triggered.connect(self.switch_to_management)

        products_action = QAction("Products", self)
        products_action.triggered.connect(self.switch_to_products)

        tool_bar.addAction(store_action)
        tool_bar.addAction(library_action)
        if user_type == 0:
            tool_bar.addAction(management_action)
        else:
            tool_bar.addAction(products_action)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        tool_bar.addWidget(spacer)

        balance = GetUserBalance()
        balance_label = QLabel(f"Balance: ${balance}")
        balance_label.setAlignment(Qt.AlignRight)
        tool_bar.addWidget(balance_label)

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

        title_label = QLabel(self.product_data["title"])
        title_label.setFont(QFont("Arial", 24))
        title_label.setStyleSheet("color: white; font-weight: bold;")
        title_label.setAlignment(Qt.AlignCenter)

        main_layout.addWidget(title_label)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedHeight(300)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        
        scroll_widget = QWidget()
        scroll_layout = QHBoxLayout(scroll_widget)

        for img_path in self.product_data["images"]:
            img_label = QLabel()
            pixmap = QPixmap(img_path)
            pixmap = pixmap.scaledToHeight(250)
            img_label.setPixmap(pixmap)
            scroll_layout.addWidget(img_label)

        scroll_area.setWidget(scroll_widget)
        main_layout.addWidget(scroll_area)

        price_and_buy_layout = QHBoxLayout()
        
        price_label = QLabel(self.product_data["price"])
        price_label.setFont(QFont("Arial", 18))
        price_label.setStyleSheet("color: white;")
        price_label.setAlignment(Qt.AlignCenter)

        price_and_buy_layout.addWidget(price_label)

        buy_button = QPushButton("BUY")
        buy_button.setStyleSheet("background: #0e5b0e; color: white; font-size: 25px; font-weight:bold;")
        buy_button.setFixedSize(150, 60)
        price_and_buy_layout.addWidget(buy_button)

        main_layout.addLayout(price_and_buy_layout)

        description_label = QLabel(self.product_data["description"])
        description_label.setFont(QFont("Arial", 12))
        description_label.setStyleSheet("color: white;")
        description_label.setWordWrap(True)
        main_layout.addWidget(description_label)

        self.setCentralWidget(main_widget)


    def switch_to_store(self):
        from StorePage import StorePage

        self.store_page = StorePage()
        self.store_page.show()
        self.hide()

    def switch_to_management(self):
        from ManagementPage import ManagementPage

        self.management_page = ManagementPage()
        self.management_page.show()
        self.hide()

    def switch_to_products(self):
        from ProductsPage import ProductsPage

        self.products_page = ProductsPage()
        self.products_page.show()
        self.hide()

    def switch_to_library(self):
        from LibraryPage import LibraryPage

        self.library_page = LibraryPage()
        self.library_page.show()
        self.hide()

    