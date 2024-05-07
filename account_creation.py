import mysql.connector
import random


# first_name,last_name,pan_number,mobile_number,email,address,balance
def insert_data():
    print("Welcome to the bank.")
    print("While you create your account with us, it is not necessary to deposit while\ncreating the account. You can add funds afterwards.")
    print("To create account you need to enter the following details:\n1.Name\n2.PAN Number\n3.Mobile Number\n4.Email\n5.Address")
    take_fname = input("Enter your first name: ")
    take_lname = input("Enter your last name: ")
    take_pan = input("Enter your pan: ")
    take_mobileNo = input("Enter your mobile number: ")
    k = input("Do you want to add initial deposit(yes/no): ")
    if k == 'yes' or k =='Yes':
        take_balance = float(input("Enter the amount you want to add in your account:"))
    else:
        pass 
    take_address = input("Enter your address: ")
    take_email = input("Enter your email: ")
    customer_id = random.randint(200000,888888)
    mydata = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database = 'bank_management_system'
        )
    cursor1 = mydata.cursor()
    pan_table ="insert into pan_records(first_name,last_name,mobile_number,pan_number) values(%s,%s,%s,%s);"
    insert_pan_table = (take_fname,take_lname,take_mobileNo,take_pan)

    customer_table = "insert into customer(customer_id,first_name,last_name,email,phone_number,pan,address) values(%s,%s,%s,%s,%s,%s,%s);"
    insert_customer_data = (customer_id,take_fname,take_lname,take_email,take_mobileNo,take_pan,take_address)
    ac_no = random.randint(40000000,99999999)
    account_table = "insert into accounts(customer_id,account_number,balance) values(%s,%s,%s);"
    insert_account_table = (customer_id,ac_no,take_balance)
    cursor1.execute(pan_table,insert_pan_table)
    cursor1.execute(customer_table,insert_customer_data)
    cursor1.execute(account_table,insert_account_table)
    mydata.commit()
