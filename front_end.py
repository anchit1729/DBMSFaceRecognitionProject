import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMainWindow, QStackedWidget, QWidget
from PyQt5.QtCore import QTime
import face_capture as fc
import train as tr
import faces as fa
import dbutils as du
from dbutils import Account, Banker, Customer, Transaction, Branch
import fpdf
from copy import deepcopy 
import pdfprinting as pp




class LoginScreen(QDialog):
    def fade(self, widget, duration=1000):
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(duration)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

    def unfade(self, widget, duration=1000):
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(duration)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("UI/Login.ui", self)
        self.faceid.clicked.connect(self.go_to_faceid)
        self.register_label.clicked.connect(self.go_to_register)
        self.login.clicked.connect(self.go_to_dashboard)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.dashboard = None

        try:
            self.fade(LoginScreen, 0)
            self.unfade(LoginScreen, 3000)
        except:
            print('Error in fading animation.')


    def go_to_register(self):
        user_name = self.user_name.text()
        password = self.password.text()
        auth_value = du.validate_login(user_name, password)
        if (auth_value[0]):
            self.error.setText("")
            fc.username(user_name)
            tr.training()
            self.user_name.setText("")
            self.password.setText("")
        else:
            self.error.setText("Invalid Login-Id or Password!!!!")

    def go_to_faceid(self):    
        x = fa.faces()
        user_name = x[0]
        password = du.get_password(user_name)[0]
        result = du.validate_login(user_name, password)
        customer = Customer(user_name, result[1])
        self.dashboard = Dashboard(customer, customer.banker)
        print(x)

    def go_to_dashboard(self):
        user_name = self.user_name.text()
        password = self.password.text()
        auth_value = du.validate_login(user_name, password)
        
        if len(user_name) == 0 or len(password) == 0:
            self.error.setText("Please input all fields!")
        elif not auth_value:
            self.error.setText("Incorrect Login-Id or Password!")
        else:        
            customer = Customer(user_name, auth_value[1])
            self.dashboard = Dashboard(customer, customer.banker)
            self.user_name.setText("")
            self.password.setText("")

class Dashboard(QMainWindow):
    def __init__(self, customer, banker):
        super(Dashboard, self).__init__()
        loadUi("UI/Dashboard.ui", self)
        
        widget.addWidget(self)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        
        self.customer = customer
        self.banker = banker
        self.name.setText(f"Name: {customer.salutation}. {customer.first_name} {customer.last_name}")
        self.dateOfBirth.setText(f"Date of Birth: {customer.date_of_birth}")
        self.address.setText(f"Address: {customer.address} {customer.address_city} {customer.address_state} {customer.address_country} {customer.address_postcode}")
        self.email_id.setText(f"Email-Id: {customer.email}")
        if customer.contact_no_2:
            self.phone.setText(f"Phone: {customer.contact_no_1}, {customer.contact_no_2}")
        else:
            self.phone.setText(f"Phone: {customer.contact_no_1}")
        self.latest_login.setText(f"Last login: {customer.last_login}")
        self.greeting.setText(f"Welcome back, {customer.first_name}!")
        self.banker_name.setText(f"Name: {banker.first_name} {banker.last_name}")
        self.banker_branch.setText(f"Branch: {banker.branch.address}")
        self.banker_office.setText(f"Email ID: {banker.email}")
        self.banker_phone.setText(f"Phone Number: {banker.contact_no}")
        self.banker_experience.setText(f"Experience: {banker.years_of_experience} year(s)")
        self.account_table.setRowCount(len(customer.account_list))
        self.account_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        table_row = 0
        
        for account in customer.account_list:
            self.account_table.setItem(table_row, 0, QtWidgets.QTableWidgetItem(account.account_id))
            self.account_table.setItem(table_row, 1, QtWidgets.QTableWidgetItem(account.account_type))
            self.account_table.setItem(table_row, 2, QtWidgets.QTableWidgetItem(account.currency))
            self.account_table.setItem(table_row, 3, QtWidgets.QTableWidgetItem(f'{account.balance:.2f}'))
            table_row += 1
        
        self.account_table.itemClicked.connect(self.handle_account_clicked)
        self.logout.clicked.connect(self.go_to_login)

    def handle_account_clicked(self, table_item):
        row_count = self.account_table.rowCount()
        
        for row in range(row_count):
            if table_item.text() == self.account_table.item(row, 0).text():
                self.go_to_account_details(table_item.text())
                

    def go_to_account_details(self, account_id):
        self.account_details_screen = AccountDetails(self.customer, account_id)
        
    def go_to_login(self):
        widget.removeWidget(self)


