import mysql.connector
from datetime import datetime

# Make a connection to the local database
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Champu2k',
    database='banking_application'
)


def display_user_profile(user_id):
    # Here, we display the entire row from the Customer table
    mycursor = mydb.cursor()
    mycursor.execute('select * from Customer where customer_id =  %s', (user_id,))
    result = mycursor.fetchall()
    print(f'Customer ID: {result[0][0]}')
    print(f'Customer Name: {result[0][1]}. {result[0][2]} {result[0][3]} {result[0][4]}')
    print(f'Date of Birth: {result[0][5].strftime("%d-%b-%Y")}')
    print(f'Contact No. (1): {result[0][6]}')
    print(f'Contact No. (2): {result[0][7]}')
    print(f'Email Address: {result[0][8]}')
    print(f'Address: {result[0][9]}, {result[0][10]}, {result[0][11]} {result[0][12]}')
    print(f'Post Code: {result[0][13]}')


def display_user_accounts(user_id):
    # Here, we display all the rows in the Account table that match with the customer_id
    mycursor = mydb.cursor()
    mycursor.execute('select * from Account where customer_id = %s', (user_id,))
    result = mycursor.fetchall()
    if len(result) == 0:
        print('No accounts to display!')
    for entry in result:
        print('--------------------------------------------------------------')
        print(f'Account ID: {entry[0]}')
        print(f'Account Balance: {entry[2]}')
        print(f'Account Currency: {entry[3]}')
        print(f'Account Type: {entry[4]}')
        print(f'Opening Date: {entry[5]}')
        print(f'Branch ID: {entry[6]}')
        print('--------------------------------------------------------------')


def select_user_account(user_id):
    print('Enter the Account ID of the account whose transactions are to be displayed:')
    mycursor = mydb.cursor()
    mycursor.execute('select * from Account where customer_id = %s', (user_id,))
    result = mycursor.fetchall()
    for i in range(len(result)):
        print(f'Account #{i+1}. {result[i][0]}')
    input_id = input()
    return input_id


def display_account_transactions(account_id):
    mycursor = mydb.cursor()
    mycursor.execute('select * from Transaction where account_id = %s', (account_id,))
    result = mycursor.fetchall()
    for entry in result:
        print('-------------------------------------------------------------------------')
        print(f'Transaction ID: {entry[0]}')
        print(f'Recipient Details: {entry[2]}')
        print(f'Transaction Remarks: {entry[3]}')
        print(f'Amount: {entry[4]}')
        print(f'Currency: {entry[5]}')
        print(f'Transaction Time: {entry[6].strftime("%d-%b-%Y %H:%M:%S")}')
        print('-------------------------------------------------------------------------')


def display_user_login_history(user_id):
    mycursor = mydb.cursor()
    mycursor.execute('select * from LoginHistory where customer_id = %s', (user_id,))
    result = mycursor.fetchall()
    print('----------------------------------------------------------------------')
    for i in range(len(result)):
        print(f'Login #{i+1}.:{result[i][1]}')
    print('----------------------------------------------------------------------')


def validate_login(user_id, password):
    # To check if user login information is accurate
    mycursor = mydb.cursor()
    mycursor.execute('select * from CustomerSPI where customer_id = %s and customer_password = %s', (user_id, password))
    result = mycursor.fetchall()
    if len(result) == 1:
        # Query executed successfully
        # Update the login times table by adding the current timestamp
        mycursor.execute('insert into LoginHistory (customer_id, last_login) values (%s, %s)', (user_id, datetime.now()))
        mydb.commit()
        return True
    else:
        return False


def main_menu(user_id):
    print('Welcome to the database utility test!')
    print('Please select an option:')
    print('1. Display User Profile Details')
    print('2. Display User Accounts')
    print('3. Display User Transactions')
    print('4. Display User Login History')
    print('5. Exit')
    selected_option = int(input())
    if selected_option == 1:
        display_user_profile(user_id)
        return True
    if selected_option == 2:
        display_user_accounts(user_id)
        return True
    if selected_option == 3:
        account_id = select_user_account(user_id)
        display_account_transactions(account_id)
        return True
    if selected_option == 4:
        display_user_login_history(user_id)
        return True
    if selected_option == 5:
        return False


def main():
    # Print the details of the connector
    print(mydb)
    # Ask for user login
    user_id = input('Enter the user id: ')
    password = input('Enter the user password: ')
    if validate_login(user_id, password):
        flag = True
        while flag:
            flag = main_menu(user_id)
            if not flag:
                break


if __name__ == '__main__':
    main()
