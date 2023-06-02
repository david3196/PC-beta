import sys
from PyQt5.QtWidgets import (QMainWindow, QCheckBox, QToolBar, QAction, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QComboBox,
                            QScrollArea, QFrame, QSizePolicy, QLabel, QToolButton)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from ProductPage import ProductPage

#todo
def GetUserType():
    return 0

def GetUserBalance():
    return 36.99

def getUserLibList():
    list = [
        {"date": "10.12.2022",
        "title": "App1",
        "price": "12"},
        {"date": "5.05.2023",
        "title": "Game1",
        "price": "14"},
        {"date": "16.06.2022",
        "title": "App2",
        "price": "18"},
        {"date": "10.02.2023",
        "title": "Tool2",
        "price": "19"},
        {"date": "10.12.2022",
        "title": "App1",
        "price": "12"},
        {"date": "5.05.2023",
        "title": "Game1",
        "price": "14"},
        {"date": "16.06.2022",
        "title": "App2",
        "price": "18"},
        {"date": "10.02.2023",
        "title": "Tool2",
        "price": "19"},
    ]
    return list

class ClickableQFrame(QFrame):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()


class WalletPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Magazin de produse digitale")
        self.setGeometry(100, 100, 1200, 800)
        self.app_data = getUserLibList()
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
        
        
        title_label = QLabel("Current balance: $" + str(GetUserBalance()))
        title_label.setFont(QFont("Arial", 15))
        title_label.setStyleSheet("color: white;")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        main_layout.addStretch(1)

        history_label = QLabel("Purchase history")
        history_label.setFont(QFont("Arial", 20))
        history_label.setStyleSheet("color: white; font-weight: bold;")
        history_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(history_label)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        apps_widget = QWidget()
        apps_layout = QVBoxLayout(apps_widget)
        
        for app in self.app_data:
            app_widget = self.create_app_widget(app)
            apps_layout.addWidget(app_widget)

        scroll_area.setWidget(apps_widget)
        main_layout.addWidget(scroll_area)

        main_layout.addStretch(3)
        if len(getUserLibList()) > 0:
            self.setCentralWidget(main_widget)
        else:
            main_widget = QWidget()
            main_layout = QVBoxLayout(main_widget)

            background = """
            background: #1e1e1e
            """
            self.setStyleSheet("QWidget { background: %s }" % background)
            main_widget.setStyleSheet(background)
            main_layout.addStretch(3)
            title_label = QLabel("Current balance: $" + str(GetUserBalance()))
            title_label.setFont(QFont("Arial", 15))
            title_label.setStyleSheet("color: white;")
            title_label.setAlignment(Qt.AlignCenter)
            main_layout.addWidget(title_label)
            
            main_layout.addStretch(1)

            no_label = QLabel("You have no purchases yet!")
            no_label.setFont(QFont("Arial", 17))
            no_label.setStyleSheet("color: white; font-weight: bold;")
            no_label.setAlignment(Qt.AlignCenter)
            main_layout.addWidget(no_label)
            main_layout.addStretch(3)

            self.setCentralWidget(main_widget)

    def create_app_widget(self, app):
        app_widget = ClickableQFrame()
        app_widget.setFrameShape(QFrame.StyledPanel)
        app_widget.setFrameShadow(QFrame.Raised)
        app_widget.setLineWidth(1)
        app_widget.setStyleSheet("border: 1px solid #CCCCCC;")

        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        app_widget.setSizePolicy(size_policy)
        app_widget.setFixedHeight(50)

        app_layout = QHBoxLayout()

        date_label = QLabel(app["date"])
        date_label.setStyleSheet("font-size: 18px; border: 0px; color: white;")
        
        title_label = QLabel(app["title"])
        title_label.setStyleSheet("font-size: 18px; border: 0px; color: white;")

        price_label = QLabel("$"+app["price"])
        price_label.setStyleSheet("font-size: 18px; border: 0px; color: white;")

        
        app_layout.addStretch(1)
        app_layout.addWidget(date_label)
        app_layout.addStretch(1)
        app_layout.addWidget(title_label)
        app_layout.addStretch(1)
        app_layout.addWidget(price_label)
        app_layout.addStretch(1)

        app_widget.setLayout(app_layout)

        return app_widget
    
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

        self.cart_page = CartPage(self.app_data)
        self.cart_page.show()
        self.hide()

    def switch_to_wallet(self):
        from WalletPage import WalletPage

        self.wallet_page = WalletPage()
        self.wallet_page.show()
        self.hide()
        
