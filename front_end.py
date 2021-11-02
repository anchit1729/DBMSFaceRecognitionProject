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
        loadUi("login.ui", self)
        self.faceid.clicked.connect(self.gotofaceid)
        self.register_2.clicked.connect(self.gotoregister)
        self.login.clicked.connect(self.gotologin)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
    

    def gotoregister(self):

        t = self.user_name.text()
        password = self.password.text()
        t_value = du.validate_login(t, password)
        if(t_value):
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
        if(len(u)==0 or len(p)==0):
            self.error.setText("Please input all fields!!!!")
        elif(not t_value):
            self.error.setText("Incorrect Password!!!!")
        else:
            customer = Customer(u)
            banker = customer.banker
            self.error.setText("Logged In")
            print("Loggedin")
            self.loggedin = LoginScreen()
            widget.addWidget(self.loggedin)
            widget.setCurrentIndex(widget.currentIndex()+1)
            self.loggedin.name.setText("Name: "+customer.first_name+" "+customer.last_name)
            self.loggedin.address.setText("Address: "+customer.address+" "+customer.address_city)
            self.loggedin.office.setText("Email-Id: "+customer.email)
            self.loggedin.phone.setText("Phone: "+customer.contact_no_1)
            self.loggedin.latestlogin.setText(f"Last login: {customer.last_login}")
            self.loggedin.Custogreeting.setText(f"Welcome back, {customer.salutation}. {customer.last_name}!")
            
            self.loggedin.banker_name.setText("Name: "+banker.first_name+" "+banker.last_name)
            self.loggedin.banker_branch.setText("Branch: "+banker.branch.address)
            self.loggedin.banker_office.setText("Email ID: "+banker.email)
            self.loggedin.banker_phone.setText("Phone Number: "+banker.contact_no)
            self.loggedin.banker_experience.setText(f"Experience: {banker.years_of_experience} year(s)")
            
            self.loggedin.tableWidget.setRowCount(len(customer.account_list))
            self.loggedin.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            
            tablerow = 0
            for account in customer.account_list:
                self.loggedin.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(account.account_summary[0]))
                self.loggedin.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(account.account_summary[1]))
                self.loggedin.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(account.account_summary[2]))
                self.loggedin.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(account.account_summary[3])))
                
                self.loggedin.tableWidget.itemClicked.connect(self.loggedin.handle_account_clicked)
                # self.transaction_screen = TransactionScreen()
                # widget.addWidget(self.transaction_screen)
                # widget.setCurrentIndex(widget.currentIndex()+1)
                
                # acc = Account(account.account_summary[0], u)
                # acc.transaction_list
                
                tablerow+=1
    
    


class LoginScreen(QMainWindow):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("dbms_1200.ui", self)
    
    def handle_account_clicked(self, tableItem):
        print(tableItem.text())
        print(self.tableWidget.item(0, 0).text())
        print(self.tableWidget.item(1, 0).text())
        print(self.tableWidget.rowCount())
        rowCount = self.tableWidget.rowCount()
        for row in range(rowCount):
            if tableItem.text() == self.tableWidget.item(row, 0).text():
                self.gototransaction()
    
    def gototransaction(self):
        self.transaction_screen = TransactionScreen()
        widget.addWidget(self.transaction_screen)
        widget.setCurrentIndex(widget.currentIndex()+1)
        # acc_num = self.tableWidget.itemAt(tablerow, 0)
        # self.transaction_screen = TransactionScreen()
        # widget.addWidget(self.transaction_screen)
        # widget.setCurrentIndex(widget.currentIndex()+1)
                
        # acc = Account(account.account_summary[0], u)
        # acc.transaction_list
        
        
class TransactionScreen(QMainWindow):
    def __init__(self):
        super(TransactionScreen, self).__init__()
        loadUi("transactions_1200.ui", self)
        self.pushButton.clicked.connect(self.backtologin)
        
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