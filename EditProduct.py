import sys
from PyQt5.QtWidgets import (QMainWindow, QCheckBox, QToolBar, QAction, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QComboBox,
                            QScrollArea, QGridLayout, QTextEdit, QFrame, QSizePolicy, QLabel, QListWidget, QStackedLayout, QListWidgetItem,
                            QToolButton)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QSize

#todo
def GetUserType():
    return 1

def GetUserBalance():
    return 36.99

class ImageDropLabel(QListWidget):
    def __init__(self, parent=None, img_list=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

        self.setStyleSheet("""
            border: 4px dashed grey;
            background-color: #151515;
            color: white;
        """)
        self.setResizeMode(QListWidget.Adjust)
        self.setFlow(QListWidget.TopToBottom)
        self.setWrapping(False)
        self.setDragDropMode(QListWidget.InternalMove)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.placeholder = QLabel("Drag images here:", self)
        self.placeholder.setStyleSheet("border: 0px;")
        self.placeholder.setAlignment(Qt.AlignCenter)
        self.placeholder.setVisible(True)
        if img_list is not None:
            self.images_list = img_list
            self.display_images(self.images_list)
        else:
            self.images_list = []

    def display_images(self, img_list):
        self.placeholder.setVisible(False)
        for file_path in img_list:
            file_widget = QWidget()
            file_widget.setStyleSheet("border: 0px;")
            file_widget.file_path = file_path
            file_layout = QHBoxLayout(file_widget)
            file_layout.setAlignment(Qt.AlignCenter)

            file_path_label = QLabel(file_path)
            file_path_label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)

            remove_button = QPushButton('X')
            remove_button.setStyleSheet("""
            QPushButton {
                background-color: red; 
                color: white; 
                width: 15px; 
                height: 15px; 
                font-size: 8px; 
                border-radius: 0;
            }
            """)
            remove_button.setFixedSize(15, 15)
            remove_button.clicked.connect(lambda checked, widget=file_widget: self.remove_image(widget))
            remove_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)

            file_layout.addWidget(file_path_label)
            file_layout.addWidget(remove_button)

            list_item = QListWidgetItem(self)
            list_item.setSizeHint(file_widget.sizeHint())

            self.addItem(list_item)
            self.setItemWidget(list_item, file_widget)
    
    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        if self.images_list:
            self.placeholder.setVisible(False)
        else:
            self.placeholder.setVisible(True)
        
        for url in e.mimeData().urls():
            file_path = str(url.toLocalFile())  
            self.images_list.append(file_path)

            file_widget = QWidget()
            file_widget.setStyleSheet("border: 0px;")
            file_widget.file_path = file_path
            file_layout = QHBoxLayout(file_widget)
            file_layout.setAlignment(Qt.AlignCenter)

            file_path_label = QLabel(file_path)
            file_path_label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)

            remove_button = QPushButton('X')
            remove_button.setStyleSheet("""
            QPushButton {
                background-color: red; 
                color: white; 
                width: 15px; 
                height: 15px; 
                font-size: 8px; 
                border-radius: 0;
            }
            """)
            remove_button.setFixedSize(15, 15)
            remove_button.clicked.connect(lambda checked, widget=file_widget: self.remove_image(widget))
            remove_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)

            file_layout.addWidget(file_path_label)
            file_layout.addWidget(remove_button)

            list_item = QListWidgetItem(self)
            list_item.setSizeHint(file_widget.sizeHint())

            self.addItem(list_item)
            self.setItemWidget(list_item, file_widget)

    
    def remove_image(self, widget):
        file_path = widget.file_path
        for index in range(self.count()):
            if self.itemWidget(self.item(index)) == widget:
                list_item = self.takeItem(index)
                widget.deleteLater()
                self.images_list.remove(file_path)
                del list_item
                break
        if not self.images_list:
            self.placeholder.setVisible(True)


