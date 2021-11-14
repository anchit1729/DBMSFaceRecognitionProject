/* set up the database */
DROP DATABASE IF EXISTS `banking_application`;
CREATE DATABASE `banking_application`;

/* switch to database */
USE `banking_application`;

/* create all required tables */


CREATE TABLE Branch
(
  branch_id CHAR(5) NOT NULL,
  branch_address VARCHAR(50) NOT NULL,
  branch_city VARCHAR(32) NOT NULL,
  branch_state VARCHAR(32),
  branch_country VARCHAR(32) NOT NULL,
  branch_postcode VARCHAR(10) NOT NULL,
  PRIMARY KEY (branch_id)
);

CREATE TABLE Banker
(
  banker_id CHAR(5) NOT NULL,
  branch_id CHAR(5) NOT NULL,
  first_name VARCHAR(20) NOT NULL,
  last_name VARCHAR(20) NOT NULL,
  date_of_birth DATE NOT NULL,
  date_of_joining DATE NOT NULL,
  contact_no VARCHAR(15) NOT NULL,
  email VARCHAR(50) NOT NULL,
  PRIMARY KEY (banker_id),
  FOREIGN KEY (branch_id) REFERENCES Branch (branch_id)
);

CREATE TABLE Customer
(
  customer_id CHAR(10) NOT NULL,
  banker_id CHAR(10) NOT NULL,
  salutation VARCHAR(3) NOT NULL,
  first_name VARCHAR(20) NOT NULL,
  last_name VARCHAR(20) NOT NULL,
  date_of_birth DATE NOT NULL,
  contact_no_1 VARCHAR(15) NOT NULL,
  contact_no_2 VARCHAR(15),
  email VARCHAR(50) NOT NULL,
  address VARCHAR(50) NOT NULL,
  address_city VARCHAR(32) NOT NULL,
  address_state VARCHAR(32),
  address_country VARCHAR(32) NOT NULL,
  address_post_code VARCHAR(10) NOT NULL,
  PRIMARY KEY (customer_id),
  FOREIGN KEY (banker_id) REFERENCES Banker (banker_id)
);

CREATE TABLE LoginDetails
(
  customer_id CHAR(10) NOT NULL UNIQUE,
  login_id VARCHAR(50) NOT NULL,
  customer_password VARCHAR(50) NOT NULL,
  last_login DATETIME,
  PRIMARY KEY (login_id),
  FOREIGN KEY (customer_id) REFERENCES Customer (customer_id)
);

CREATE TABLE Account
(
  account_id CHAR(10) NOT NULL,
  customer_id CHAR(10) NOT NULL,
  account_balance FLOAT NOT NULL,
  account_currency CHAR(3) NOT NULL check (account_currency IN ('HKD','USD','GBP')),
  opening_date DATE NOT NULL,
  branch_id VARCHAR(5) NOT NULL,
  PRIMARY KEY (account_id),
  FOREIGN KEY (customer_id) REFERENCES Customer (customer_id),
  FOREIGN KEY (branch_id) REFERENCES Branch (branch_id)
);

CREATE TABLE SavingsAccount
(
  account_id CHAR(10) NOT NULL,
  interest_rate FLOAT NOT NULL,
  PRIMARY KEY (account_id),
  FOREIGN KEY (account_id) REFERENCES Account (account_id)
);

CREATE TABLE CurrentAccount
(
  account_id CHAR(10) NOT NULL,
  overdraft_limit INT NOT NULL,
  overdraft_used INT NOT NULL,
  overdraft_due_date DATE,
  PRIMARY KEY (account_id),
  FOREIGN KEY (account_id) REFERENCES Account (account_id)
);

CREATE TABLE Transaction
(
  transaction_id VARCHAR(10) NOT NULL,
  account_id CHAR(10) NOT NULL,
  transaction_details VARCHAR(15) NOT NULL,
  transaction_type CHAR(2) NOT NULL check (transaction_type in ('CR','DR')),
  remarks VARCHAR(50) NOT NULL,
  amount DECIMAL(11, 2) NOT NULL,
  currency CHAR(3) NOT NULL check (currency IN ('HKD','USD','GBP')),
  transaction_date_time DATETIME NOT NULL,
  PRIMARY KEY (transaction_id, account_id),
  FOREIGN KEY (account_id) REFERENCES Account (account_id)
);


