import sys
from PyQt5.QtWidgets import (QMainWindow, QCheckBox, QToolBar, QAction, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QComboBox,
                            QScrollArea, QFrame, QSizePolicy, QLabel, QListWidget, QStackedLayout, QListWidgetItem, QToolButton)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QSize

#todo
def GetUserType():
    return 1

def GetUserBalance():
    return 36.99

class LibraryPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Magazin de produse digitale")
        self.setGeometry(100, 100, 1200, 800)

        self.init_tool_bar()
        self.init_main_layout()

        self.app_data = [
        {
            "title": "App1",
            "image": "path/to/app1_image.png",
            "images": ["./login-img.png", "./login-img.png", "./login-img.png", "./login-img.png", "./login-img.png"],
            "description":  """
                Lorem ipsum dipsum dolor sit amet, consectetur adipiscing elit. Cras mollis massa in rhoncus congue. Vestibulum eleifend neque et nulla convallis lacinia. Vivamus iaculis dui id lectus sollicitudin, a dignissim nunc venenatis. Nunc in malesuada nisi. Nam nec est at massa consectetur pharetra. Sed iaculis venenatis eros eget fringilla. Sed euismod risus at urna viverra gravida. Cras mi nisl, semper vitae enim id, pharetra sodales risus. Maecenas pulvinar nisi neque, eget aliquet est rhoncus eget. Nullam convallis metus ac nulla consequat, quis commodo purus consequat. Mauris feugiat nunc eget urna auctor, vel gravida nisi egestas. Pellentesque a metus commodo, elementum augue ut, laoreet diam. Cras scelerisque mollis porta. Aenean sagittis ligula ut urna hendrerit, nec finibus nunc auctor. Aliquam fringilla porta elit, pretium volutpat erat vehicula at. Suspendisse non varius velit.
                ipsum dolor sit amet, consectetur adipiscing elit. Cras mollis massa in rhoncus congue. Vestibulum eleifend neque et nulla convallis lacinia. Vivamus iaculis dui id lectus sollicitudin, a dignissim nunc venenatis. Nunc in malesuada nisi. Nam nec est at massa consectetur pharetra. Sed iaculis venenatis eros eget fringilla. Sed euismod risus at urna viverra gravida. Cras mi nisl, semper vitae enim id, pharetra sodales risus. Maecenas pulvinar nisi neque, eget aliquet est rhoncus eget. Nullam convallis metus ac nulla consequat, quis commodo purus consequat. Mauris feugiat nunc eget urna auctor, vel gravida nisi egestas. Pellentesque a metus commodo, elementum augue ut, laoreet diam. Cras scelerisque mollis porta. Aenean sagittis ligula ut urna hendrerit, nec finibus nunc auctor. Aliquam fringilla porta elit, pretium volutpat erat vehicula at. Suspendisse non varius velit.
                ipsum dolor sit amet, consectetur adipiscing elit. Cras mollis massa in rhoncus congue. Vestibulum eleifend neque et nulla convallis lacinia. Vivamus iaculis dui id lectus sollicitudin, a dignissim nunc venenatis. Nunc in malesuada nisi. Nam nec est at massa consectetur pharetra. Sed iaculis venenatis eros eget fringilla. Sed euismod risus at urna viverra gravida. Cras mi nisl, semper vitae enim id, pharetra sodales risus. Maecenas pulvinar nisi neque, eget aliquet est rhoncus eget. Nullam convallis metus ac nulla consequat, quis commodo purus consequat. Mauris feugiat nunc eget urna auctor, vel gravida nisi egestas. Pellentesque a metus commodo, elementum augue ut, laoreet diam. Cras scelerisque mollis porta. Aenean sagittis ligula ut urna hendrerit, nec finibus nunc auctor. Aliquam fringilla porta elit, pretium volutpat erat vehicula at. Suspendisse non varius velit.
                olor sit amet, consectetur adipiscing elit. Cras mollis massa in rhoncus congue. Vestibulum eleifend neque et nulla convallis lacinia. Vivamus iaculis dui id lectus sollicitudin, a dignissim nunc venenatis. Nunc in malesuada nisi. Nam nec est at massa consectetur pharetra. Sed iaculis venenatis eros eget fringilla. Sed euismod risus at urna viverra gravida. Cras mi nisl, semper vitae enim id, pharetra sodales risus. Maecenas pulvinar nisi neque, eget aliquet est rhoncus eget. Nullam convallis metus ac nulla consequat, quis commodo purus consequat. Mauris feugiat nunc eget urna auctor, vel gravida nisi egestas. Pellentesque a metus commodo, elementum augue ut, laoreet diam. Cras scelerisque mollis porta. Aenean sagittis ligula ut urna hendrerit, nec finibus nunc auctor. Aliquam fringilla porta elit, pretium volutpat erat vehicula at. Suspendisse non varius velit.

                Phasellus eleifend nunc eget scelerisque condimentum. Vestibulum ultrices semper enim, ac sodales nulla mollis vitae. Mauris vel aliquet ante. Sed at ultricies leo. Phasellus quis sapien lorem. Morbi consequat euismod nisl, ut fringilla mi blandit vehicula. Curabitur arcu dui, dignissim at pharetra a, tempus sodales arcu. Nunc vehicula lacus sed est finibus, nec varius ante imperdiet. Aliquam semper libero ante, nec ultrices augue consectetur eu. Sed lacus dolor, pellentesque et commodo sed, tempor eget ipsum. Nulla id bibendum felis, a hendrerit ipsum. Vestibulum porttitor a enim in vestibulum. Aliquam erat volutpat. Nunc mi massa, volutpat eget quam a, auctor lobortis ante. Etiam dictum suscipit ornare. In orci lorem, aliquam at maximus ut, elementum at nisi.""",

            "price": "9.99",
            "category": "Applications"
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
            "title": "Tool1",
            "image": "path/to/app1_image.png",
            "images": ["./login-img.png"],
            "description": "This is a sample tool.",
            "price": "9.99",
            "category": "Tools"
        },
        {
            "title": "App2",
            "image": "path/to/app1_image.png",
            "images": ["./login-img.png", "./login-img.png", "./login-img.png", "./login-img.png", "./login-img.png"],
            "description": "This is a sample application.",
            "price": "9.99",
            "category": "Applications"
        },
        {
            "title": "Game2",
            "image": "path/to/game1_image.png",
            "images": ["./login-img.png", "./login-img.png"],
            "description": "This is a sample game.",
            "price": "19.99",
            "category": "Games"
        },
        {
            "title": "Tool2",
            "image": "path/to/app1_image.png",
            "images": ["./login-img.png"],
            "description": "This is a sample tool.",
            "price": "9.99",
            "category": "Tools"
        },
        ]

        self.update_items()
    
    def init_tool_bar(self):
        tool_bar = QToolBar()

        user_type = GetUserType()

        store_action = QAction("Store", self)
        store_action.triggered.connect(self.switch_to_store)
        
        library_action = QAction("Library", self)
        library_action.setDisabled(True)

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
        init_layout = QHBoxLayout()

        toolbar_layout = QVBoxLayout()
        init_layout.addLayout(toolbar_layout, 1)

        home_button = QPushButton("HOME")
        home_button.setStyleSheet("background-color: #151515; border: #151515; color: white;")
        home_button.setCursor(Qt.PointingHandCursor)
        toolbar_layout.addWidget(home_button)

        category_combo = QComboBox()
        category_combo.addItem("All")
        category_combo.addItem("Applications")
        category_combo.addItem("Games")
        category_combo.addItem("Tools")
        category_combo.currentTextChanged.connect(self.update_items)
        category_combo.setStyleSheet("background-color: #151515; border: #151515; color: white;")
        category_combo.setCursor(Qt.PointingHandCursor)
        toolbar_layout.addWidget(category_combo)

        search_edit = QLineEdit()
        search_edit.setPlaceholderText("Search...")
        search_edit.returnPressed.connect(self.update_items)
        search_edit.setStyleSheet("background-color: #151515; border: #151515; color: white;")
        toolbar_layout.addWidget(search_edit)

        self.item_list = QListWidget()
        self.item_list.itemClicked.connect(self.on_item_clicked)
        self.item_list.setStyleSheet("background-color: #151515; border: transparent; color: white;")
        toolbar_layout.addWidget(self.item_list)

        self.main_content = QStackedLayout()
        init_layout.addLayout(self.main_content, 3)

        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout()
        self.content_widget.setLayout(self.content_layout)

        self.main_content.addWidget(self.content_widget)
        

        main_widget = QWidget()
        main_widget.setLayout(init_layout)

        background = """
        background: #1e1e1e
        """
        self.setStyleSheet("QWidget { background: %s }" % background)
        main_widget.setStyleSheet(background)

        self.setCentralWidget(main_widget)

    def update_items(self):
        search_text = self.findChild(QLineEdit).text()
        category = self.findChild(QComboBox).currentText()

        self.item_list.clear()

        for product in self.app_data:
            title = product.get("title", "")
            product_category = product.get("category", "")
            if (category == "All" or product_category == category) and (search_text.lower() in title.lower()):
                item = QListWidgetItem(title)
                item.setData(Qt.UserRole, product)
                self.item_list.addItem(item)

    def on_item_clicked(self, item):
        item_name = item.text()
        item_data = next((product for product in self.app_data if product.get("title", "") == item_name), {})
        old_widget = self.main_content.widget(0)
        self.main_content.removeWidget(old_widget)
        old_widget.deleteLater()

        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout()
        self.content_layout.setContentsMargins(0, 0, 0, 0) 
        self.content_widget.setLayout(self.content_layout)

        title_label = QLabel(item_name)
        title_label.setStyleSheet("font-weight: bold; font-size: 24px; color: white;")
        title_label.setAlignment(Qt.AlignCenter)
        self.content_layout.addWidget(title_label)
        

        action_button = QPushButton()
        action_button.setIcon(QIcon('./arrow.png'))
        icon_size = QSize(90, 190) 
        action_button.setIconSize(icon_size)
        action_button.setFixedSize(170, 70)
        action_button.setCursor(Qt.PointingHandCursor)
        #-
        info_button = QPushButton()
        info_button.setIcon(QIcon('./info.png'))
        icon_size = QSize(60, 60) 
        info_button.setIconSize(icon_size)
        info_button.setFixedSize(70, 70)
        info_button.setCursor(Qt.PointingHandCursor)
        ##
        app = {}
        for product in self.app_data:
            if product["title"] == item_name:
                app = product
                break
        #
        info_button.clicked.connect(lambda: self.open_product_page(app))

        
        action_button.setStyleSheet("background: #151515; border: 1px solid #b0b0b0;")
        info_button.setStyleSheet("background: #151515; border: 1px solid #b0b0b0;")

        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(info_button)
        #button_layout.addStretch(1)
        button_layout.addWidget(action_button)
        button_layout.addStretch(1)

        button_widget = QWidget()
        button_widget.setLayout(button_layout)

        self.content_layout.addWidget(button_widget)

        ##
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedHeight(300)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        
        scroll_widget = QWidget()
        scroll_layout = QHBoxLayout(scroll_widget)

        for img_path in app["images"]:
            img_label = QLabel()
            pixmap = QPixmap(img_path)
            pixmap = pixmap.scaledToHeight(250)
            img_label.setPixmap(pixmap)
            scroll_layout.addWidget(img_label)

        scroll_area.setWidget(scroll_widget)
        self.content_layout.addWidget(scroll_area)
        ##

        description_label = QLabel(item_data.get("description", ""))
        description_label.setWordWrap(True)
        description_label.setAlignment(Qt.AlignJustify)
        description_label.setStyleSheet("font-size: 16px; color: white; padding: 10px;")

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(description_label)
        #scroll_area.setStyleSheet("border: 0.5px solid #b0b0b0;")
        self.content_layout.addWidget(scroll_area)

        self.main_content.addWidget(self.content_widget)
    
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

    def open_product_page(self, app):
        from ProductPage import ProductPage
        
        self.product_page = ProductPage(app)
        self.product_page.show()
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
    