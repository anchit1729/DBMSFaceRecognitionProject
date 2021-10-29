Insert Into Branch (branch_id,branch_address,branch_city,branch_state,branch_country,branch_postcode)
VALUES
('H1001','9 Maine Street, Central','Hong Kong','','Hong Kong SAR','999077'),
('H1002','Times Square, Causeway Bay','Hong Kong','','Hong Kong SAR','999077'),
('H1003','Des Voeux Road Central, Sheung Wan','Hong Kong','','Hong Kong SAR','999077'),
('H1004','Hennessy Road Wan Chai','Hong Kong','','Hong Kong SAR','999077'),
('H1005','150-160 Castle Peak Road, Yuen Long','Hong Kong','','Hong Kong SAR','999077'),
('H1006','54-58 Kwong Fuk Road, Tai Po','Hong Kong','','Hong Kong SAR','999077');

Insert into Customer (customer_id,salutation_name,first_name,middle_name,last_name,date_of_birth,contact_no_1,contact_no_2,email,address,address_city,address_state,address_country,address_post_code)
Values
('CUST10001','Mr','Tim','','Cook','1999-02-03','+854 67348921','','tim@gmail.com','A501 JCSV-III','Hong Kong','','Hong Kong SAR','999077'),
('CUST10002','Mr','Anchit','','Mishra','2000-05-15','+854 1234 8123','+852 5376 0021','anchit@connect.hku.hk','A2012 JCSV-III','Hong Kong','','Hong Kong SAR','999077'),
('CUST10003','Ms','Lisa','','Ray','1980-11-02','+854 1232 1925','','lr@gmail.com','A15 Rose Villa','Hong Kong','','Hong Kong SAR','999077'),
('CUST10004','Ms','Victoria','','Ruddock','1999-02-06','+854 6734 2111','','vr@abc.com','B29 KC Tower','Hong Kong','','Hong Kong SAR','999077'),
('CUST10005','Mr','Abhigyan','','Kashyap','2001-05-14','+854 6734 6242','','cl@cds.com','34A T Tower','Hong Kong','','Hong Kong SAR','999077'),
('CUST10006','Mr','Raghav','','Agarwal','2001-11-03','+854 6714 1613','','rv@hku.com','12D Richmond Road','Hong Kong','','Hong Kong SAR','999077'),
('CUST10007','Mr','Ajayveer','','Singh','2001-01-11','+854 6734 9414','','as@hku.com','8 KC Street','Hong Kong','','Hong Kong SAR','999077'),
('CUST10008','Ms','Marry','','Fernandis','1999-12-11','+854 6729 5731','','mf@abc.com','A6011-B JCSV -3','Hong Kong','','Hong Kong SAR','999077'),
('CUST10009','Mr','Kritik','','Satija','2001-03-12','+854 6793 4321','','vg@gmail.com','A19-B KC Tower','Hong Kong','','Hong Kong SAR','999077');

Insert Into LoginHistory (customer_id,last_login)
Values
('CUST10001','2020-12-06'),
('CUST10001','2020-11-06'),
('CUST10001','2020-04-06'),
('CUST10003','2020-05-06'),
('CUST10003','2020-06-06'),
('CUST10004','2020-06-17'),
('CUST10004','2020-06-18'),
('CUST10004','2020-06-19'),
('CUST10004','2020-06-20'),
('CUST10005','2020-06-21'),
('CUST10001','2020-06-22'),
('CUST10002','2020-06-23'),
('CUST10003','2020-06-24'),
('CUST10004','2020-06-25'),
('CUST10005','2020-06-26');

Insert Into Account
(account_id,customer_id,account_balance,account_currency,account_type,opening_date,branch_id)
Values
('A123000001','CUST10001','10150','HKD','Saving','2019-08-31','H1001'),
-- Accounts for Anchit
('A123000002','CUST10002','5550','HKD','Saving','2019-09-01','H1002'),
('A123000003','CUST10002','1500','USD','Saving','2019-11-01','H1004'),
('A123000004','CUST10002','11000','HKD','Current','2019-11-04','H1002'),
('A123000005','CUST10002','8900','HKD','Saving','2019-09-02','H1003'),
('A123000006','CUST10004','12000','HKD','Saving','2019-09-03','H1001'),
-- Accounts for Abhigyan
('A123000007','CUST10005','14500','HKD','Saving','2019-09-04','H1002'),
('A123000008','CUST10005','5000','HKD','Saving','2019-09-04','H1001'),
('A123000009','CUST10005','900','USD','Current','2020-01-05','H1004'),
-- Accounts for Raghav
('A123000010','CUST10006','8950','USD','Saving','2019-09-05','H1003'),
-- Accounts for Ajay
('A123000011','CUST10007','1200','HKD','Saving','2019-09-06','H1001'),
('A123000012','CUST10007','4800','USD','Saving','2019-09-07','H1002'),
-- Accounts for Kritik
('A123000013','CUST10009','7500','USD','Saving','2019-09-08','H1003'),
('A123000014','CUST10009','7555','USD','Current','2020-04-09','H1001'),
('A123000015','CUST10003','8580','USD','Current','2019-08-02','H1003'),
('A123000016','CUST10008','11850','HKD','Current','2019-11-12','H1002');

Insert Into Transaction
(transaction_id,account_id,recepient_details,transaction_remarks,amount,currency,transaction_date_time)
Values
('TX00000001','A123000002','IKEA','Bedsheet','200','HKD','2019-11-11 12:30'),
('TX00000002','A123000002','7-11','1lt. Milk, 1pkt. Bread','80','HKD','2019-11-11 13:05'),
('TX00000001','A123000003','Paisano Pizza','1x Pizza','13','USD','2019-11-13 16:30'),
('TX00000001','A123000004','Marks&Spencer','3x Shirt','300','HKD','2020-06-14 12:30'),
('TX00000002','A123000004','Pizza Express','1x Pizza','300','HKD','2020-06-15 11:35'),
('TX00000001','A123000005','Amazon','Books','500','HKD','2020-07-16 12:30'),
('TX00000001','A123000007','Amazon','Electronics','12000','HKD','2020-07-16 14:30'),
('TX00000001','A123000008','Wellcome','Groceries','650','HKD','2020-07-14 11:35'),
('TX00000001','A123000009','MTR','Weekly Travel Pass','65','USD','2020-06-14 11:45'),
('TX00000001','A123000010','T Mobile','Mobile Plan Rent','75','HKD','2020-11-20 11:00'),
('TX00000001','A123000011','H&M','Trousers','1150','USD','2020-12-20 13:00'),
('TX00000001','A123000013','Wellcome','Groceries','450','HKD','2020-11-22 10:30');

Insert into CustomerSPI
(customer_id,customer_password)
Values
('cust10001','cu@1234'),
('cust10002','custAnchit'),
('cust10003','cu@1236'),
('cust10004','cu@1237'),
('cust10005','custAbhigyan'),
('cust10006','custRaghav'),
('cust10007','custAjay'),
('cust10008','cu@1241'),
('cust10009','custKritik');