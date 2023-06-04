from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWebEngineWidgets import *
import darkdetect
from TabBar import TabBar
import re

startPage = "https://www.google.com/"
iconTheme = "" if darkdetect.isLight() else "_dark"

def checkIfUrl(text) -> bool:
    if re.search("[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", text):
        return True
    return False

class SBrowser(QMainWindow):
    tabs = 0

    def __init__(self) -> None:
        tabs = 1
        super().__init__()
        self.window = QWidget()
        self.window.setWindowTitle("SBrowser")

        self.layout = QVBoxLayout()

        self.toolbar = QHBoxLayout()
        self.toolbar.setSpacing(1)

        self.tabBar = TabBar(self)
        self.tabBar.addTab("Hompage")

        self.urlBar = QLineEdit()
        self.urlBar.setMinimumHeight(30)
        self.urlBar.setPlaceholderText("Website Url or Search Param")

        self.goButton = QPushButton("Go")
        self.goButton.setMinimumHeight(30)

        self.reloadButton = QPushButton()
        self.reloadButton.setIcon(QIcon("assets/refresh"+iconTheme+".png"))
        self.reloadButton.setIconSize(QSize(10,10))
        self.reloadButton.setMinimumHeight(30)

        self.backButton = QPushButton("<")
        self.backButton.setMinimumHeight(30)
        self.fwdButton = QPushButton(">")
        self.fwdButton.setMinimumHeight(30)

        self.toolbar.addWidget(self.urlBar)
        self.toolbar.addWidget(self.goButton)
        self.toolbar.addWidget(self.reloadButton)
        self.toolbar.addWidget(self.backButton)
        self.toolbar.addWidget(self.fwdButton)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(startPage))
        self.browser.loadFinished.connect(self.pageFinished)

        self.goButton.clicked.connect(lambda: self.navigate(self.urlBar.text()))
        self.reloadButton.clicked.connect(self.browser.reload)
        self.fwdButton.clicked.connect(self.browser.forward)
        self.backButton.clicked.connect(self.browser.back)

        self.backButton.setHidden(True)
        self.fwdButton.setHidden(True)

        self.layout.addLayout(self.toolbar)
        self.layout.addLayout(self.tabBar)
        self.layout.addWidget(self.browser)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(5, 0, 5, 1)

        #Keyboard shortcuts
        self.shortcut = QShortcut(QKeySequence("Ctrl+R"), self.window)
        self.shortcut.activated.connect(self.browser.reload)

        self.shortcut = QShortcut(QKeySequence("Return"), self.window)
        self.shortcut.activated.connect(self.enterButton)
        

        self.window.setLayout(self.layout)
        self.window.show()


    def enterButton(self):
        if(self.urlBar.hasFocus):
            QApplication.focusWidget().clearFocus()
            self.navigate(self.urlBar.text())

    def pageFinished(self):
        if(startPage != self.browser.page().url().toString()):
            self.urlBar.setText(self.browser.page().url().toString())
        else:
            self.urlBar.setText("")
        self.tabBar.setActiveTabTitle(self.browser.page().title())
        self.backButton.setHidden(not self.browser.history().canGoBack())
        self.fwdButton.setHidden(not self.browser.history().canGoForward())

    def navigate(self, url, override=False):
        if((checkIfUrl(url) and not url.startswith("https")) and override == False):
            url = "https://" + url
            self.urlBar.setText(url)
        elif not checkIfUrl(url) and override == False:
            url = "https://google.com/search?q=" + url.replace(" ", "+")
            self.urlBar.setText(url)
        self.browser.setUrl(QUrl(url))
        self.pageFinished()