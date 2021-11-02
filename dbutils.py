import mysql.connector
from datetime import datetime
import smtplib
import ssl
from email.mime.text import MIMEText

# Make a connection to the local database
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Raghav@2001',
    database='banking_application'
)

# Define a port for SSL
port = 465
email_password = 'pottermore'
email_id = 'bestbank1729@gmail.com'

# Create secure SSL context
context = ssl.create_default_context()


# Define a class to store the user details
# This not only reduces the number of queries made to the database
# But also makes code much more reusable and modular
class Customer:
    def __init__(self, login_id):
        # Given the login_id, we retrieve all information from the Customer and LoginDetails tables
        mycursor = mydb.cursor()
        mycursor.execute('select * from Customer c, LoginDetails ld where c.customer_id = ld.customer_id and '
                         'ld.login_id = %s', (login_id,))
        response = mycursor.fetchall()
        if len(response) == 0 or not response:
            exit(404)
        self.customer_id = response[0][0]
        self.salutation = response[0][2]
        self.first_name = response[0][3]
        self.last_name = response[0][4]
        self.date_of_birth = response[0][5]
        self.contact_no_1 = response[0][6]
        self.contact_no_2 = response[0][7]
        self.email = response[0][8]
        self.address = response[0][9]
        self.address_city = response[0][10]
        self.address_state = response[0][11]
        self.address_country = response[0][12]
        self.address_postcode = response[0][13]
        self.last_login = self.retrieve_last_login()
        self.banker = Banker(response[0][1])
        self.account_list = self.retrieve_account_list()

    def print_user(self):
        name = self.salutation + '. ' + self.first_name + ' ' + self.last_name
        print('----------------------------------------------------------------------------------------------------')
        print(f'Name: {name}')
        print(f'Date of Birth: {self.date_of_birth}')
        print(f'Contact No (1): {self.contact_no_1}')
        print(f'Contact No (2): {self.contact_no_2}')
        print(f'Email: {self.email}')
        print(f'Address: {self.address}, {self.address_city} {self.address_state} {self.address_country} {self.address_postcode}')
        print(f'Last Login: {self.last_login}')
        self.banker.print_banker()
        print('----------------------------------------------------------------------------------------------------')

    def retrieve_last_login(self):
        mycursor = mydb.cursor()
        mycursor.execute('select max(last_login) from LoginHistory where customer_id = %s and last_login < (select max(last_login) from LoginHistory)', (self.customer_id,))
        response = mycursor.fetchall()
        if len(response) == 0 or not response:
            return 'First login'
        return response[0][0]

    def print_login_history(self):
        mycursor = mydb.cursor()
        mycursor.execute('select * from LoginHistory where customer_id = %s', (self.customer_id,))
        result = mycursor.fetchall()
        print('----------------------------------------------------------------------------------------------------')
        for i in range(len(result)):
            print(f'Login #{i + 1}.:{result[i][1]}')
        print('----------------------------------------------------------------------------------------------------')

    def retrieve_account_list(self):
        mycursor = mydb.cursor()
        mycursor.execute('select account_id from Account where customer_id = %s', (self.customer_id,))
        response = mycursor.fetchall()
        account_list = []
        if len(response) == 0 or not response:
            return []
        for account_id in response:
            new_account = Account(account_id[0], self.salutation + '. ' + self.first_name + ' ' + self.last_name)
            account_list.append(new_account)
        return account_list


