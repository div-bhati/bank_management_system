--Step 1
use bank_management_system;
create table if not exists pan_records(
	first_name varchar(20),
    	last_name varchar(20),
    	pan_number varchar(11) unique,
    	mobile_number varchar(10));

create table if not exists customer(
	customer_id integer primary key,
	first_name varchar(20) not null,
   	last_name varchar(20),
   	email varchar(30) not null unique,
	phone_number varchar(20) unique ,
	pan varchar(11) unique,
	address varchar(100),
	foreign key (pan) references pan_records(pan_number));

create table if not exists accounts(
	customer_id integer not null,
	account_number integer primary key,
	balance decimal(10,3),
	foreign key (customer_id) references customer(customer_id));

create table transactions(
	sender integer,
	receiver integer,
	amount varchar(50),
	pan_record varchar(10),
	phone_no varchar(20),
	transaction_description varchar(500),
	foreign key (sender) references accounts(account_number),
	foreign key (receiver) references accounts(account_number),
	foreign key (pan_record) references pan_records(pan_number),
	foreign key (phone_no) references customer(phone_number));

show tables;

