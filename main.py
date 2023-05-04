from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWebEngineWidgets import *
from SBrowser import SBrowser;

app = QApplication([])
window = SBrowser()

app.exec()