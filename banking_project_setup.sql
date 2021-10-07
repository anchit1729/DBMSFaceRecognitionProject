/* set up the database */
DROP DATABASE IF EXISTS `banking_application`;
CREATE DATABASE `banking_application`;

/* switch to database */
USE `banking_application`;

/* create all required tables */
CREATE TABLE Guardian
(
  guardian_id INT NOT NULL,
  title_name VARCHAR(10) NOT NULL,
  first_name VARCHAR(20) NOT NULL,
  middle_name VARCHAR(20),
  last_name VARCHAR(20) NOT NULL,
  date_of_birth DATE NOT NULL,
  govt_id VARCHAR(8) NOT NULL,
  email_address VARCHAR(50) NOT NULL,
  PRIMARY KEY (guardian_id)
);

CREATE TABLE Branch
(
  branch_id INT NOT NULL,
  branch_address_line_one VARCHAR(50) NOT NULL,
  branch_address_line_two VARCHAR(50),
  branch_address_line_three VARCHAR(50),
  branch_address_city VARCHAR(32) NOT NULL,
  branch_address_state VARCHAR(32),
  branch_address_country VARCHAR(32) NOT NULL,
  branch_address_postcode VARCHAR(10) NOT NULL,
  PRIMARY KEY (branch_id)
);

CREATE TABLE Customer
(
  title_name VARCHAR(10) NOT NULL,
  first_name VARCHAR(20) NOT NULL,
  middle_name VARCHAR(20),
  last_name VARCHAR(20) NOT NULL,
  date_of_birth DATE NOT NULL,
  govt_id VARCHAR(8) NOT NULL,
  email VARCHAR(50) NOT NULL,
  theme_color INT NOT NULL,
  last_login DATETIME,
  address_line_one VARCHAR(50) NOT NULL,
  address_line_two VARCHAR(50),
  address_line_three VARCHAR(50),
  address_city VARCHAR(32) NOT NULL,
  address_state VARCHAR(32),
  address_country VARCHAR(32) NOT NULL,
  address_post_code VARCHAR(10) NOT NULL,
  user_id INT NOT NULL,
  user_login VARCHAR(32) NOT NULL,
  user_password CHAR(32) NOT NULL,
  is_minor BIT(1) NOT NULL,
  guardian_id INT,
  PRIMARY KEY (user_id),
  FOREIGN KEY (guardian_id) REFERENCES Guardian (guardian_id)
);

CREATE TABLE UserPhone
(
  user_id INT NOT NULL,
  phone VARCHAR(15) NOT NULL,
  FOREIGN KEY (user_id) REFERENCES Customer (user_id)
);

CREATE TABLE GuardianPhone
(
  guardian_id INT NOT NULL,
  phone VARCHAR(15) NOT NULL,
  FOREIGN KEY (guardian_id) REFERENCES Guardian (guardian_id)
);

CREATE TABLE Account
(
  account_id INT NOT NULL,
  user_id INT NOT NULL,
  account_balance INT NOT NULL,
  account_currency CHAR(3) NOT NULL,
  account_type VARCHAR(7) NOT NULL,
  opening_date DATE NOT NULL,
  branch_id INT NOT NULL,
  PRIMARY KEY (account_id),
  FOREIGN KEY (user_id) REFERENCES Customer (user_id),
  FOREIGN KEY (branch_id) REFERENCES Branch (branch_id)
);

CREATE TABLE Card
(
  card_id INT NOT NULL,
  card_number VARCHAR(16) NOT NULL,
  issue_date DATE NOT NULL,
  expiration_date DATE NOT NULL,
  currency CHAR(3) NOT NULL,
  card_type VARCHAR(6) NOT NULL,
  credit_limit INT,
  card_balance INT,
  payment_due_date DATE,
  account_id INT NOT NULL,
  PRIMARY KEY (card_id),
  FOREIGN KEY (account_id) REFERENCES Account (account_id)
);

CREATE TABLE Transaction
(
  transaction_id INT NOT NULL,
  account_id INT NOT NULL,
  recepient_id INT NOT NULL,
  amount INT NOT NULL,
  currency INT NOT NULL,
  transaction_date_time DATETIME NOT NULL,
  PRIMARY KEY (transaction_id),
  FOREIGN KEY (account_id) REFERENCES Account (account_id)
);
