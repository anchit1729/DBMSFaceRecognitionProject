# DBMS Face Recognition Project

This is the implementation for the COMP3278 Introduction to Database Management Systems course project. It uses Python and MySQL for an eKYC Face-ID based banking application.

## Group Members

1. Anchit Mishra
2. Kritik Satija
3. Raghav Agarwal
4. Abhigyan Kashyap
5. Ajayveer Singh

## Contributions

| Component         | Tools Used | Contributor(s)           |
|-------------------|------------|--------------------------|
| Face-ID           | Python     | NA                       |
| UI                | PyQT5      | Kritik, Raghav, Abhigyan, Ajay |
| Database          | MySQL      | Anchit                   |
| DB-UI Connections | Python     | Anchit, Raghav, Kritik   | 

*******

## Usage

### Environment

Create virtual environment using Anaconda.
```
conda create -n face python=3.x
conda activate face
pip install -r requirements.txt
```

### MySQL Install

[Mac](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/macos-installation.html)

[Ubuntu](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/linux-installation.html)

[Windows](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/windows-installation.html)

You'll obtain an account and password after installation, then you should modify the `faces.py`, with the corresponding
`user` and `passwd`:
```
# create database connection
myconn = mysql.connector.connect(host="localhost", user="root", passwd="xxxxx", database="facerecognition")
```

*******

## Run

### 1. Main GUI-Based Application

NOTE: This application was primarily developed on a 13 inch Macbook Pro system with macOS 12.0.1 Monterey. As a result, the screen resolutions and GUI layouts are best viewed on the macOS platform. However, we have tried to accomodate Windows users by implementing separate UI files for Windows PCs.

#### 1.1 Running the application

Run the file `front_end.py` to start the application:
```
python front_end.py
```

#### 1.2 Login Page

Once the application login window is open, there are multiple options:

1. Login - You may enter your Login ID/User ID and Password into the text box and click 'Login' to authenticate and enter the application.
2. Register Face - You may enter your Login ID/User ID and Password into the text box and click 'Register Face' to authenticate and enter the application. Note that it is NOT POSSIBLE to create a new Login ID/User ID and Password pair for this application. This models the real-world functioning of a bank, where you must possess an online-banking account to access the eKYC functions. It does not practically make sense for a user to create a new eKYC account without creating a new bank account by visiting the branch.
3. Face Login - If you have already registered your face with login credentials, you may click on the Face-ID button in the center. This turns on the camera and once your face is recognised, you are logged into your account.

#### 1.3 Dashboard

On this page, all your basic account information is displayed, including your personal details as well as the details of the personal banker assigned to assist you. In addition, a tabular view of all your accounts is also available. You may click on individual accounts to open a new, detailed view for the account. On the top right is a logout button, which you may click to log out of the application. Closing the application window is also allowed.

#### 1.4 Account Details

On this page, a detailed view of the account is presented, with information such as account number, account type, currency and balance. In addition, another tabular view is provided that displays a list of transactions carried out with the account. At the bottom, there is a text field to enter a password to generate a PDF. This allows users to generate a PDF of their account summary. This PDF can either be sent to the registered email ID of the customer or downloaded to the root directory of this project. The transaction table also allows users to search transactions based on time, day, month, year and amount. As an engineering choice and to make table search simpler, we have decided to allocate the time 00:00:00 for server maintenance, which basically allows the system to ignore searched time values of 00:00:00. Finally, individual transactions may be clicked to open a new view containing a summary of the transaction.

#### 1.5 Transaction Details

On this page, a summary of the transaction is provided, including transaction type, transaction ID, transaction details (which describe sender/recipient information depending on whether the transaction is a debit or credit to the account), currency, amount and remarks. Similar to the Account Details view, individual transaction summaries may also be downloaded or sent via email as a PDF.

### 2. Database Design

There are two scripts provided for the database: `banking_project_setup.sql` and `data_dump.sql`. The first one is to create the tables as per our DB design while the second one is to populate the tables with custom-created data for demonstration and use.

#### 2.1 Import Database
Open mysql server and import the files `banking_project_setup.sql` and `data_dump.sql`, in exactly that order.
```
# login to the mysql prompt
mysql -u root -p

# import from sql file
mysql> source banking_project_setup.sql
mysql> source data_dump.sql
```



