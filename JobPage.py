import sys
from PyQt5.QtWidgets import (QMainWindow, QCheckBox, QToolBar, QAction, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QComboBox,
                            QScrollArea, QFrame, QSizePolicy, QLabel, QListWidget, QStackedLayout, QListWidgetItem, QToolButton, QTextEdit)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QSize

#todo
def GetUserType():
    return 1

def GetUserBalance():
    return 36.99

class JobPage(QMainWindow):
    def __init__(self, product_data):
        super().__init__()

        self.setWindowTitle("Magazin de produse digitale")
        self.setGeometry(100, 100, 1200, 800)

        self.product_data = product_data

        self.init_tool_bar()
        self.init_main_layout()
    
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
        store_action_widget = tool_bar.widgetForAction(store_action)
        store_action_widget.setCursor(Qt.PointingHandCursor)
        tool_bar.addAction(library_action)
        library_action_widget = tool_bar.widgetForAction(library_action)
        library_action_widget.setCursor(Qt.PointingHandCursor)
        
        if user_type == 0:
            tool_bar.addAction(management_action)
            management_action_widget = tool_bar.widgetForAction(management_action)
            management_action_widget.setCursor(Qt.PointingHandCursor)
        else:
            tool_bar.addAction(products_action)
            products_action_widget = tool_bar.widgetForAction(products_action)
            products_action_widget.setCursor(Qt.PointingHandCursor)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        tool_bar.addWidget(spacer)

        cart_button = QToolButton()
        cart_icon = QIcon("./cart.png")
        cart_button.setIcon(cart_icon)
        cart_button.setCursor(Qt.PointingHandCursor)
        tool_bar.addWidget(cart_button)
        cart_button.clicked.connect(self.switch_to_cart)

        balance = GetUserBalance()

        balance_button = QToolButton()
        wallet_icon = QIcon("./wallet.png")
        balance_button.setIcon(wallet_icon)
        balance_button.setText(f'${balance}')
        balance_button.setStyleSheet("font-size: 14px")
        balance_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        balance_button.setCursor(Qt.PointingHandCursor)
        tool_bar.addWidget(balance_button)
        balance_button.clicked.connect(self.switch_to_wallet)

        
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
        title_label.setFont(QFont("Arial", 20))
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

        price_layout = QHBoxLayout()
        
        price_label = QLabel("Price: "+ str(self.product_data["price"]))
        price_label.setFont(QFont("Arial", 18))
        price_label.setStyleSheet("color: white;")
        price_label.setAlignment(Qt.AlignCenter)

        price_layout.addWidget(price_label)
        main_layout.addLayout(price_layout)

        description_label = QLabel(self.product_data["description"])
        description_label.setWordWrap(True)
        description_label.setAlignment(Qt.AlignJustify)
        
        description_label.setStyleSheet("font-size: 16px; color: white; padding: 20px;")

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(description_label)
        scroll_area.setMinimumHeight(250)
        main_layout.addWidget(scroll_area)

        test_layout = QHBoxLayout()
        test_button = QPushButton("DOWNLOAD")
        test_button.setCursor(Qt.PointingHandCursor)
        test_button.setStyleSheet("background: #3e613e; color: white; font-size: 20px; font-weight:bold;")
        test_button.setFixedSize(170, 60)
        test_button.clicked.connect(self.download)
        test_layout.addWidget(test_button)

        main_layout.addLayout(test_layout)

        self.raport_input = QTextEdit()
        self.raport_input.setAcceptDrops(False)
        self.raport_input.setPlaceholderText("Raport...")
        self.raport_input.setStyleSheet("color: white;")
        self.raport_input.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.raport_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.raport_input.setFixedHeight(300)
        main_layout.addWidget(self.raport_input)

        accept_and_reject_layout = QHBoxLayout()

        reject_button = QPushButton("REJECT")
        reject_button.setCursor(Qt.PointingHandCursor)
        reject_button.setStyleSheet("background: red; color: white; font-size: 25px; font-weight:bold;")
        reject_button.setFixedSize(150, 60)
        reject_button.clicked.connect(self.reject)

        accept_button = QPushButton("ACCEPT")
        accept_button.setCursor(Qt.PointingHandCursor)
        accept_button.setStyleSheet("background: #0e5b0e; color: white; font-size: 25px; font-weight:bold;")
        accept_button.setFixedSize(150, 60)
        accept_button.clicked.connect(self.accept)

        accept_and_reject_layout.addWidget(accept_button)
        accept_and_reject_layout.addWidget(reject_button)
        main_layout.addLayout(accept_and_reject_layout)

        scroll_area = QScrollArea()
        scroll_area.setStyleSheet("background: #1e1e1e;")
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(main_widget)
        self.setCentralWidget(scroll_area)


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

    def switch_to_cart(self):
        from CartPage import CartPage

        self.cart_page = CartPage(self.product_data)
        self.cart_page.show()
        self.hide()

    def reject(self):
        pass

    def download(self):
        pass

    def accept(self):
        raport_content = self.raport_input.toPlainText()
        print(raport_content)
        
        from ManagementPage import ManagementPage

        self.management_page = ManagementPage()
        self.management_page.show()
        self.hide()
    
    def switch_to_wallet(self):
        from WalletPage import WalletPage

        self.wallet_page = WalletPage()
        self.wallet_page.show()
        self.hide()