import mysql.connector
import random

def do_transactions():
    '''
    1 add balance 
    2 withdraw balance 
    3 transfer balance
    '''
    mydata = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database = 'bank_management_system'
        )
    cursor2 = mydata.cursor()

    sender = input("Enter your bank account number: ")
    print('''
To add balance yo your account PRESS 1
To withdraw balance from your account PRESS 2
To transfer the balance PRESS 3
For balance enquiry PRESS 9
''')
    k = int(input("Enter your response: "))
    if k == 1:
        add_bal = float(input("Enter the amount you want to add to your funds: "))
        sql_q2 = "update accounts set balance = balance +%s where account_number = %s;"
        values_add = (add_bal,sender)
        cursor2.execute(sql_q2,values_add)
        funds_added = f"{add_bal} successfully creditd to your account number {sender}"
        sql_global_query = "insert into transactions(sender,amount,transaction_description) values(%s,%s,%s);"
        data = (sender,add_bal,funds_added)
        cursor2.execute(sql_global_query,data)
    elif k == 2:
        withdraw_bal = float(input("Enter the amount you want to withdraw: "))
        sql_bal_enq = "select balance from accounts where account_number = %s;"
        cursor2.execute(sql_bal_enq, (sender,))
        result = cursor2.fetchone()  # Fetch the result of the query
        current_balance = float(result[0])  # Extract the current balance from the result
        if withdraw_bal > current_balance:
            print("Insufficient balance in the account!!")
            print("Transaction REJECTED!!")
        else:
            sql_withdrawl = "UPDATE accounts SET balance = balance - %s WHERE account_number = %s"
            values_2 = (withdraw_bal, sender)
            cursor2.execute(sql_withdrawl, values_2)
            print("Withdrawal Successful!!!!")
            new_balance = current_balance - withdraw_bal
            print(f"The remaining balance in your account number {sender} is {new_balance}")
            withdrawal_desc = f"{withdraw_bal} deducted from your account number {sender}"
            sql_global_query = "insert into transactions(sender, amount, transaction_description) values(%s, %s, %s);"
            data = (sender, withdraw_bal, withdrawal_desc)
            cursor2.execute(sql_global_query, data)

    elif k == 3:
        tranfer_bal = float(input("Enter the amount you need do transfer: "))
        receiver = input("Enter the receiver's account number: ")
        take_phone_no = input("Enter your phone number registered with bank: ") ##
        take_pan = input("Enter your PAN number: ").upper()
        tranaction_ref = input("Enter yes if you want to enter the message for transaction: ")
        if tranaction_ref == 'yes' or 'YES' or 'Yes':
            transaction_desc_1 = input("Enter the message you want to enter: ")
        elif tranaction_ref == 'no' or 'NO' or 'No':
            transaction_desc = f"{tranfer_bal} successfully transferred between {sender} to {receiver}."
            sql_global_query = "insert into transactions(sender,receiver,amount,transaction_description,pan_record,phone_no) values(%s,%s,%s,%s,%s,%s);"
            data = (sender,receiver,tranfer_bal,transaction_desc,take_pan,take_phone_no)
            cursor2.execute(sql_global_query,data)
        sql_q3 = 'update accounts set balance= balance + %s where account_number = %s'
        sql_q3_minus = "update accounts set balance = balance - %s where account_number = %s;"
        values_sql_q3_miuns = (tranfer_bal,sender)
        cursor2.execute(sql_q3_minus,values_sql_q3_miuns)
        val_sql_q3 = (tranfer_bal,receiver)
        cursor2.execute(sql_q3,val_sql_q3)
        print("Successfully tranferred!!")
        transaction_desc = f"{transaction_desc_1}."
        sql_global_query = "insert into transactions(sender,receiver,amount,transaction_description,pan_record,phone_no) values(%s,%s,%s,%s,%s,%s);"
        data = (sender,receiver,tranfer_bal,transaction_desc,take_pan,take_phone_no)
        cursor2.execute(sql_global_query,data)
    elif k == 9:
        sql_q1 = 'Select balance as "Balance" from accounts where account_number = %s;'
        cursor2.execute(sql_q1,sender)
    
    mydata.commit()
