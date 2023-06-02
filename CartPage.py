import sys
from PyQt5.QtWidgets import (QMainWindow, QCheckBox, QToolBar, QAction, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QComboBox,
                            QScrollArea, QFrame, QSizePolicy, QLabel, QListWidget, QStackedLayout, QListWidgetItem, QToolButton, QTableWidget,
                            QTableWidgetItem, QHeaderView, QMessageBox, QAbstractItemView)
from PyQt5.QtGui import QIcon, QFont, QPixmap, QColor
from PyQt5.QtCore import Qt, QSize

#todo
def GetUserType():
    return 1

def GetUserBalance():
    return 36.99

def UpdateUserBalance(nr):
    pass

cart = {}

class CartPage(QMainWindow):
    def __init__(self, product_data):
        super().__init__()
        self.setWindowTitle("Magazin de produse digitale")
        self.setGeometry(100, 100, 1200, 800)

        self.product_data = product_data
        self.cart = globals().get('cart', {})

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
        widget = QWidget()
        layout = QVBoxLayout()

        widget.setStyleSheet("background: #151515; color: white;")

        table = QTableWidget()
        table.horizontalHeader().setStyleSheet("::section { background: #151515; color: white; }")
        table.verticalHeader().setStyleSheet("::section { background: #151515; color: white; }")
        table.setCornerButtonEnabled(False)

        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(['Name', 'Price', ''])
        table.setSizePolicy(QSizePolicy.Expanding, table.sizePolicy().verticalPolicy())
        table.horizontalHeader().setStretchLastSection(True)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setFixedWidth(800)
        table.setFixedHeight(600)
        table.setStyleSheet("""
        QTableView {
            gridline-color: white;
            alternate-background-color: grey;
            background-color: #1e1e1e;
        }
        QHeaderView::section {
            background-color: grey;
            color: white;
            padding-left: 10px;
            border: 1px solid white;
            font-weight:bold;
        }
        QPushButton {
            background-color: #1e1e1e;
            color: white;
            border: 0px;
        }
        QPushButton:hover {
            font-size: 20px;
        }
        QTableCornerButton::section {
            background-color: #151515;
            border: 1px solid white;
        }
        """)
        table.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setSelectionMode(QAbstractItemView.NoSelection)
        table.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)



        total = float(0)
        for row, (item, price) in enumerate(self.cart.items()):
            name_item = QTableWidgetItem(item)
            name_item.setTextAlignment(Qt.AlignCenter)
            price_item = QTableWidgetItem(str(price))
            price_item.setTextAlignment(Qt.AlignCenter)
            total += float(price)
            delete_button = QPushButton("Delete")
            delete_button.setCursor(Qt.PointingHandCursor)
            delete_button.setStyleSheet("color: red; font-weight: bold;")
            delete_button.clicked.connect(lambda checked, item=item: self.delete_item(item))
            
            table.insertRow(row)
            table.setItem(row, 0, name_item)
            table.setItem(row, 1, price_item)
            table.setCellWidget(row, 2, delete_button)

        layout.addWidget(table, alignment=Qt.AlignCenter)

        total_label = QLabel(f"Total: ${round(total,2)}")
        total_label.setAlignment(Qt.AlignCenter) 
        total_label.setStyleSheet("font-size: 20px;")
        layout.addWidget(total_label, alignment=Qt.AlignCenter)

        buy_button = QPushButton("BUY ALL")
        buy_button.clicked.connect(self.buy_all)
        layout.addWidget(buy_button, alignment=Qt.AlignCenter)
        buy_button.setStyleSheet("background: #0e5b0e; color: white; font-size: 25px; font-weight:bold;")
        buy_button.setFixedSize(150, 60)
        buy_button.setCursor(Qt.PointingHandCursor)

        widget.setLayout(layout)
        if (cart != {}):
            self.setCentralWidget(widget)
        else:
            main_widget = QWidget()
            main_layout = QVBoxLayout(main_widget)

            background = """
            background: #1e1e1e
            """
            self.setStyleSheet("QWidget { background: %s }" % background)
            main_widget.setStyleSheet(background)
            title_label = QLabel("Your cart is empty!")
            title_label.setFont(QFont("Arial", 24))
            title_label.setStyleSheet("color: white; font-weight: bold;")
            title_label.setAlignment(Qt.AlignCenter)

            main_layout.addWidget(title_label)
            self.setCentralWidget(main_widget)

    def delete_item(self, item):
        del self.cart[item]
        self.init_main_layout()
        
    def buy_all(self):
        total = sum(float(value) for value in self.cart.values())
        balance = GetUserBalance()
        if balance >= total:
            UpdateUserBalance(balance - total) 
            self.cart.clear()
            self.init_main_layout()
        else:
            QMessageBox.warning(self, "Not enough balance", "You do not have enough balance to purchase all items.")

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

    def switch_to_wallet(self):
        from WalletPage import WalletPage

        self.wallet_page = WalletPage()
        self.wallet_page.show()
        self.hide()

    