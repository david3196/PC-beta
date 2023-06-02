import sys
from PyQt5.QtWidgets import (QMainWindow, QCheckBox, QToolBar, QAction, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QComboBox,
                            QScrollArea, QFrame, QSizePolicy, QLabel, QToolButton)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from ProductPage import ProductPage

#todo
def GetUserType():
    return 1

def GetUserBalance():
    return 36.99

class ClickableQFrame(QFrame):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()


class StorePage(QMainWindow):
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
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras mollis massa in rhoncus congue. Vestibulum eleifend neque et nulla convallis lacinia. Vivamus iaculis dui id lectus sollicitudin, a dignissim nunc venenatis. Nunc in malesuada nisi. Nam nec est at massa consectetur pharetra. Sed iaculis venenatis eros eget fringilla. Sed euismod risus at urna viverra gravida. Cras mi nisl, semper vitae enim id, pharetra sodales risus. Maecenas pulvinar nisi neque, eget aliquet est rhoncus eget. Nullam convallis metus ac nulla consequat, quis commodo purus consequat. Mauris feugiat nunc eget urna auctor, vel gravida nisi egestas. Pellentesque a metus commodo, elementum augue ut, laoreet diam. Cras scelerisque mollis porta. Aenean sagittis ligula ut urna hendrerit, nec finibus nunc auctor. Aliquam fringilla porta elit, pretium volutpat erat vehicula at. Suspendisse non varius velit.

                Phasellus eleifend nunc eget scelerisque condimentum. Vestibulum ultrices semper enim, ac sodales nulla mollis vitae. Mauris vel aliquet ante. Sed at ultricies leo. Phasellus quis sapien lorem. Morbi consequat euismod nisl, ut fringilla mi blandit vehicula. Curabitur arcu dui, dignissim at pharetra a, tempus sodales arcu. Nunc vehicula lacus sed est finibus, nec varius ante imperdiet. Aliquam semper libero ante, nec ultrices augue consectetur eu. Sed lacus dolor, pellentesque et commodo sed, tempor eget ipsum. Nulla id bibendum felis, a hendrerit ipsum. Vestibulum porttitor a enim in vestibulum. Aliquam erat volutpat. Nunc mi massa, volutpat eget quam a, auctor lobortis ante. Etiam dictum suscipit ornare. In orci lorem, aliquam at maximus ut, elementum at nisi.""",
            "price": "9.99",
            "category": "Apps"
        },
        {
            "title": "Game1",
            "image": "path/to/game1_image.png",
            "images": ["./login-img.png", "./login-img.png"],
            "description": "This is a sample game.",
            "price": "19.99",
            "category": "Games"
        },
        {
            "title": "App1",
            "image": "path/to/app1_image.png",
            "images": ["./login-img.png"],
            "description": "This is a sample application.",
            "price": "9.99",
            "category": "Apps"
        },
        {
            "title": "Game1",
            "image": "path/to/game1_image.png",
            "images": ["./login-img.png", "./login-img.png", "./login-img.png", "./login-img.png", "./login-img.png"],
            "description": "This is a sample game.",
            "price": "19.99",
            "category": "Games"
        },
        {
            "title": "App1",
            "image": "path/to/app1_image.png",
            "images": ["./login-img.png", "./login-img.png", "./login-img.png", "./login-img.png", "./login-img.png"],
            "description": "This is a sample application.",
            "price": "9.99",
            "category": "Apps"
        },
        {
            "title": "Game2",
            "image": "path/to/game1_image.png",
            "images": ["./login-img.png", "./login-img.png", "./login-img.png", "./login-img.png", "./login-img.png"],
            "description": "This is a sample game.",
            "price": "19.99",
            "category": "Games"
        },
        {
            "title": "App1",
            "image": "login-img.png",
            "images": ["./login-img.png", "./login-img.png", "./login-img.png", "./login-img.png", "./login-img.png"],
            "description": "This is a sample application.",
            "price": "9.99",
            "category": "Apps"
        },
        {
            "title": "Game3",
            "image": "path/to/game1_image.png",
            "images": ["./login-img.png", "./login-img.png", "./login-img.png", "./login-img.png", "./login-img.png"],
            "description": "This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample gameThis is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample gameThis is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game.This is a sample game",
            "price": "19.99",
            "category": "Games"
        },
        ]

        self.init_tool_bar()
        self.init_main_layout()
    
    def init_tool_bar(self):
        tool_bar = QToolBar()

        user_type = GetUserType()
        
        store_action = QAction("Store", self)
        store_action.setDisabled(True)

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


    def on_search_button_clicked(self):
        search_text = self.search_edit.text().lower()
        selected_category = self.category_combo.currentText()

        filtered_apps = [app for app in self.app_data if search_text in app["title"].lower() and app["category"] == selected_category]

        while self.apps_layout.count():
            item = self.apps_layout.takeAt(0)
            item.widget().deleteLater()

        for app in filtered_apps:
            app_widget = self.create_app_widget(app)
            self.apps_layout.addWidget(app_widget)

    def init_main_layout(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        background = """
        background: #1e1e1e
        """
        self.setStyleSheet("QWidget { background: %s }" % background)
        main_widget.setStyleSheet(background)
        
        search_layout = QHBoxLayout()

        search_edit = QLineEdit()
        search_edit.setPlaceholderText("Search...")
        search_edit.setStyleSheet("background-color: #151515; border: #151515; color: white;")
        search_edit.setFixedHeight(30)
        search_layout.addWidget(search_edit)

        search_button = QPushButton("Search")
        search_button.setStyleSheet("background-color: #151515; border: #151515; color: white; padding: 3px;")
        search_button.setFixedSize(70, 30)
        search_layout.addWidget(search_button)

        category_combo = QComboBox()
        category_combo.addItem("Apps")
        category_combo.addItem("Games")
        category_combo.addItem("Tools")
        category_combo.setStyleSheet("background-color: #151515; border: #151515; color: white;")
        category_combo.setFixedSize(70, 30)

        search_layout.addWidget(category_combo)

        search_button.clicked.connect(self.on_search_button_clicked)
        
        main_layout.addLayout(search_layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        apps_widget = QWidget()
        apps_layout = QVBoxLayout(apps_widget)
        
        for app in self.app_data:
            app_widget = self.create_app_widget(app)
            apps_layout.addWidget(app_widget)

        scroll_area.setWidget(apps_widget)
        main_layout.addWidget(scroll_area)

        self.setCentralWidget(main_widget)
        self.search_edit = search_edit
        self.category_combo = category_combo
        self.apps_layout = apps_layout


    def create_app_widget(self, app):
        app_widget = ClickableQFrame()
        app_widget.setFrameShape(QFrame.StyledPanel)
        app_widget.setFrameShadow(QFrame.Raised)
        app_widget.setLineWidth(1)
        app_widget.setStyleSheet("border: 1px solid #CCCCCC;")
        app_widget.clicked.connect(lambda: self.open_product_page(app))
        app_widget.setCursor(Qt.PointingHandCursor)

        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        app_widget.setSizePolicy(size_policy)
        app_widget.setFixedHeight(100)

        app_layout = QHBoxLayout()

        title_label = QLabel(app["title"])
        title_label.setStyleSheet("font-weight: bold; font-size: 18px; border: 0px; color: white;")
        image_label = QLabel()
        image_label.setStyleSheet("border: 0px;")
        pixmap = QPixmap(app["image"])
        image_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))
        description_label = QLabel(app["description"])
        description_label.setWordWrap(True)
        description_label.setStyleSheet("border: 0px; color: white;")

        price_label = QLabel(app["price"])
        price_label.setStyleSheet("font-weight: bold; font-size: 18px; border: 0px; color: white;")

        right_arrow_button = QPushButton()
        right_arrow_button.setIcon(QIcon("next.png"))
        right_arrow_button.setIconSize(QSize(60, 60))
        right_arrow_button.setStyleSheet("font-weight: bold; font-size: 18px; border: 0px; color: white;")

        app_layout.addWidget(image_label)
        app_layout.addWidget(title_label)
        app_layout.addStretch(1)
        app_layout.addWidget(description_label)
        app_layout.addStretch(1)
        app_layout.addWidget(price_label)
        app_layout.addStretch(1)
        app_layout.addWidget(right_arrow_button)

        app_widget.setLayout(app_layout)

        return app_widget
    
    def open_product_page(self, app):
        from ProductPage import ProductPage
        
        self.product_page = ProductPage(app)
        self.product_page.show()
        self.hide()

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
        
    def open_review_page(self):
        from ReviewPage import ReviewPage
        
        self.review_page = ReviewPage(self.product_data)
        self.review_page.show()