# Define a class to store account details
# A Customer owns a certain number of accounts
class Account:
    def __init__(self, account_id, owner_name):
        mycursor = mydb.cursor()
        mycursor.execute('select * from Account where account_id = %s', (account_id,))
        response = mycursor.fetchall()
        if len(response) == 0 or not response:
            exit(404)
        self.account_id = account_id
        self.owner_name = owner_name
        self.balance = response[0][2]
        self.currency = response[0][3]
        self.opening_date = response[0][4]
        self.branch = Branch(response[0][5])
        self.last_updated = response[0][6]
        self.transaction_list = self.retrieve_transaction_list()
        mycursor.execute('select * from SavingsAccount where account_id = %s', (account_id,))
        response = mycursor.fetchall()
        if response:
            self.account_type = 'Savings'
            self.interest_rate = response[0][1]
        else:
            self.account_type = 'Current'
            mycursor.execute('select * from CurrentAccount where account_id = %s', (account_id,))
            response = mycursor.fetchall()
            self.overdraft_limit = response[0][1]
            self.overdraft_used = response[0][2]
            self.overdraft_due_date = response[0][3]

    def print_account(self):
        print('----------------------------------------------------------------------------------------------------')
        print(f'Account ID: {self.account_id}')
        print(f'Owner Name: {self.owner_name}')
        print(f'Account Balance: {self.currency} {self.balance}')
        print(f'Account Currency: {self.currency}')
        if self.account_type == 'Savings':
            print(f'Account Type: Savings')
            print(f'Interest Rate: {self.interest_rate}')
        else:
            print(f'Account Type: Current')
            print(f'Overdraft Limit: {self.overdraft_limit}')
            print(f'Overdraft Used: {self.overdraft_used}')
            print(f'Overdraft Remaining: {self.overdraft_limit - self.overdraft_used}')
            print(f'Overdraft Due Date: {self.overdraft_due_date}')
        print(f'Opening Date: {self.opening_date}')
        self.branch.print_branch()
        print(f'Last Updated: {self.last_updated}')
        print('----------------------------------------------------------------------------------------------------')

    def retrieve_transaction_list(self):
        mycursor = mydb.cursor()
        mycursor.execute('select transaction_id from Transaction where account_id = %s', (self.account_id,))
        response = mycursor.fetchall()
        transaction_list = []
        if not response:
            return []
        for transaction_id in response:
            new_transaction = Transaction(transaction_id[0], self.account_id)
            transaction_list.append(new_transaction)
        return transaction_list


# Define a class to store account transactions
# An account may have one or more transactions
class Transaction:
    def __init__(self, transaction_id, account_id):
        mycursor = mydb.cursor()
        mycursor.execute('select * from Transaction where transaction_id = %s and account_id = %s', (transaction_id, account_id))
        response = mycursor.fetchall()
        self.transaction_id = transaction_id
        self.account_id = account_id
        self.transaction_details = response[0][2]
        self.transaction_type = response[0][3]
        self.remarks = response[0][4]
        self.amount = response[0][5]
        self.currency = response[0][6]
        self.date_time = response[0][7]

    def print_transaction(self):
        print('----------------------------------------------------------------------------------------------------')
        print(f'Transaction ID: {self.transaction_id}')
        print(f'Account ID: {self.account_id}')
        print(f'Transaction Details: {self.transaction_details}')
        print(f'Transaction Type: {self.transaction_type}')
        print(f'Amount: {self.currency} {self.amount}')
        print(f'Currency: {self.currency}')
        print(f'DateTime: {self.date_time}')
        print(f'Remarks: {self.remarks}')
        print('----------------------------------------------------------------------------------------------------')


# Define a class to store branch information
# Every account is linked to a branch, and every banker is linked to a branch
class Branch:
    def __init__(self, branch_id):
        mycursor = mydb.cursor()
        mycursor.execute('select * from Branch where branch_id = %s', (branch_id,))
        response = mycursor.fetchall()
        if not response or len(response) == 0:
            exit(404)
        self.branch_id = branch_id
        self.address = response[0][1]
        self.branch_city = response[0][2]
        self.branch_state = response[0][3]
        self.branch_country = response[0][4]
        self.branch_postcode = response[0][5]

    def print_branch(self):
        print('----------------------------------------------------------------------------------------------------')
        print(f'Branch ID: {self.branch_id}')
        print(f'Address: {self.address}, {self.branch_city}, {self.branch_state} {self.branch_country} - {self.branch_postcode}')
        print('----------------------------------------------------------------------------------------------------')


