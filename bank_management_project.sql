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

show tables;

