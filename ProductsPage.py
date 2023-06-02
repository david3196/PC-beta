import sys
from PyQt5.QtWidgets import (QMainWindow, QCheckBox, QToolBar, QAction, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QComboBox,
                            QScrollArea, QFrame, QSizePolicy, QLabel, QListWidget, QStackedLayout, QListWidgetItem, QToolButton)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QSize, pyqtSignal

#todo
def GetUserType():
    return 1

def GetUserBalance():
    return 36.99

class ClickableQFrame(QFrame):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()

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
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras mollis massa in rhoncus congue. Vestibulum eleifend neque et nulla convallis lacinia. Vivamus iaculis dui id lectus sollicitudin, a dignissim nunc venenatis. Nunc in malesuada nisi. Nam nec est at massa consectetur pharetra. Sed iaculis venenatis eros eget fringilla. Sed euismod risus at urna viverra gravida. Cras mi nisl, semper vitae enim id, pharetra sodales risus. Maecenas pulvinar nisi neque, eget aliquet est rhoncus eget. Nullam convallis metus ac nulla consequat, quis commodo purus consequat. Mauris feugiat nunc eget urna auctor, vel gravida nisi egestas. Pellentesque a metus commodo, elementum augue ut, laoreet diam. Cras scelerisque mollis porta. Aenean sagittis ligula ut urna hendrerit, nec finibus nunc auctor. Aliquam fringilla porta elit, pretium volutpat erat vehicula at. Suspendisse non varius velit.",
            "images": ["D:\images\img1.jpg","D:\images\img2.jpg","D:\images\img3.jpg","D:\images\img4.jpg"],
            "file": "D:\\apps\\app1.exe"
            },
            {
            "title": "Game1",
            "price": "10",
            "revenue": "500",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras mollis massa in rhoncus congue. Vestibulum eleifend neque et nulla convallis lacinia. Vivamus iaculis dui id lectus sollicitudin, a dignissim nunc venenatis. Nunc in malesuada nisi. Nam nec est at massa consectetur pharetra. Sed iaculis venenatis eros eget fringilla. Sed euismod risus at urna viverra gravida. Cras mi nisl, semper vitae enim id, pharetra sodales risus. Maecenas pulvinar nisi neque, eget aliquet est rhoncus eget. Nullam convallis metus ac nulla consequat, quis commodo purus consequat. Mauris feugiat nunc eget urna auctor, vel gravida nisi egestas. Pellentesque a metus commodo, elementum augue ut, laoreet diam. Cras scelerisque mollis porta. Aenean sagittis ligula ut urna hendrerit, nec finibus nunc auctor. Aliquam fringilla porta elit, pretium volutpat erat vehicula at. Suspendisse non varius velit.",
            "images": ["D:\images\img1.jpg","D:\images\img2.jpg","D:\images\img3.jpg","D:\images\img4.jpg"],
            "file": "D:\\apps\\app1.exe"
            },
            {
            "title": "Tool1",
            "price": "30",
            "revenue": "300",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras mollis massa in rhoncus congue. Vestibulum eleifend neque et nulla convallis lacinia. Vivamus iaculis dui id lectus sollicitudin, a dignissim nunc venenatis. Nunc in malesuada nisi. Nam nec est at massa consectetur pharetra. Sed iaculis venenatis eros eget fringilla. Sed euismod risus at urna viverra gravida. Cras mi nisl, semper vitae enim id, pharetra sodales risus. Maecenas pulvinar nisi neque, eget aliquet est rhoncus eget. Nullam convallis metus ac nulla consequat, quis commodo purus consequat. Mauris feugiat nunc eget urna auctor, vel gravida nisi egestas. Pellentesque a metus commodo, elementum augue ut, laoreet diam. Cras scelerisque mollis porta. Aenean sagittis ligula ut urna hendrerit, nec finibus nunc auctor. Aliquam fringilla porta elit, pretium volutpat erat vehicula at. Suspendisse non varius velit.",
            "images": ["D:\images\img1.jpg","D:\images\img2.jpg","D:\images\img3.jpg","D:\images\img4.jpg"],
            "file": "D:\\apps\\app1.exe"
            },
            {
            "title": "App2",
            "price": "10",
            "revenue": "100",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras mollis massa in rhoncus congue. Vestibulum eleifend neque et nulla convallis lacinia. Vivamus iaculis dui id lectus sollicitudin, a dignissim nunc venenatis. Nunc in malesuada nisi. Nam nec est at massa consectetur pharetra. Sed iaculis venenatis eros eget fringilla. Sed euismod risus at urna viverra gravida. Cras mi nisl, semper vitae enim id, pharetra sodales risus. Maecenas pulvinar nisi neque, eget aliquet est rhoncus eget. Nullam convallis metus ac nulla consequat, quis commodo purus consequat. Mauris feugiat nunc eget urna auctor, vel gravida nisi egestas. Pellentesque a metus commodo, elementum augue ut, laoreet diam. Cras scelerisque mollis porta. Aenean sagittis ligula ut urna hendrerit, nec finibus nunc auctor. Aliquam fringilla porta elit, pretium volutpat erat vehicula at. Suspendisse non varius velit.",
            "images": ["D:\images\img1.jpg","D:\images\img2.jpg","D:\images\img3.jpg","D:\images\img4.jpg"],
            "file": "D:\\apps\\app1.exe"
            },
            {
            "title": "Game2",
            "price": "20",
            "revenue": "400",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras mollis massa in rhoncus congue. Vestibulum eleifend neque et nulla convallis lacinia. Vivamus iaculis dui id lectus sollicitudin, a dignissim nunc venenatis. Nunc in malesuada nisi. Nam nec est at massa consectetur pharetra. Sed iaculis venenatis eros eget fringilla. Sed euismod risus at urna viverra gravida. Cras mi nisl, semper vitae enim id, pharetra sodales risus. Maecenas pulvinar nisi neque, eget aliquet est rhoncus eget. Nullam convallis metus ac nulla consequat, quis commodo purus consequat. Mauris feugiat nunc eget urna auctor, vel gravida nisi egestas. Pellentesque a metus commodo, elementum augue ut, laoreet diam. Cras scelerisque mollis porta. Aenean sagittis ligula ut urna hendrerit, nec finibus nunc auctor. Aliquam fringilla porta elit, pretium volutpat erat vehicula at. Suspendisse non varius velit.",
            "images": ["D:\images\img1.jpg","D:\images\img2.jpg","D:\images\img3.jpg","D:\images\img4.jpg"],
            "file": "D:\\apps\\app1.exe"
            },
            {
            "title": "Tool2",
            "price": "30",
            "revenue": "400",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras mollis massa in rhoncus congue. Vestibulum eleifend neque et nulla convallis lacinia. Vivamus iaculis dui id lectus sollicitudin, a dignissim nunc venenatis. Nunc in malesuada nisi. Nam nec est at massa consectetur pharetra. Sed iaculis venenatis eros eget fringilla. Sed euismod risus at urna viverra gravida. Cras mi nisl, semper vitae enim id, pharetra sodales risus. Maecenas pulvinar nisi neque, eget aliquet est rhoncus eget. Nullam convallis metus ac nulla consequat, quis commodo purus consequat. Mauris feugiat nunc eget urna auctor, vel gravida nisi egestas. Pellentesque a metus commodo, elementum augue ut, laoreet diam. Cras scelerisque mollis porta. Aenean sagittis ligula ut urna hendrerit, nec finibus nunc auctor. Aliquam fringilla porta elit, pretium volutpat erat vehicula at. Suspendisse non varius velit.",
            "images": ["D:\images\img1.jpg","D:\images\img2.jpg","D:\images\img3.jpg","D:\images\img4.jpg"],
            "file": "D:\\apps\\app1.exe"
            },     
        ]

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

        post_new_widget = ClickableQFrame()
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
        post_new_widget.clicked.connect(lambda: self.open_edit_page(None))
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
        edit_button.clicked.connect(lambda: self.open_edit_page(app))

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

    def open_edit_page(self, app):
        from EditProduct import EditProduct
        
        self.product_page = EditProduct(app)
        self.product_page.show()
        self.hide()