class AccountDetails(QMainWindow):
    def __init__(self, customer, account_id):
        super(AccountDetails, self).__init__()
        loadUi("UI/AccountDetails.ui", self)
        
        widget.addWidget(self)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.file_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.back.clicked.connect(self.back_to_dashboard)
        self.search.clicked.connect(self.search_values)
        self.clear.clicked.connect(self.on_clear)
        self.download_pdf.clicked.connect(self.pdfDownload)
        self.email_pdf.clicked.connect(self.pdfEmail1)
        self.account_id = account_id
        self.customer = customer
        
        self.target_account = None
        
        for account in customer.account_list:
            if account.account_id == self.account_id:
                self.target_account = deepcopy(account)
                break
    
        self.branchName.setText(f"Branch: {self.target_account.branch.address}")
        self.accountNumber.setText(f"Account No.: {self.target_account.account_id} (opened {self.target_account.opening_date})")
        self.accountType.setText(f"Account Type: {self.target_account.account_type}")
        # for savings accounts, only display the interest rates
        if self.target_account.account_type == 'Savings':
            self.overdraftLimit.setText(f"Interest Rate: {self.target_account.interest_rate:.2f}")
            self.dueDate.setText("")
        else:
            self.overdraftLimit.setText(f"Overdraft Limit: {self.target_account.overdraft_limit:.2f} ({self.target_account.overdraft_used:.2f} used)")
            if self.target_account.overdraft_used > 0:
                self.dueDate.setText(f"Due Date: {self.target_account.overdraft_due_date}")
            else:
                self.dueDate.setText("Due Date: NA")

        self.accountBalance.setText(f"Balance: {self.target_account.balance:.2f} ({self.target_account.currency})")

        self.repaint_table(False)
    
    def pdfDownload(self):
        
        if(len(self.file_password.text())==0):
            self.file_error.setText("Please enter password!!")
        else:
            from prettytable import PrettyTable

            x = PrettyTable()

            x.field_names = ["Transaction", "Date", "Time", "Description", "Amount", "Transaction Type"]

            for i in self.target_account.transaction_list:
                x.add_row([str(i.transaction_id), str(i.date_time.date()),str(i.date_time.time()), str(i.transaction_details), f"{i.currency}{i.amount}", str(i.transaction_type)])

            pp.pdfprint(x, self.target_account)
            self.file_error.setText("")
            
            
            from PyPDF2 import PdfFileReader, PdfFileWriter
            pdf_file_path = 'simple_demo.pdf'
            pdfWriter = PdfFileWriter()
            pdf = PdfFileReader(pdf_file_path)

            for page_num in range(pdf.numPages):
                pdfWriter.addPage(pdf.getPage(page_num))
            
            pdfWriter.encrypt(f"{self.file_password.text()}")

            with open(f"{self.target_account.account_id}.pdf", "wb") as out_file:
                    pdfWriter.write(out_file)
                    out_file.close
            import os
            if os.path.exists("simple_demo.pdf"):
                os.remove("simple_demo.pdf")
    
    def pdfEmail1(self):
    
        if(len(self.file_password.text())==0):
            self.file_error.setText("Please enter password!!")
        else:
            from prettytable import PrettyTable

            x = PrettyTable()

            x.field_names = ["Transaction", "Date", "Time", "Description", "Amount", "Transaction Type"]

            for i in self.target_account.transaction_list:
                x.add_row([str(i.transaction_id), str(i.date_time.date()),str(i.date_time.time()), str(i.transaction_details), f"{i.currency}{i.amount:.2f}", str(i.transaction_type)])

            pp.pdfprint(x, self.target_account)

            self.file_error.setText("")
            
            
            from PyPDF2 import PdfFileReader, PdfFileWriter
            pdf_file_path = 'simple_demo.pdf'
            pdfWriter = PdfFileWriter()
            pdf = PdfFileReader(pdf_file_path)

            for page_num in range(pdf.numPages):
                pdfWriter.addPage(pdf.getPage(page_num))
            
            pdfWriter.encrypt(f"{self.file_password.text()}")

            name_file = "account_details"
            with open(f"{name_file}.pdf", "wb") as out_file:
                    pdfWriter.write(out_file)
                    out_file.close

            du.sendPDF(self.customer.email, f"{name_file}.pdf")

            import os
            if os.path.exists("simple_demo.pdf"):
                os.remove("simple_demo.pdf")
                os.remove(f"{name_file}.pdf")
    
    def search_values(self):
        for account in self.customer.account_list:
            if account.account_id == self.account_id:
                self.target_account = deepcopy(account)
                break
        
        time = self.time.time()
        day = self.day.text()
        month = self.month.text()
        year = self.year.text()
        amount = float(self.amount.text())
        
        if time != QTime(0, 0):
            self.target_account.transaction_list = [x for x in self.target_account.transaction_list if QTime(x.date_time.hour, x.date_time.minute) == time]
        if day:
            self.target_account.transaction_list = [x for x in self.target_account.transaction_list if f"{x.date_time.day:02}" == day]
        if month:
            self.target_account.transaction_list = [x for x in self.target_account.transaction_list if f"{x.date_time.month:02}" == month]
        if year:
            self.target_account.transaction_list = [x for x in self.target_account.transaction_list if str(x.date_time.year) == year]
        if amount:
            self.target_account.transaction_list = [x for x in self.target_account.transaction_list if f'{x.amount:.2f}' == f'{amount:.2f}']
        
        self.repaint_table(False)
    
    def on_clear(self):
        time = QTime(0, 0)
        self.time.setTime(time)
        self.day.setText("")
        self.month.setText("")
        self.year.setText("")
        self.amount.setText("")
        self.repaint_table(True)
    
    def repaint_table(self, reset_flag):
        
        tablerow = 0
        
        if reset_flag:
            for account in self.customer.account_list:
                if account.account_id == self.account_id:
                    self.target_account = deepcopy(account)
                    break
            
        self.transactionTable.setRowCount(len(self.target_account.transaction_list))
        self.transactionTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            
        for transaction in self.target_account.transaction_list:
            self.transactionTable.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(transaction.transaction_id))
            self.transactionTable.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(transaction.date_time.date())))
            self.transactionTable.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(transaction.date_time.time())))
            self.transactionTable.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(transaction.transaction_details))
            self.transactionTable.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(f"{transaction.currency}{transaction.amount:.2f}"))
            self.transactionTable.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(transaction.transaction_type))
            tablerow += 1
            
        self.transactionTable.itemClicked.connect(self.handle_transaction_clicked)
         
    def handle_transaction_clicked(self, table_item):
        row_count = self.transactionTable.rowCount()
        
        for row in range(row_count):
            if table_item.text() == self.transactionTable.item(row, 0).text():
                self.go_to_transaction_details(table_item.text())
                

    def go_to_transaction_details(self, transaction_id):
        self.transaction_details_screen = TransactionDetails(self.customer, self.account_id, transaction_id)

    def back_to_dashboard(self):
        widget.removeWidget(self)

