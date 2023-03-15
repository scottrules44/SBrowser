from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

startPage = "https://google.com"

class SBrowser(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.window = QWidget()
        self.window.setWindowTitle("SBrowser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.urlBar = QLineEdit()
        self.urlBar.setMinimumHeight(30)
        self.urlBar.setPlaceholderText("Website Url or Search Param")


        self.goButton = QPushButton("Go")
        self.goButton.setMinimumHeight(30)

        self.reloadButton = QPushButton()
        self.reloadButton.setIcon(QIcon("assets/refresh.png"))
        self.reloadButton.setIconSize(QSize(10,10))
        self.reloadButton.setMinimumHeight(30)

        self.backButton = QPushButton("<")
        self.backButton.setMinimumHeight(30)
        self.fwdButton = QPushButton(">")
        self.fwdButton.setMinimumHeight(30)

        self.horizontal.addWidget(self.urlBar)
        self.horizontal.addWidget(self.goButton)
        self.horizontal.addWidget(self.reloadButton)
        self.horizontal.addWidget(self.backButton)
        self.horizontal.addWidget(self.fwdButton)

        self.goButton.clicked.connect(lambda: self.navigate(self.urlBar.text()))

        self.backButton.setHidden(True)
        self.fwdButton.setHidden(True)

        self.layout.addLayout(self.horizontal)
        self.layout.setContentsMargins(5, 1, 5, 5)

        #Keyboard shortcuts
        self.shortcut = QShortcut(QKeySequence("Ctrl+R"), self.window)

        self.shortcut = QShortcut(QKeySequence("Return"), self.window)
        self.shortcut.activated.connect(self.enterButton)


        self.window.setLayout(self.layout)
        self.window.show()


    def enterButton(self):
        if(self.urlBar.hasFocus):
            QApplication.focusWidget().clearFocus()
            self.navigate(self.urlBar.text())


    def pageFinished(self):
        print("run123")

    def navigate(self, url):
        if not url.startswith("https"):
            url = "https://" + url
            self.urlBar.setText(url)
        self.pageFinished()



app = QApplication([])
window = SBrowser()
app.exec()
