from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtWebEngineWidgets import *

startPage = "https://google.com"

class SBrowser(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.window = QWidget()
        self.window.setWindowTitle("SBrowser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.urlBar = QTextEdit()
        self.urlBar.setMaximumHeight(30)

        self.goButton = QPushButton("Go")     
        self.goButton.setMinimumHeight(30)

        self.reloadButton = QPushButton("r")     
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

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(startPage))

        self.goButton.clicked.connect(lambda: self.navigate(self.urlBar.toPlainText()))
        self.reloadButton.clicked.connect(self.browser.reload)
        self.fwdButton.clicked.connect(self.browser.forward)
        self.backButton.clicked.connect(self.browser.back)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)


        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        if not url.startswith("https"):
            url = "https://" + url
            self.urlBar.setText(url)
        self.browser.setUrl(QUrl(url))
        

app = QApplication([])
window = SBrowser()
app.exec()