# Define a class to store banker information
# Every customer is assigned their own personal banker
class Banker:
    def __init__(self, banker_id):
        mycursor = mydb.cursor()
        mycursor.execute('select * from Banker where banker_id = %s', (banker_id,))
        response = mycursor.fetchall()
        if not response or len(response) == 0:
            exit(404)
        self.banker_id = banker_id
        self.branch = Branch(response[0][1])
        self.first_name = response[0][2]
        self.last_name = response[0][3]
        self.date_of_birth = response[0][4]
        self.date_of_joining = response[0][5]
        self.contact_no = response[0][6]
        self.email = response[0][7]
        self.years_of_experience = round((datetime.now().date() - self.date_of_joining).days / 365)

    def print_banker(self):
        experience = datetime.now().date() - self.date_of_joining
        print('----------------------------------------------------------------------------------------------------')
        print(f'Banker ID: {self.banker_id}')
        print(f'Banker Name: {self.first_name} {self.last_name}')
        print(f'Date of Birth: {self.date_of_birth}')
        print(f'Date of Joining: {self.date_of_joining}')
        print(f'Years of Experience: {self.years_of_experience}')
        self.branch.print_branch()
        print('----------------------------------------------------------------------------------------------------')


def validate_login(login_id, password):
    # To check if user login information is accurate
    mycursor = mydb.cursor()
    mycursor.execute('select * from LoginDetails where login_id = %s and customer_password = %s',
                     (login_id, password))
    result = mycursor.fetchall()
    if len(result) == 1:
        # Query executed successfully
        # Check if number of entries for the customer is equal to 10
        #mycursor.execute('select * from LoginHistory where customer_id = %s', (result[0][0]))
        #list_of_entries = mycursor.fetchall()
        #if len(list_of_entries) >= 10:
            # If so, then delete the oldest one
            #mycursor.execute('delete from LoginHistory where customer_id = %s and last_login in (select min(last_login) from LoginHistory where customer_id = %s)', (result[0][0], result[0][0]))
        # Update the login times table by adding the current timestamp
        timestamp = datetime.now()
        mycursor.execute('insert into LoginHistory (customer_id, last_login) values (%s, %s)',
                         (result[0][0], timestamp))
        # Send email notification of login to the user
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(email_id, email_password)
            # TODO: Send email here
            mycursor.execute('select c.email from Customer c, LoginDetails ld where ld.customer_id = c.customer_id and ld.login_id = %s', (login_id,))
            recipient_address = mycursor.fetchall()[0][0]
            message = """\
            From: BestBank\nSubject: [BestBank] Login Notification\n\nThis is an automated notification email. A login with your login_id %s was detected at %s.
            """ % (login_id, timestamp)
            server.sendmail(email_id, recipient_address, message)
        mydb.commit()
        return True
    else:
        return False


def main_menu(customer):
    print('Select an option: ')
    print('1. Print Customer Profile')
    print('2. Print Account List')
    print('3. Print Transaction List')
    print('4. Print Login History')
    print('5. Print Last Login')
    print('6. Exit')
    selection = int(input())
    if selection == 1:
        customer.print_user()
    if selection == 2:
        for account in customer.account_list:
            account.print_account()
    if selection == 3:
        print('Enter the account ID:')
        for account in customer.account_list:
            print(account.account_id)
        input_id = input()
        for account in customer.account_list:
            if account.account_id == input_id:
                for transaction in account.transaction_list:
                    transaction.print_transaction()
    if selection == 4:
        customer.print_login_history()
    if selection == 5:
        print(customer.last_login)
    if selection == 6:
        return False
    return True


def main():
    # Ask for user login
    print('Welcome to Best Bank iKYC!')
    login_id = input('Enter the user login id: ')
    password = input('Enter the user password: ')
    if validate_login(login_id, password):
        flag = True
        customer = Customer(login_id)
        while flag:
            flag = main_menu(customer)
            if not flag:
                break


if __name__ == '__main__':
    main()
