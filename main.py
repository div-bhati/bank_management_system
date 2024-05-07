import account_creation
import do_transactions

is_quit = False
while not is_quit:
    print("Welcome to the Bank")
    command = input('''PRESS 1 for account creation\nPRESS 2 for doing transactions\nTYPE "Quit" to exit.\n''')
    if command == '1':
        account_creation.insert_data()
    elif command == '2':
        do_transactions.do_transactions()
    elif command.lower() == 'quit':
        is_quit = True
    else:
        print("Invalid command. Please try again.\n")

print("Thank you for using the Bank. Goodbye!")