class TransactionDetails(QMainWindow):
    def __init__(self, customer, account_id, transaction_id):
        super(TransactionDetails, self).__init__()
        loadUi("UI/TransactionDetails.ui", self)
        
        widget.addWidget(self)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.file_password.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.back.clicked.connect(self.back_to_account_details)
        self.download_pdf.clicked.connect(self.pdfExport)
        self.email_pdf.clicked.connect(self.pdfEmail)
        self.account_id = account_id
        self.transaction_id = transaction_id
        self.customer = customer
        
        self.target_account = None
        self.target_transaction = None
        
        for account in customer.account_list:
            if account.account_id == self.account_id:
                self.target_account = deepcopy(account)
                break
        
        for transaction in self.target_account.transaction_list:
            if transaction.transaction_id == self.transaction_id:
                self.target_transaction = deepcopy(transaction)
                break
    
        self.transactionID.setText(f"Transaction ID: {self.transaction_id}")
        self.accountID.setText(f"Account No.: {self.account_id}")
        self.transactionDetails.setText(f"Transaction Details: {self.target_transaction.transaction_details}")
        self.transactionType.setText(f"Transaction Type: {self.target_transaction.transaction_type}")
        self.amount.setText(f"Amount: {self.target_transaction.amount:.2f}")
        self.currency.setText(f"Currency: {self.target_transaction.currency}")
        self.time.setText(f"Time: {self.target_transaction.date_time}")
        self.remarks.setText(f"Remarks: {self.target_transaction.remarks}")

    def back_to_account_details(self):
        widget.removeWidget(self)

    def pdfExport(self):
        if(len(self.file_password.text())==0):
            self.file_error.setText("Please enter password!!")
        else:
            self.file_error.setText("")
            pdf = fpdf.FPDF(format='letter') #pdf format
            pdf.add_page() #create new page
            pdf.set_font("Arial", size=12) # font and textsize

            pdf.image("Images/bestbanklogo.jpg", x=pdf.w/3, y=0, w=pdf.w/3, h=pdf.w/11 )
            pdf.cell(200, 10, txt="", ln=1, align="L")
            pdf.cell(200, 10, txt="", ln=2, align="L")
            pdf.cell(200, 10, txt=f"Transaction ID: {self.transaction_id}", ln=3, align="L")
            pdf.cell(200, 10, txt=f"Account No.: {self.account_id}", ln=4, align="L")
            pdf.cell(200, 10, txt=f"Transaction Details: {self.target_transaction.transaction_details}", ln=5, align="L")
            pdf.cell(200, 10, txt=f"Transaction Type: {self.target_transaction.transaction_type}", ln=6, align="L")
            pdf.cell(200, 10, txt=f"Amount: {self.target_transaction.amount:.2f}", ln=7, align="L")
            pdf.cell(200, 10, txt=f"Currency: {self.target_transaction.currency}", ln=8, align="L")
            pdf.cell(200, 10, txt=f"Time: {self.target_transaction.date_time}", ln=9, align="L")
            pdf.cell(200, 10, txt=f"Remarks: {self.target_transaction.remarks}", ln=10, align="L")
            pdf.output("test.pdf")
            
            from PyPDF2 import PdfFileReader, PdfFileWriter
            pdf_file_path = 'test.pdf'
            pdfWriter = PdfFileWriter()
            pdf = PdfFileReader(pdf_file_path)

            for page_num in range(pdf.numPages):
                pdfWriter.addPage(pdf.getPage(page_num))
            
            pdfWriter.encrypt(f"{self.file_password.text()}")

            with open(f"{self.transaction_id}.pdf", "wb") as out_file:
                    pdfWriter.write(out_file)
                    out_file.close
            import os
            if os.path.exists("test.pdf"):
                os.remove("test.pdf")

    def pdfEmail(self):
        if(len(self.file_password.text())==0):
            self.file_error.setText("Please enter password!!")
        else:
            self.file_error.setText("")
            pdf = fpdf.FPDF(format='letter') #pdf format
            pdf.add_page() #create new page
            pdf.set_font("Arial", size=12) # font and textsize

            pdf.image("Images/bestbanklogo.jpg", x=pdf.w/3, y=0, w=pdf.w/3, h=pdf.w/11 )
            pdf.cell(200, 10, txt="", ln=1, align="L")
            pdf.cell(200, 10, txt="", ln=2, align="L")
            pdf.cell(200, 10, txt=f"Transaction ID: {self.transaction_id}", ln=3, align="L")
            pdf.cell(200, 10, txt=f"Account No.: {self.account_id}", ln=4, align="L")
            pdf.cell(200, 10, txt=f"Transaction Details: {self.target_transaction.transaction_details}", ln=5, align="L")
            pdf.cell(200, 10, txt=f"Transaction Type: {self.target_transaction.transaction_type}", ln=6, align="L")
            pdf.cell(200, 10, txt=f"Amount: {self.target_transaction.amount:.2f}", ln=7, align="L")
            pdf.cell(200, 10, txt=f"Currency: {self.target_transaction.currency}", ln=8, align="L")
            pdf.cell(200, 10, txt=f"Time: {self.target_transaction.date_time}", ln=9, align="L")
            pdf.cell(200, 10, txt=f"Remarks: {self.target_transaction.remarks}", ln=10, align="L")
            pdf.output("test.pdf")
            
            from PyPDF2 import PdfFileReader, PdfFileWriter
            pdf_file_path = 'test.pdf'
            pdfWriter = PdfFileWriter()
            pdf = PdfFileReader(pdf_file_path)

            for page_num in range(pdf.numPages):
                pdfWriter.addPage(pdf.getPage(page_num))
            
            pdfWriter.encrypt(f"{self.file_password.text()}")
            x = "Transaction_email"
            with open(f"{x}.pdf", "wb") as out_file:
                    pdfWriter.write(out_file)
                    out_file.close
            
            du.sendPDF(self.customer.email, f"{x}.pdf")

            import os
            if os.path.exists("test.pdf"):
                os.remove("test.pdf")
                os.remove(f"{x}.pdf")


app = QApplication(sys.argv)
login_screen = LoginScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(login_screen)
widget.setCurrentIndex(widget.currentIndex() + 1)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting app")
