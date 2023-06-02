import sys
from PyQt5.QtWidgets import (QMainWindow, QCheckBox, QToolBar, QAction, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QComboBox,
                            QScrollArea, QFrame, QSizePolicy, QLabel, QListWidget, QStackedLayout, QListWidgetItem, QToolButton)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QSize, pyqtSignal

def GetUserType():
    return 1

def GetUserBalance():
    return 36.99

class ClickableQFrame(QFrame):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()

class ManagementPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Magazin de produse digitale")
        self.setGeometry(100, 100, 1200, 800)

        self.app_data = [
        {
            "title": "App1",
            "image": "path/to/app1_image.png",
            "images": ["./login-img.png", "./login-img.png", "./login-img.png", "./login-img.png", "./login-img.png"],
            "description": """
                Lorem ipsum dolor s sit amet, consectetur adipiscing elit. Cras mollis massa in rhoncus congue. Vestibulum eleifend neque et nulla convallis lacinia. Vivamus iaculis dui id lectus sollicitudin, a dignissim nunc venenatis. Nunc in malesuada nisi. Nam nec est at massa consectetur pharetra. Sed iaculis venenatis eros eget fringilla. Sed euismod risus at urna viverra gravida. Cras mi nisl, semper vitae enim id, pharetra sodales risus. Maecenas pulvinar nisi neque, eget aliquet est rhoncus eget. Nullam convallis metus ac nulla consequat, quis commodo purus consequat. Mauris feugiat nunc eget urna auctor, vel gravida nisi egestas. Pellentesque a metus commodo, elementum augue ut, laoreet diam. Cras scelerisque mollis porta. Aenean sagittis ligula ut urna hendrerit, nec finibus nunc auctor. Aliquam fringilla porta elit, pretium volutpat erat vehicula at. Suspendisse non varius velit.
                sit amet, consectetur adipiscing elit. Cras mollis massa in rhoncus congue. Vestibulum eleifend neque et nulla convallis lacinia. Vivamus iaculis dui id lectus sollicitudin, a dignissim nunc venenatis. Nunc in malesuada nisi. Nam nec est at massa consectetur pharetra. Sed iaculis venenatis eros eget fringilla. Sed euismod risus at urna viverra gravida. Cras mi nisl, semper vitae enim id, pharetra sodales risus. Maecenas pulvinar nisi neque, eget aliquet est rhoncus eget. Nullam convallis metus ac nulla consequat, quis commodo purus consequat. Mauris feugiat nunc eget urna auctor, vel gravida nisi egestas. Pellentesque a metus commodo, elementum augue ut, laoreet diam. Cras scelerisque mollis porta. Aenean sagittis ligula ut urna hendrerit, nec finibus nunc auctor. Aliquam fringilla porta elit, pretium volutpat erat vehicula at. Suspendisse non varius velit.
                sit amet, consectetur adipiscing elit. Cras mollis massa in rhoncus congue. Vestibulum eleifend neque et nulla convallis lacinia. Vivamus iaculis dui id lectus sollicitudin, a dignissim nunc venenatis. Nunc in malesuada nisi. Nam nec est at massa consectetur pharetra. Sed iaculis venenatis eros eget fringilla. Sed euismod risus at urna viverra gravida. Cras mi nisl, semper vitae enim id, pharetra sodales risus. Maecenas pulvinar nisi neque, eget aliquet est rhoncus eget. Nullam convallis metus ac nulla consequat, quis commodo purus consequat. Mauris feugiat nunc eget urna auctor, vel gravida nisi egestas. Pellentesque a metus commodo, elementum augue ut, laoreet diam. Cras scelerisque mollis porta. Aenean sagittis ligula ut urna hendrerit, nec finibus nunc auctor. Aliquam fringilla porta elit, pretium volutpat erat vehicula at. Suspendisse non varius velit.
                it amet, consectetur adipiscing elit. Cras mollis massa in rhoncus congue. Vestibulum eleifend neque et nulla convallis lacinia. Vivamus iaculis dui id lectus sollicitudin, a dignissim nunc venenatis. Nunc in malesuada nisi. Nam nec est at massa consectetur pharetra. Sed iaculis venenatis eros eget fringilla. Sed euismod risus at urna viverra gravida. Cras mi nisl, semper vitae enim id, pharetra sodales risus. Maecenas pulvinar nisi neque, eget aliquet est rhoncus eget. Nullam convallis metus ac nulla consequat, quis commodo purus consequat. Mauris feugiat nunc eget urna auctor, vel gravida nisi egestas. Pellentesque a metus commodo, elementum augue ut, laoreet diam. Cras scelerisque mollis porta. Aenean sagittis ligula ut urna hendrerit, nec finibus nunc auctor. Aliquam fringilla porta elit, pretium volutpat erat vehicula at. Suspendisse non varius velit.

                Phasellus eleifend nunc eget scelerisque condimentum. Vestibulum ultrices semper enim, ac sodales nulla mollis vitae. Mauris vel aliquet ante. Sed at ultricies leo. Phasellus quis sapien lorem. Morbi consequat euismod nisl, ut fringilla mi blandit vehicula. Curabitur arcu dui, dignissim at pharetra a, tempus sodales arcu. Nunc vehicula lacus sed est finibus, nec varius ante imperdiet. Aliquam semper libero ante, nec ultrices augue consectetur eu. Sed lacus dolor, pellentesque et commodo sed, tempor eget ipsum. Nulla id bibendum felis, a hendrerit ipsum. Vestibulum porttitor a enim in vestibulum. Aliquam erat volutpat. Nunc mi massa, volutpat eget quam a, auctor lobortis ante. Etiam dictum suscipit ornare. In orci lorem, aliquam at maximus ut, elementum at nisi.""",
            "price": "$9.99",
            "category": "Applications",
            "revenue": "800",
            "status": "in review",
            "file": "D://aaa//ok.exe",
            "raport": """
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras mollis massa in rhoncus congue. Vestibulum eleifend neque et nulla convallis lacinia. Vivamus iaculis dui id lectus sollicitudin, a dignissim nunc venenatis. Nunc in malesuada nisi. Nam nec est at massa consectetur pharetra. Sed iaculis venenatis eros eget fringilla. Sed euismod risus at urna viverra gravida. Cras mi nisl, semper vitae enim id, pharetra sodales risus. Maecenas pulvinar nisi neque, eget aliquet est rhoncus eget. Nullam convallis metus ac nulla consequat, quis commodo purus consequat. Mauris feugiat nunc eget urna auctor, vel gravida nisi egestas. Pellentesque a metus commodo, elementum augue ut, laoreet diam. Cras scelerisque mollis porta. Aenean sagittis ligula ut urna hendrerit, nec finibus nunc auctor. Aliquam fringilla porta elit, pretium volutpat erat vehicula at. Suspendisse non varius velit.

                Phasellus eleifend nunc eget scelerisque condimentum. Vestibulum ultrices semper enim, ac sodales nulla mollis vitae. Mauris vel aliquet ante. Sed at ultricies leo. Phasellus quis sapien lorem. Morbi consequat euismod nisl, ut fringilla mi blandit vehicula. Curabitur arcu dui, dignissim at pharetra a, tempus sodales arcu. Nunc vehicula lacus sed est finibus, nec varius ante imperdiet. Aliquam semper libero ante, nec ultrices augue consectetur eu. Sed lacus dolor, pellentesque et commodo sed, tempor eget ipsum. Nulla id bibendum felis, a hendrerit ipsum. Vestibulum porttitor a enim in vestibulum. Aliquam erat volutpat. Nunc mi massa, volutpat eget quam a, auctor lobortis ante. Etiam dictum suscipit ornare. In orci lorem, aliquam at maximus ut, elementum at nisi."""

        },
        {
            "title": "Game1",
            "image": "path/to/game1_image.png",
            "images": ["./login-img.png", "./login-img.png"],
            "description": "This is a sample game.",
            "price": "$19.99",
            "category": "Games",
            "revenue": "300",
            "status": "accepted",
            "file": "D://aaa//ok.exe",
            "raport": """
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras mollis massa in rhoncus congue. Vestibulum eleifend neque et nulla convallis lacinia. Vivamus iaculis dui id lectus sollicitudin, a dignissim nunc venenatis. Nunc in malesuada nisi. Nam nec est at massa consectetur pharetra. Sed iaculis venenatis eros eget fringilla. Sed euismod risus at urna viverra gravida. Cras mi nisl, semper vitae enim id, pharetra sodales risus. Maecenas pulvinar nisi neque, eget aliquet est rhoncus eget. Nullam convallis metus ac nulla consequat, quis commodo purus consequat. Mauris feugiat nunc eget urna auctor, vel gravida nisi egestas. Pellentesque a metus commodo, elementum augue ut, laoreet diam. Cras scelerisque mollis porta. Aenean sagittis ligula ut urna hendrerit, nec finibus nunc auctor. Aliquam fringilla porta elit, pretium volutpat erat vehicula at. Suspendisse non varius velit.

                Phasellus eleifend nunc eget scelerisque condimentum. Vestibulum ultrices semper enim, ac sodales nulla mollis vitae. Mauris vel aliquet ante. Sed at ultricies leo. Phasellus quis sapien lorem. Morbi consequat euismod nisl, ut fringilla mi blandit vehicula. Curabitur arcu dui, dignissim at pharetra a, tempus sodales arcu. Nunc vehicula lacus sed est finibus, nec varius ante imperdiet. Aliquam semper libero ante, nec ultrices augue consectetur eu. Sed lacus dolor, pellentesque et commodo sed, tempor eget ipsum. Nulla id bibendum felis, a hendrerit ipsum. Vestibulum porttitor a enim in vestibulum. Aliquam erat volutpat. Nunc mi massa, volutpat eget quam a, auctor lobortis ante. Etiam dictum suscipit ornare. In orci lorem, aliquam at maximus ut, elementum at nisi."""

        },
        {
            "title": "Tool1",
            "image": "path/to/app1_image.png",
            "images": ["./login-img.png"],
            "description": "This is a sample tool.",
            "price": "$9.99",
            "category": "Tools",
            "revenue": "400",
            "status": "in review",
            "file": "D://aaa//ok.exe",
            "raport": """
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras mollis massa in rhoncus congue. Vestibulum eleifend neque et nulla convallis lacinia. Vivamus iaculis dui id lectus sollicitudin, a dignissim nunc venenatis. Nunc in malesuada nisi. Nam nec est at massa consectetur pharetra. Sed iaculis venenatis eros eget fringilla. Sed euismod risus at urna viverra gravida. Cras mi nisl, semper vitae enim id, pharetra sodales risus. Maecenas pulvinar nisi neque, eget aliquet est rhoncus eget. Nullam convallis metus ac nulla consequat, quis commodo purus consequat. Mauris feugiat nunc eget urna auctor, vel gravida nisi egestas. Pellentesque a metus commodo, elementum augue ut, laoreet diam. Cras scelerisque mollis porta. Aenean sagittis ligula ut urna hendrerit, nec finibus nunc auctor. Aliquam fringilla porta elit, pretium volutpat erat vehicula at. Suspendisse non varius velit.

                Phasellus eleifend nunc eget scelerisque condimentum. Vestibulum ultrices semper enim, ac sodales nulla mollis vitae. Mauris vel aliquet ante. Sed at ultricies leo. Phasellus quis sapien lorem. Morbi consequat euismod nisl, ut fringilla mi blandit vehicula. Curabitur arcu dui, dignissim at pharetra a, tempus sodales arcu. Nunc vehicula lacus sed est finibus, nec varius ante imperdiet. Aliquam semper libero ante, nec ultrices augue consectetur eu. Sed lacus dolor, pellentesque et commodo sed, tempor eget ipsum. Nulla id bibendum felis, a hendrerit ipsum. Vestibulum porttitor a enim in vestibulum. Aliquam erat volutpat. Nunc mi massa, volutpat eget quam a, auctor lobortis ante. Etiam dictum suscipit ornare. In orci lorem, aliquam at maximus ut, elementum at nisi."""

        },
        {
            "title": "App2",
            "image": "path/to/app1_image.png",
            "images": ["./login-img.png", "./login-img.png", "./login-img.png", "./login-img.png", "./login-img.png"],
            "description": "This is a sample application.",
            "price": "$9.99",
            "category": "Applications",
            "revenue": "800",
            "status": "in review",
            "file": "D://aaa//ok.exe",
            "raport": """
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras mollis massa in rhoncus congue. Vestibulum eleifend neque et nulla convallis lacinia. Vivamus iaculis dui id lectus sollicitudin, a dignissim nunc venenatis. Nunc in malesuada nisi. Nam nec est at massa consectetur pharetra. Sed iaculis venenatis eros eget fringilla. Sed euismod risus at urna viverra gravida. Cras mi nisl, semper vitae enim id, pharetra sodales risus. Maecenas pulvinar nisi neque, eget aliquet est rhoncus eget. Nullam convallis metus ac nulla consequat, quis commodo purus consequat. Mauris feugiat nunc eget urna auctor, vel gravida nisi egestas. Pellentesque a metus commodo, elementum augue ut, laoreet diam. Cras scelerisque mollis porta. Aenean sagittis ligula ut urna hendrerit, nec finibus nunc auctor. Aliquam fringilla porta elit, pretium volutpat erat vehicula at. Suspendisse non varius velit.

                Phasellus eleifend nunc eget scelerisque condimentum. Vestibulum ultrices semper enim, ac sodales nulla mollis vitae. Mauris vel aliquet ante. Sed at ultricies leo. Phasellus quis sapien lorem. Morbi consequat euismod nisl, ut fringilla mi blandit vehicula. Curabitur arcu dui, dignissim at pharetra a, tempus sodales arcu. Nunc vehicula lacus sed est finibus, nec varius ante imperdiet. Aliquam semper libero ante, nec ultrices augue consectetur eu. Sed lacus dolor, pellentesque et commodo sed, tempor eget ipsum. Nulla id bibendum felis, a hendrerit ipsum. Vestibulum porttitor a enim in vestibulum. Aliquam erat volutpat. Nunc mi massa, volutpat eget quam a, auctor lobortis ante. Etiam dictum suscipit ornare. In orci lorem, aliquam at maximus ut, elementum at nisi."""

        },
        {
            "title": "Game2",
            "image": "path/to/game1_image.png",
            "images": ["./login-img.png", "./login-img.png"],
            "description": "This is a sample game.",
            "price": "$19.99",
            "category": "Games",
            "revenue": "800",
            "status": "in review",
            "file": "D://aaa//ok.exe",
            "raport": ""
            
        },
        {
            "title": "Tool2",
            "image": "path/to/app1_image.png",
            "images": ["./login-img.png"],
            "description": "This is a sample tool.",
            "price": "$9.99",
            "category": "Tools",
            "revenue": "800",
            "status": "rejected",
            "file": "D://aaa//ok.exe",
            "raport": ""
        },
        {
            "title": "App1",
            "image": "path/to/app1_image.png",
            "images": ["./login-img.png", "./login-img.png", "./login-img.png", "./login-img.png", "./login-img.png"],
            "description": "This is a sample application.",
            "price": "$9.99",
            "category": "Applications",
            "revenue": "800",
            "status": "in review",
            "file": "D://aaa//ok.exe",
            "raport": ""

        },
        {
            "title": "Game1",
            "image": "path/to/game1_image.png",
            "images": ["./login-img.png", "./login-img.png"],
            "description": "This is a sample game.",
            "price": "$19.99",
            "category": "Games",
            "revenue": "300",
            "status": "accepted",
            "file": "D://aaa//ok.exe",
            "raport": ""
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
        management_action.setDisabled(True)

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

        post_new_text = QLabel("New Job")
        post_new_text.setFont(QFont("Arial", 18))
        post_new_text.setStyleSheet("border: 0px; color: white; font-weight:bold;")
        post_new_layout.addWidget(post_new_text)

        post_new_widget.setLayout(post_new_layout)
        post_new_widget.setCursor(Qt.PointingHandCursor)
        post_new_layout.addStretch(1)
        post_new_widget.clicked.connect(lambda: self.open_job_page(self.app_data[0]))
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

        name_and_status_layout = QVBoxLayout()
        name_label = QLabel(app["title"])
        name_label.setStyleSheet("font-weight: bold; font-size: 18px; border: 0px; color: white;")
        name_and_status_layout.addWidget(name_label)

        status_label = QLabel("Status: {}".format(app["status"]))
        status_label.setStyleSheet(" font-size: 18px; border: 0px; color: white;")
        name_and_status_layout.addWidget(status_label)

        price_and_revenue_layout = QVBoxLayout()
        price_label = QLabel("Price: {}".format(app["price"]))
        price_label.setStyleSheet(" font-size: 18px; border: 0px; color: white;")
        price_and_revenue_layout.addWidget(price_label)

        revenue_label = QLabel("Revenue: ${}".format(app["revenue"]))
        revenue_label.setStyleSheet(" font-size: 18px; border: 0px; color: white;")
        price_and_revenue_layout.addWidget(revenue_label)

        raport_label = QPushButton("Raport...")
        raport_label.setStyleSheet("font-size: 18px; color: white; background: #151515;")
        raport_label.setFixedSize(80, 80)
        raport_label.setCursor(Qt.PointingHandCursor)
        raport_label.clicked.connect(lambda: self.open_raport_page(app))

        product_layout.addLayout(name_and_status_layout)
        product_layout.addStretch(1)
        product_layout.addLayout(price_and_revenue_layout)
        product_layout.addStretch(4)
        product_layout.addWidget(raport_label)
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
    
    def open_raport_page(self, app):
        from RaportPage import RaportPage
        
        self.raport_page = RaportPage(app)
        self.raport_page.show()

    def open_job_page(self, app):
        from JobPage import JobPage
        
        self.job_page = JobPage(app)
        self.job_page.show()
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

    def switch_to_products(self):
        from ProductsPage import ProductsPage

        self.products_page = ProductsPage()
        self.products_page.show()
        self.hide()