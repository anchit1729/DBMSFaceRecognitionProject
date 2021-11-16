Insert Into Branch (branch_id,branch_street_address,branch_city,branch_state,branch_country,branch_postcode)
VALUES
('H1001','9 Maine Street, Central','Hong Kong','','Hong Kong SAR','999077'),
('H1002','Times Square, Causeway Bay','Hong Kong','','Hong Kong SAR','999077'),
('H1003','Des Voeux Road Central, Sheung Wan','Hong Kong','','Hong Kong SAR','999077'),
('H1004','Hennessy Road Wan Chai','Hong Kong','','Hong Kong SAR','999077');

Insert Into Banker (banker_id,branch_id,first_name,last_name,date_of_birth,date_of_joining,contact_no,email)
VALUES
('B1001','H1001','James','Smith','1990-02-14','2015-06-03','+852 5372 9981','james@bank.com'),
('B1002','H1001','Michael','Robertson','1985-10-01','2012-04-01','+852 3421 5641','michael@bank.com'),
('B1003','H1002','Emily','Jones','1992-06-13','2014-05-03','+852 7584 4839','emily@bank.com'),
('B1004','H1003','Jess','Ableton','1989-02-22','2018-09-24','+852 2853 5739','jess@bank.com'),
('B1005','H1004','Reese','Richards','1990-01-05','2020-07-20','+852 4398 9781','reese@bank.com');

Insert into Customer (customer_id,salutation,first_name,last_name,date_of_birth,contact_no_1,contact_no_2,email,street_address,address_city,address_state,address_country,address_post_code,banker_id)
Values
('CUST10001','Mr','Anchit','Mishra','2000-05-15','+854 5376 0021','+852 2315 0069','anchit@connect.hku.hk','A2012 JCSV-III','Hong Kong','','Hong Kong SAR','999077','B1001'),
('CUST10002','Mr','Abhigyan','Kashyap','2001-05-14','+854 6734 6242','','abhigyan@connect.hku.hk','34A T Tower','Hong Kong','','Hong Kong SAR','999077','B1002'),
('CUST10003','Mr','Raghav','Agarwal','2001-11-03','+854 6714 1613','+852 8294 4232','raghav@connect.hku.hk','12D Richmond Road','Hong Kong','','Hong Kong SAR','999077','B1003'),
('CUST10004','Mr','Ajayveer','Singh','2001-01-11','+854 6734 9414','','ajayvs@connect.hku.hk','8 KC Street','Hong Kong','','Hong Kong SAR','999077','B1004'),
('CUST10005','Mr','Kritik','Satija','2001-03-12','+854 6793 4321','+852 1523 7584','kritik@connect.hku.hk','A19-B KC Tower','Hong Kong','','Hong Kong SAR','999077','B1005');

Insert into LoginDetails
(customer_id,login_id,customer_password, last_login)
Values
('CUST10001','anchit1729','custAnchit', '2021-10-20 09:20:31'),
('CUST10002','ak472001','custAbhigyan', '2021-10-29 19:00:01'),
('CUST10003','marwadi3000','custRaghav', '2021-10-10 07:35:11'),
('CUST10004','ajayveer2002','custAjay', '2021-10-15 11:22:08'),
('CUST10005','voyeur69','custKritik', '2021-10-21 13:28:02');

Insert Into Account
(account_id,customer_id,account_balance,account_currency,opening_date,branch_id)
Values
-- Accounts for Anchit
('A123000001','CUST10001','5550','HKD','2019-09-01','H1002'),
('A123000002','CUST10001','1500','USD','2019-11-01','H1004'),
('A123000003','CUST10001','11000','HKD','2019-11-04','H1002'),
-- Accounts for Abhigyan
('A123000004','CUST10002','5000','HKD','2019-09-04','H1001'),
('A123000005','CUST10002','900','USD','2020-01-05','H1004'),
-- Accounts for Raghav
('A123000006','CUST10003','8950','USD','2019-09-05','H1003'),
-- Accounts for Ajay
('A123000007','CUST10004','1200','HKD','2019-09-06','H1001'),
('A123000008','CUST10004','4800','USD','2019-09-07','H1002'),
-- Accounts for Kritik
('A123000009','CUST10005','8580','USD','2019-08-02','H1003'),
('A123000010','CUST10005','11850','HKD','2019-11-12','H1002');

Insert Into SavingsAccount
(account_id,interest_rate)
Values
('A123000001','1.0'),
('A123000002','0.8'),
('A123000004','1.0'),
('A123000006','1.2'),
('A123000007','0.5'),
('A123000008','0.3');

Insert Into CurrentAccount
(account_id,overdraft_limit,overdraft_used,overdraft_due_date)
Values
('A123000003','20000','0',NULL),
('A123000005','1000','0',NULL),
('A123000009','10000','6000','2021-11-22'),
('A123000010','20000','0',NULL);


Insert Into Transaction
(transaction_id,account_id,transaction_details,transaction_type,remarks,amount,currency,transaction_date_time)
Values
('TX00000001','A123000001','IKEA','DR','Bedsheet','200','HKD','2019-11-11 12:30'),
('TX00000002','A123000001','7-11','DR','1lt. Milk, 1pkt. Bread','80','HKD','2019-11-11 13:05'),
('TX00000003','A123000001','MTR Corp','CR','Rewards','100','HKD','2019-12-01 20:20'),
('TX00000001','A123000002','Paisano Pizza','DR','1x Pizza','13','USD','2019-11-13 16:30'),
('TX00000002','A123000002','Marks&Spencer','DR','3x Shirt','300','USD','2020-06-14 12:30'),
('TX00000003','A123000002','Pizza Express','DR','1x Pizza','300','USD','2020-06-15 11:35'),
('TX00000004','A123000002','Arvind Mishra','CR','Monthly Allowance','300','USD','2020-09-10 08:20'),
('TX00000005','A123000002','Ali Murtaza','CR','Lunch Bill Split','10','USD','2020-10-10 12:30'),
('TX00000001','A123000003','Amazon','DR','Books','500','HKD','2020-07-16 12:30'),
('TX00000001','A123000004','Amazon','DR','Electronics','12000','HKD','2020-07-16 14:30'),
('TX00000002','A123000004','Wellcome','DR','Groceries','650','HKD','2020-07-14 11:35'),
('TX00000001','A123000005','MTR','DR','Weekly Travel Pass','65','USD','2020-06-14 11:45'),
('TX00000002','A123000005','T Mobile','DR','Mobile Plan Rent','10','USD','2020-11-20 11:00'),
('TX00000001','A123000006','H&M','DR','Trousers','1150','USD','2020-12-20 13:00'),
('TX00000001','A123000007','Wellcome','DR','Groceries','450','HKD','2020-11-22 10:30'),
('TX00000001','A123000008','7-11','DR','1lt. Orange Juice','3','USD','2020-10-12 13:20'),
('TX00000001','A123000009','360 Best Mart','DR','1pkt. Oreo','2','USD','2020-09-19 18:20'),
('TX00000001','A123000010','Staples Online','DR','10x Whiteboard Markers','200','HKD','2020-08-10 21:30');