class FileDropLabel(QFrame):
    def __init__(self, parent=None, initial_file=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

        self.setStyleSheet("""
            border: 4px dashed grey;
            background-color: #151515;
            color: white;
        """)
        self.setFixedHeight(100)

        self.placeholder = QLabel("Drag file here:", self)
        self.placeholder.setStyleSheet("border: 0px;")
        self.placeholder.setAlignment(Qt.AlignCenter)

        self.file_widget = None
        self.setLayout(QVBoxLayout())

        if initial_file:
            self.filePath = initial_file
            self.setFile(initial_file)
        else:
            self.filePath = ''

    def setFile(self, file_path):
        self.clear()
        self.filePath = file_path
        self.placeholder.setVisible(False)
        self.file_widget = QWidget()
        self.file_widget.setStyleSheet("border: 0px;")
        self.file_widget.file_path = file_path
        file_layout = QHBoxLayout(self.file_widget)
        file_layout.setAlignment(Qt.AlignCenter)

        file_path_label = QLabel(file_path)
        file_path_label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)

        remove_button = QPushButton('X')
        remove_button.setStyleSheet("""
        QPushButton {
            background-color: red; 
            color: white; 
            width: 15px; 
            height: 15px; 
            font-size: 8px; 
            border-radius: 0;
        }
        """)
        remove_button.setFixedSize(15, 15)
        remove_button.clicked.connect(lambda checked, widget=self.file_widget: self.remove_file(widget))
        remove_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)

        file_layout.addWidget(file_path_label)
        file_layout.addWidget(remove_button)

        self.layout().addWidget(self.file_widget)

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        url = e.mimeData().urls()[0]
        file_path = str(url.toLocalFile())
        self.setFile(file_path)
        self.placeholder.setVisible(False)

    def remove_file(self, widget):
        self.layout().removeWidget(widget)
        self.filePath = ''
        widget.deleteLater()
        self.file_widget = None
        self.placeholder.setVisible(True)

    def clear(self):
        if self.file_widget is not None:
            self.layout().removeWidget(self.file_widget)
            self.file_widget.deleteLater()
        self.file_widget = None

    

class EditProduct(QMainWindow):
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
        main_widget.setStyleSheet("background: #1e1e1e;")

        save_layout = QHBoxLayout()
        save_layout.addStretch()
        self.save_button = QPushButton("Save")
        self.save_button.setCursor(Qt.PointingHandCursor)
        save_layout.addWidget(self.save_button)
        save_layout.addStretch()
        main_layout.addLayout(save_layout)
        self.save_button.setStyleSheet("background: #0e5b0e; color: white; font-size: 25px; font-weight:bold;")
        self.save_button.setFixedSize(150, 60)
        self.save_button.clicked.connect(self.save_product)
        

        input_layout = QGridLayout()
        main_layout.addLayout(input_layout)

        name_label = QLabel("Product Name:")
        name_label.setStyleSheet("color: white;")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Product Name")
        self.name_input.setStyleSheet("color: white;")
        input_layout.addWidget(name_label, 0, 0)
        input_layout.addWidget(self.name_input, 0, 1)

        price_label = QLabel("Price:")
        price_label.setStyleSheet("color: white;")
        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText("Product Price")            
        self.price_input.setStyleSheet("color: white;")
        input_layout.addWidget(price_label, 1, 0)
        input_layout.addWidget(self.price_input, 1, 1)

        if self.product_data is not None:
            self.image_label = ImageDropLabel(self, self.product_data['images'])
        else:
            self.image_label = ImageDropLabel(self)
        main_layout.addWidget(self.image_label)

        self.description_input = QTextEdit()
        self.description_input.setAcceptDrops(False)
        self.description_input.setPlaceholderText("Product Description")
        self.description_input.setStyleSheet("color: white;")
        self.description_input.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.description_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.description_input.setFixedHeight(450)
        main_layout.addWidget(self.description_input)

        if self.product_data:
            self.file_label = FileDropLabel(self, self.product_data['file'])
        else:
            self.file_label = FileDropLabel(self)
        main_layout.addWidget(self.file_label)

        ### EDIT ###
        if self.product_data is not None:
            self.name_input.setText(self.product_data['title'])
            self.price_input.setText(self.product_data['price'])
            self.description_input.setText(self.product_data['description'])


        self.setCentralWidget(main_widget)

    def save_product(self):
        self.product_data = {
            "name": self.name_input.text(),
            "image": self.image_label.images_list,
            "price": self.price_input.text(),
            "description": self.description_input.toPlainText(),
            "file": self.file_label.filePath
        }
        print(self.product_data)

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

    def switch_to_wallet(self):
        from WalletPage import WalletPage

        self.wallet_page = WalletPage()
        self.wallet_page.show()
        self.hide()

    