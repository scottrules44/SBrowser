from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
class TabBar(QHBoxLayout):
    tabNum = 0
    activeTab = 0
    tabs = QHBoxLayout()
    browser = None

    def __init__(self, SBrowser) -> None:
        super().__init__()
        self.browser = SBrowser
        self.setSpacing(1) 
        
        self.addLayout(self.tabs)
        addTabButton = QPushButton("+")
        addTabButton.setMaximumWidth(30)
        addTabButton.pressed.connect(lambda: self.addTab("New Tab"))
        self.addWidget(addTabButton)
    
    def tabClicked(self, tabNum):
        if(self.activeTab == tabNum):
            return
        oldActiveTab = self.activeTab
        oldWebsite = self.browser.urlBar.text()
        if oldWebsite == "":
            oldWebsite = "https://google.com"
        for i in range(self.tabNum):
            if i == tabNum:
                self.activeTab = i
                self.tabs.itemAt(i).widget().setChecked(True)
                self.browser.navigate(self.tabs.itemAt(i).widget().objectName, True)
            else:
                if i == oldActiveTab:
                    self.tabs.itemAt(i).widget().objectName = oldWebsite
                self.tabs.itemAt(i).widget().setChecked(False)
            
    def setActiveTabTitle(self, title):
        self.tabs.itemAt(self.activeTab).widget().setText(title)

    def addTab(self, tabName, websiteUrl="https://google.com"):
        self.tabNum += 1
        tabNum = self.tabNum
        self.tab = QPushButton(tabName)
        self.tab.setMinimumHeight(30)
        self.tab.objectName = websiteUrl
        self.tab.setCheckable(True)
        if(self.tabNum == 1):
            self.tab.setChecked(True)
        self.tab.clicked.connect(lambda: self.tabClicked(tabNum-1))
        self.tabs.addWidget(self.tab)
        return tabNum