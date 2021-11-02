import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QStackedWidget, QWidget
import face_capture as fc
import train as tr
import faces as fa
import dbutils as du
from dbutils import Account, Banker, Customer, Transaction, Branch


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("UI/Login.ui", self)
        self.faceid.clicked.connect(self.gotofaceid)
        self.register_2.clicked.connect(self.gotoregister)
        self.login.clicked.connect(self.gotologin)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loggedin = None

    def gotoregister(self):

        t = self.user_name.text()
        password = self.password.text()
        t_value = du.validate_login(t, password)
        if (t_value):
            fc.username(t)
            tr.training()
        else:
            self.error.setText("Invalid Login-Id or Password!!!!")

    def gotofaceid(self):

        x = fa.faces()
        print(x)

    def gotologin(self):
        u = self.user_name.text()
        p = self.password.text()
        t_value = du.validate_login(u, p)
        if len(u) == 0 or len(p) == 0:
            self.error.setText("Please input all fields!!!!")
        elif not t_value:
            self.error.setText("Incorrect Password!!!!")
        else:
            self.error.setText("Logged In")
            print("Logged In")
            customer = Customer(u)
            self.loggedin = LoginScreen(customer, customer.banker)
            widget.addWidget(self.loggedin)
            widget.setCurrentIndex(widget.currentIndex() + 1)


class LoginScreen(QMainWindow):
    def __init__(self, customer, banker):
        super(LoginScreen, self).__init__()
        loadUi("UI/Dashboard.ui", self)
        self.customer = customer
        self.banker = banker
        self.name.setText(f"Name: {customer.first_name} {customer.last_name}")
        self.address.setText(f"Address: {customer.address} {customer.address_city}")
        self.office.setText(f"Email-Id: {customer.email}")
        self.phone.setText(f"Phone: {customer.contact_no_1}")
        self.latestlogin.setText(f"Last login: {customer.last_login}")
        self.Custogreeting.setText(f"Welcome back, {customer.salutation}. {customer.last_name}!")

        self.banker_name.setText(f"Name: {banker.first_name} {banker.last_name}")
        self.banker_branch.setText(f"Branch: {banker.branch.address}")
        self.banker_office.setText(f"Email ID: {banker.email}")
        self.banker_phone.setText(f"Phone Number: {banker.contact_no}")
        self.banker_experience.setText(f"Experience: {banker.years_of_experience} year(s)")

        self.tableWidget.setRowCount(len(customer.account_list))
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        tablerow = 0
        for account in customer.account_list:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(account.account_summary[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(account.account_summary[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(account.account_summary[2]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(account.account_summary[3])))

            self.tableWidget.itemClicked.connect(self.handle_account_clicked)
            # self.transaction_screen = TransactionScreen()
            # widget.addWidget(self.transaction_screen)
            # widget.setCurrentIndex(widget.currentIndex()+1)

            # acc = Account(account.account_summary[0], u)
            # acc.transaction_list

            tablerow += 1

    def handle_account_clicked(self, tableItem):
        print(tableItem.text())
        print(self.tableWidget.item(0, 0).text())
        print(self.tableWidget.item(1, 0).text())
        print(self.tableWidget.rowCount())
        rowCount = self.tableWidget.rowCount()
        for row in range(rowCount):
            if tableItem.text() == self.tableWidget.item(row, 0).text():
                self.gototransaction(tableItem.text())

    def gototransaction(self, account_id):
        self.transaction_screen = TransactionScreen(self.customer, account_id)
        widget.addWidget(self.transaction_screen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        # acc_num = self.tableWidget.itemAt(tablerow, 0)
        # self.transaction_screen = TransactionScreen()
        # widget.addWidget(self.transaction_screen)
        # widget.setCurrentIndex(widget.currentIndex()+1)

        # acc = Account(account.account_summary[0], u)
        # acc.transaction_list


class TransactionScreen(QMainWindow):
    def __init__(self, customer, account_id):
        super(TransactionScreen, self).__init__()
        loadUi("UI/TransactionView.ui", self)
        self.pushButton.clicked.connect(self.backtologin)
        self.account_id = account_id
        self.customer = customer
        target_account = None
        for account in customer.account_list:
            if account.account_id == account_id:
                target_account = account
        self.branchName.setText(f"Branch: {target_account.branch.address}")
        self.accountNumber.setText(f"Account No.: {target_account.account_id}")
        self.accountType.setText(f"Account Type: {target_account.account_type}")
        self.accountBalance.setText(f"Balance: {target_account.balance} ({target_account.currency})")
        tablerow = 0
        for transaction in target_account.transaction_list:
            self.transactionTable.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(account.account_summary[0]))
            self.transactionTable.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(account.account_summary[1]))
            self.transactionTable.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(account.account_summary[2]))
            self.transactionTable.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(account.account_summary[3])))

            self.tableWidget.itemClicked.connect(self.handle_account_clicked)


    def backtologin(self):
        widget.removeWidget(self)
        widget.setCurrentIndex(widget.currentIndex() - 1)


app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting app")
