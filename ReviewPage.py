import sys
from PyQt5.QtWidgets import (QMainWindow, QCheckBox, QToolBar, QAction, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QComboBox,
                            QScrollArea, QFrame, QSizePolicy, QLabel, QListWidget, QStackedLayout, QListWidgetItem, QButtonGroup, QTextEdit)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QSize


class ReviewPage(QMainWindow):
    def __init__(self, product_data):
        super().__init__()
        self.reviews = [
            {'username': 'User1', 'stars': 5, 'text': 'Great app, really useful and easy to use.'},
            {'username': 'User2', 'stars': 4, 'text': 'Good app, but could use some additional features.'},
            {'username': 'User3', 'stars': 3, 'text': 'Average app, nothing special but not bad either.'},
            {'username': 'User4', 'stars': 2, 'text': 'Not a fan of this app, it has many bugs.'},
            {'username': 'User5', 'stars': 1, 'text': 'I would not recommend this app, it crashes frequently.'},
            {'username': 'User6', 'stars': 5, 'text': 'Fantastic app! I use it every day.'},
            {'username': 'User7', 'stars': 4, 'text': 'Overall a solid app, but could be improved.'},
            {'username': 'User8', 'stars': 3, 'text': 'It does what it says, but lacks polish.'},
            {'username': 'User9', 'stars': 2, 'text': 'Has potential, but needs a lot of work.'}, 
            {'username': 'User10', 'stars': 1, 'text': 'Disappointing. I expected more from this app.Disappointing. Disappointing. Disappointing. Disappointing. Disappointing.Disap pointing.Disapp ointing. Disappointing.Dis appoin ting.Disappointing.Disapp ointing.Disappoint ing.Disappointing.Disappoin ting.Disappointing.Disapp ointing.'}
        ]

        self.setWindowTitle("Magazin de produse digitale")
        self.setGeometry(100, 100, 600, 600)

        self.product_data = product_data
        self.init_main_layout()

    
    def init_main_layout(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)

        background = """
        background: #1e1e1e
        """
        self.setStyleSheet("QWidget { background: %s }" % background)
        main_widget.setStyleSheet(background)

        title_label = QLabel("Reviews for "+ self.product_data["title"])
        title_label.setFont(QFont("Arial", 20))
        title_label.setStyleSheet("color: white; font-weight: bold;")
        title_label.setAlignment(Qt.AlignCenter)

        self.star_layout = QHBoxLayout(self)
        self.star_layout.addStretch(1)

        self.star_full_icon = QIcon('star_full.png')
        self.star_empty_icon = QIcon('star_empty.png')

        self.star_buttons = []
        for i in range(5):
            button = QPushButton()
            button.setIcon(self.star_empty_icon)
            button.setFixedSize(50, 50)
            button.setStyleSheet("border: 0px;")
            button.setCheckable(True)
            self.star_buttons.append(button)
            self.star_layout.addWidget(button)
        
        self.star_layout.addStretch(1)

        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True)
        for i, button in enumerate(self.star_buttons):
            self.button_group.addButton(button, i)

        self.button_group.buttonClicked[int].connect(self.update_stars)
        self.rating = 0 #+1

        main_layout.addWidget(title_label)
        main_layout.addLayout(self.star_layout)

        self.comment_area = QTextEdit()
        self.comment_area.setPlaceholderText("Your review...")
        self.comment_area.setFixedHeight(70)
        self.comment_area.setStyleSheet("color: white;")
        main_layout.addWidget(self.comment_area)

        submit_layout = QHBoxLayout(self)
        submit_layout.addStretch(1)
        self.submit_button = QPushButton("ADD REVIEW")
        self.submit_button.setCursor(Qt.PointingHandCursor)
        self.submit_button.clicked.connect(self.submit_review)
        self.submit_button.setStyleSheet("background: #a68c02; color: white; font-size: 17px; font-weight: bold;")
        self.submit_button.setFixedSize(130, 50)
        submit_layout.addWidget(self.submit_button)
        submit_layout.addStretch(1)
        main_layout.addLayout(submit_layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        apps_widget = QWidget()
        apps_layout = QVBoxLayout(apps_widget)
        
        for review  in self.reviews:
            review_widget = self.create_review_widget(review)
            apps_layout.addWidget(review_widget)

        scroll_area.setWidget(apps_widget)
        main_layout.addWidget(scroll_area)

        self.setCentralWidget(main_widget)

    def update_stars(self, id):
        self.rating = id + 1
        for i, button in enumerate(self.star_buttons):
            button.setIcon(self.star_full_icon if i <= id else self.star_empty_icon)

    def submit_review(self):
        not_already_submited = 1
        if self.rating > 0 and not_already_submited:
            comment = self.comment_area.toPlainText()
            print("Stars: " + str(self.rating) + "  " + comment)
    
    def create_review_widget(self, review):
        review_widget = QWidget()
        review_layout = QVBoxLayout(review_widget)

        username_label = QLabel(review["username"] + ":")
        username_label.setFont(QFont("Arial", 12))
        username_label.setStyleSheet("color: black; font-weight: bold;")
        
        stars_label = QLabel("⭐" * review["stars"])
        stars_label.setFont(QFont("Arial", 14))
        stars_label.setStyleSheet("color: gold;")

        text_label = QLabel(review["text"])
        text_label.setWordWrap(True)
        comment_font = QFont("Arial", 12)
        comment_font.setItalic(True) 
        text_label.setFont(comment_font)
        text_label.setStyleSheet("color: black;")
        
        review_layout.addWidget(username_label)
        review_layout.addWidget(stars_label)
        review_layout.addWidget(text_label)

        review_widget.setStyleSheet("background-color: lightgray; border-radius: 10px; padding: 10px;")

        return review_widget

