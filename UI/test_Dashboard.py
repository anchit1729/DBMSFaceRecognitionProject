# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1200, 800))
        self.centralwidget.setMaximumSize(QtCore.QSize(1200, 800))
        self.centralwidget.setObjectName("centralwidget")
        self.transactionmenu = QtWidgets.QWidget(self.centralwidget)
        self.transactionmenu.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.transactionmenu.setMinimumSize(QtCore.QSize(1200, 800))
        self.transactionmenu.setMaximumSize(QtCore.QSize(1200, 800))
        self.transactionmenu.setObjectName("transactionmenu")
        self.back = QtWidgets.QLabel(self.transactionmenu)
        self.back.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.back.setMinimumSize(QtCore.QSize(1200, 800))
        self.back.setMaximumSize(QtCore.QSize(1200, 800))
        self.back.setStyleSheet("background-color:rgb(255, 15, 0);")
        self.back.setText("")
        self.back.setPixmap(QtGui.QPixmap("../Images/background.png"))
        self.back.setScaledContents(True)
        self.back.setObjectName("back")
        self.logo = QtWidgets.QLabel(self.transactionmenu)
        self.logo.setGeometry(QtCore.QRect(360, 0, 411, 101))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../Images/logo.png"))
        self.logo.setScaledContents(False)
        self.logo.setObjectName("logo")
        self.profileheading = QtWidgets.QLabel(self.transactionmenu)
        self.profileheading.setGeometry(QtCore.QRect(40, 150, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Ahom")
        font.setPointSize(27)
        font.setBold(False)
        font.setWeight(50)
        self.profileheading.setFont(font)
        self.profileheading.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.profileheading.setStyleSheet("color: white;")
        self.profileheading.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.profileheading.setWordWrap(True)
        self.profileheading.setObjectName("profileheading")
        self.account_table = QtWidgets.QTableWidget(self.transactionmenu)
        self.account_table.setGeometry(QtCore.QRect(90, 480, 991, 211))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.account_table.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Zawgyi")
        font.setPointSize(15)
        self.account_table.setFont(font)
        self.account_table.setAutoFillBackground(False)
        self.account_table.setStyleSheet("\n"
"QHeaderView::section {background-color: transparent;color: white;}\n"
"QTableWidget {background-color: transparent;color: white;}\n"
"QHeaderView {background-color: transparent;color: white;}\n"
"QTableCornerButton::section {background-color: transparent;color: white;}")
        self.account_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.account_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.account_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.account_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.account_table.setAlternatingRowColors(False)
        self.account_table.setShowGrid(True)
        self.account_table.setGridStyle(QtCore.Qt.SolidLine)
        self.account_table.setWordWrap(True)
        self.account_table.setObjectName("account_table")
        self.account_table.setColumnCount(4)
        self.account_table.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.account_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.account_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.account_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.account_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setItem(3, 3, item)
        self.account_table.horizontalHeader().setCascadingSectionResizes(False)
        self.account_table.horizontalHeader().setDefaultSectionSize(240)
        self.account_table.horizontalHeader().setStretchLastSection(True)
        self.account_table_heading = QtWidgets.QLabel(self.transactionmenu)
        self.account_table_heading.setGeometry(QtCore.QRect(450, 390, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Ahom")
        font.setPointSize(35)
        self.account_table_heading.setFont(font)
        self.account_table_heading.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.account_table_heading.setStyleSheet("color: white;")
        self.account_table_heading.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.account_table_heading.setWordWrap(True)
        self.account_table_heading.setObjectName("account_table_heading")
        self.profilebg = QtWidgets.QLabel(self.transactionmenu)
        self.profilebg.setGeometry(QtCore.QRect(20, 134, 511, 221))
        self.profilebg.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(170, 102, 255, 230), stop:0.99999 rgba(90, 91, 255, 240), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;")
        self.profilebg.setText("")
        self.profilebg.setObjectName("profilebg")
        self.phone = QtWidgets.QLabel(self.transactionmenu)
        self.phone.setGeometry(QtCore.QRect(50, 314, 359, 29))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.phone.setFont(font)
        self.phone.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.phone.setStyleSheet("color: white;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.phone.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.phone.setWordWrap(True)
        self.phone.setObjectName("phone")
        self.address = QtWidgets.QLabel(self.transactionmenu)
        self.address.setGeometry(QtCore.QRect(50, 240, 461, 29))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.address.setFont(font)
        self.address.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.address.setStyleSheet("color: white;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.address.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.address.setWordWrap(True)
        self.address.setObjectName("address")
        self.email_id = QtWidgets.QLabel(self.transactionmenu)
        self.email_id.setGeometry(QtCore.QRect(50, 277, 551, 29))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.email_id.setFont(font)
        self.email_id.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.email_id.setStyleSheet("color: white;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.email_id.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.email_id.setWordWrap(True)
        self.email_id.setObjectName("email_id")
        self.name = QtWidgets.QLabel(self.transactionmenu)
        self.name.setGeometry(QtCore.QRect(50, 200, 431, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.name.setFont(font)
        self.name.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.name.setStyleSheet("color: white;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.name.setWordWrap(True)
        self.name.setObjectName("name")
        self.accountbg = QtWidgets.QLabel(self.transactionmenu)
        self.accountbg.setGeometry(QtCore.QRect(20, 380, 1151, 381))
        self.accountbg.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(170, 102, 255, 180), stop:0.99999 rgba(100, 91, 255, 200), stop:1 rgba(255, 255, 255, 200));\n"
"border-radius:20px;")
        self.accountbg.setText("")
        self.accountbg.setObjectName("accountbg")
        self.greeting = QtWidgets.QLabel(self.transactionmenu)
        self.greeting.setGeometry(QtCore.QRect(340, 40, 841, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.greeting.setFont(font)
        self.greeting.setStyleSheet("color: white;\n"
"font: 75 28pt \"MS Shell Dlg 2\";")
        self.greeting.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.greeting.setWordWrap(True)
        self.greeting.setObjectName("greeting")
        self.latest_login = QtWidgets.QLabel(self.transactionmenu)
        self.latest_login.setGeometry(QtCore.QRect(560, 90, 621, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.latest_login.setFont(font)
        self.latest_login.setStyleSheet("color: white;\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.latest_login.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.latest_login.setWordWrap(True)
        self.latest_login.setObjectName("latest_login")
        self.profilebg_2 = QtWidgets.QLabel(self.transactionmenu)
        self.profilebg_2.setGeometry(QtCore.QRect(590, 130, 481, 231))
        self.profilebg_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(170, 102, 255, 230), stop:0.99999 rgba(90, 91, 255, 240), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;")
        self.profilebg_2.setText("")
        self.profilebg_2.setObjectName("profilebg_2")
        self.bankerheading = QtWidgets.QLabel(self.transactionmenu)
        self.bankerheading.setGeometry(QtCore.QRect(610, 150, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Ahom")
        font.setPointSize(27)
        font.setBold(False)
        font.setWeight(50)
        self.bankerheading.setFont(font)
        self.bankerheading.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.bankerheading.setStyleSheet("color: white;")
        self.bankerheading.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bankerheading.setWordWrap(True)
        self.bankerheading.setObjectName("bankerheading")
        self.banker_name = QtWidgets.QLabel(self.transactionmenu)
        self.banker_name.setGeometry(QtCore.QRect(610, 190, 431, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.banker_name.setFont(font)
        self.banker_name.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.banker_name.setStyleSheet("color: white;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.banker_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.banker_name.setWordWrap(True)
        self.banker_name.setObjectName("banker_name")
        self.banker_branch = QtWidgets.QLabel(self.transactionmenu)
        self.banker_branch.setGeometry(QtCore.QRect(610, 230, 461, 29))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.banker_branch.setFont(font)
        self.banker_branch.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.banker_branch.setStyleSheet("color: white;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.banker_branch.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.banker_branch.setWordWrap(True)
        self.banker_branch.setObjectName("banker_branch")
        self.banker_office = QtWidgets.QLabel(self.transactionmenu)
        self.banker_office.setGeometry(QtCore.QRect(610, 260, 551, 29))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.banker_office.setFont(font)
        self.banker_office.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.banker_office.setStyleSheet("color: white;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.banker_office.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.banker_office.setWordWrap(True)
        self.banker_office.setObjectName("banker_office")
        self.banker_phone = QtWidgets.QLabel(self.transactionmenu)
        self.banker_phone.setGeometry(QtCore.QRect(610, 290, 359, 29))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.banker_phone.setFont(font)
        self.banker_phone.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.banker_phone.setStyleSheet("color: white;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.banker_phone.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.banker_phone.setWordWrap(True)
        self.banker_phone.setObjectName("banker_phone")
        self.banker_experience = QtWidgets.QLabel(self.transactionmenu)
        self.banker_experience.setGeometry(QtCore.QRect(610, 320, 359, 29))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.banker_experience.setFont(font)
        self.banker_experience.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.banker_experience.setStyleSheet("color: white;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.banker_experience.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.banker_experience.setWordWrap(True)
        self.banker_experience.setObjectName("banker_experience")
        self.logout = QtWidgets.QPushButton(self.transactionmenu)
        self.logout.setGeometry(QtCore.QRect(20, 20, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.logout.setFont(font)
        self.logout.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(170, 102, 255, 255), stop:0.9999 rgba(100, 91, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color:white;\n"
"border-radius:10px;")
        self.logout.setObjectName("logout")
        self.back.raise_()
        self.logo.raise_()
        self.profilebg.raise_()
        self.profileheading.raise_()
        self.phone.raise_()
        self.address.raise_()
        self.email_id.raise_()
        self.name.raise_()
        self.accountbg.raise_()
        self.account_table_heading.raise_()
        self.account_table.raise_()
        self.greeting.raise_()
        self.latest_login.raise_()
        self.profilebg_2.raise_()
        self.bankerheading.raise_()
        self.banker_name.raise_()
        self.banker_branch.raise_()
        self.banker_office.raise_()
        self.banker_phone.raise_()
        self.banker_experience.raise_()
        self.logout.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.profileheading.setText(_translate("MainWindow", "Profile:"))
        item = self.account_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.account_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.account_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.account_table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.account_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Account ID"))
        item = self.account_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Account Type"))
        item = self.account_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Currency"))
        item = self.account_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Account Balance"))
        __sortingEnabled = self.account_table.isSortingEnabled()
        self.account_table.setSortingEnabled(False)
        item = self.account_table.item(0, 0)
        item.setText(_translate("MainWindow", "251872491802"))
        item = self.account_table.item(0, 1)
        item.setText(_translate("MainWindow", "Savings"))
        item = self.account_table.item(0, 2)
        item.setText(_translate("MainWindow", "USD"))
        item = self.account_table.item(0, 3)
        item.setText(_translate("MainWindow", "1280.00"))
        item = self.account_table.item(1, 0)
        item.setText(_translate("MainWindow", "763592309221"))
        item = self.account_table.item(1, 1)
        item.setText(_translate("MainWindow", "Current"))
        item = self.account_table.item(1, 2)
        item.setText(_translate("MainWindow", "HKD"))
        item = self.account_table.item(1, 3)
        item.setText(_translate("MainWindow", "2378394.03"))
        item = self.account_table.item(2, 0)
        item.setText(_translate("MainWindow", "3178419181958"))
        item = self.account_table.item(2, 1)
        item.setText(_translate("MainWindow", "Current"))
        item = self.account_table.item(2, 2)
        item.setText(_translate("MainWindow", "RMB"))
        item = self.account_table.item(2, 3)
        item.setText(_translate("MainWindow", "134940.34"))
        item = self.account_table.item(3, 0)
        item.setText(_translate("MainWindow", "342738623987"))
        item = self.account_table.item(3, 1)
        item.setText(_translate("MainWindow", "Savings"))
        item = self.account_table.item(3, 2)
        item.setText(_translate("MainWindow", "INR"))
        item = self.account_table.item(3, 3)
        item.setText(_translate("MainWindow", "2222.44"))
        self.account_table.setSortingEnabled(__sortingEnabled)
        self.account_table_heading.setText(_translate("MainWindow", "My Accounts"))
        self.phone.setText(_translate("MainWindow", "Phone Number: 67852 74292"))
        self.address.setText(_translate("MainWindow", "Address: 1209, Schrute Farms, Scranton, PA."))
        self.email_id.setText(_translate("MainWindow", "Email ID: schrutefarms@dundermifflin.com"))
        self.name.setText(_translate("MainWindow", "Name: Dwight K. Schrute"))
        self.greeting.setText(_translate("MainWindow", "Welcome back, username!!"))
        self.latest_login.setText(_translate("MainWindow", "Last login: 29/10/2021 at 03:05:23"))
        self.bankerheading.setText(_translate("MainWindow", "Banker:"))
        self.banker_name.setText(_translate("MainWindow", "Name: Dwight K. Schrute"))
        self.banker_branch.setText(_translate("MainWindow", "Branch: 1209, Schrute Farms, Scranton, PA."))
        self.banker_office.setText(_translate("MainWindow", "Email ID: schrutefarms@dundermifflin.com"))
        self.banker_phone.setText(_translate("MainWindow", "Phone Number: 67852 74292"))
        self.banker_experience.setText(_translate("MainWindow", "Experience:"))
        self.logout.setText(_translate("MainWindow", "Logout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

