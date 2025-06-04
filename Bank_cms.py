import random
customers={}

def add_customer():
    try:
        acc_num = random.randint(100000000, 999999999) #customer account
        while acc_num in customers.keys():
            acc_num = random.randint(100000000, 999999999)
        name = input("Enter customer name: ")
        acc_type = input("Enter account type (savings/current): ").lower()
        if acc_type not in ['savings', 'current']:
            print("Error: Invalid account type. Please enter 'savings' or 'current'.")
            return
        balance = float(input("Enter initial balance: "))
        min_balance = float(input("Enter minimum balance: "))
        if balance < min_balance:
            print(f"Error: Initial balance cannot be less than minimum balance ({min_balance}).")
            return
        phone = int(input("Enter customer phone number (Number Only): "))
        if len(str(phone))!=10:
            print("Error: Phone number must be 10 digits long and contain only numbers.")
            return
        email = input("Enter customer email: ")
        if '@' not in email or '.' not in email.split('@')[-1]:
            print("Error: Invalid email format.")
            return
        
        atm_pin = random.randint(1000, 9999) #atm pin
       
        customers[acc_num] = {
            'name': name,
            'acc_type': acc_type,
            'balance': balance,
            'min_balance': min_balance,
            'phone': phone,
            'email': email,
            'atm_pin': atm_pin
        }
        print(f"Customer added successfully with account number: {acc_num}")
    except ValueError:
        print("Error: Invalid Input")
        return
    
def update_customer():
    
    try:
        acc_num = int(input("Enter customer account number: "))
        if acc_num not in customers:
             print("Customer doesn't exist")
             return
        phone = int(input("Enter customer phone number (Number Only): ")) or customers[acc_num]['phone']
        if len(str(phone)) !=10:
            print("Error: Phone number must be 10 digits long and contain only numbers.")
            return
         
        email = input("Enter customer email: ") or customers[acc_num]['email']
        if '@' not in email or '.' not in email.split('@')[-1]:
            print("Error: Invalid email format.")
            return
        customers[acc_num]['phone'] = phone
        customers[acc_num]['email'] = email
        print(f"Customer details updated successfully for account number: {acc_num}")
         
    except ValueError:
        print("Error Invalid Input")
    except:
        print("Error: Unknown error occurred, could not update customer details"),
        return
            

def del_customer():
    try:
        acc_num = int(input("Enter customer account number to delete: "))
        if acc_num not in customers:
            print("Customer doesn't exist")
            return
        del customers[acc_num]
        print(f"Customer with account number {acc_num} deleted successfully.")

    except:
        print("Error: Invalid Input")
        return
    
   
def display_customer():
     #here key eq customers[acc_num]
    for key,value in customers.items():
        print(f"Account Number: {key} Name: {value['name']}, Account Type: {value['acc_type']}, Balance: {value['balance']}, Minimum Balance: {value['min_balance']}, Phone: {value['phone']}, Email: {value['email']}, ATM PIN: {value['atm_pin']}\n")
        
    
def search_customer():
    try:
        acc_num = int(input("Enter customer account number to search: "))
        if acc_num not in customers:
            print("Customer doesn't exist")
            return
        value = customers[acc_num]
        print(f"Account Number: {acc_num} Name: {value['name']}, Account Type: {value['acc_type']}, Balance: {value['balance']}, Minimum Balance: {value['min_balance']}, Phone: {value['phone']}, Email: {value['email']}, ATM PIN: {value['atm_pin']}\n")
    except ValueError:
        print("Error: Invalid Input")

    
def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Add Customer")
        print("2. Update Customer")
        print("3. Delete Customer")
        print("4. Display Customers")
        print("5. Search Customer")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_customer()
        elif choice == '2':
            update_customer()
        elif choice == '3':
            del_customer()
        elif choice == '4':
            display_customer()
        elif choice == '5':
            search_customer()
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")


#=====Customer functions=====
def cust_deposit():
    try:
        acc_num = int(input("Enter customer account number: "))
        if acc_num not in customers:
            print("Customer doesn't exist")
            return
        while True:

            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Error: Deposit amount must be greater than zero.")
                return
            elif amount > 50000:
                print("Enter the PAN details for deposits over 50,000.")
                pan = input("Enter PAN number: ")
                customers[acc_num]['pan'] = pan
                print(f"PAN {pan} recorded for account number {acc_num}.") 
                        
            customers[acc_num]['balance'] += amount
            available_balance = customers[acc_num]['balance'] - customers[acc_num]['min_balance']
            print(f"Deposited {amount} to account number {acc_num}. Available balance: {available_balance}")
            
            break
        return
    
    except :
        print("Error: Invalid Input, Retry")
        return
    
def cust_withdraw():
    try:
        acc_num = int(input("Enter customer account number: "))
        if acc_num not in customers:
            print("Customer doesn't exist")
            return
        while True:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Error: Withdrawal amount must be greater than zero.") 
                continue
            elif amount > customers[acc_num]['balance']- customers[acc_num]['min_balance']:
                print("Error: Insufficient funds.")
                continue
            else:
                customers[acc_num]['balance'] -= amount
                available_balance = customers[acc_num]['balance'] - customers[acc_num]['min_balance']
                print(f"Withdrew {amount} from account number {acc_num}. New Availble balance: {available_balance}")
                break
        return
    except :
        print("Error: Invalid Input, Retry")
        return


def cust_display():
    
    try:
        
        acc_num = int(input("Enter customer account number to display: "))
        if acc_num not in customers:
            print("Customer doesn't exist")
            return
        value = customers[acc_num]
        available_balance = value['balance'] - value['min_balance']
        print(f"Account Number: {acc_num} Name: {value['name']}, Account Type: {value['acc_type']}, Balance: {value['balance']}, Available Balance to Withdraw: {available_balance}, Phone: {value['phone']}, Email: {value['email']}, ATM PIN: ****\n")
    except ValueError:
        print("Error: Invalid Input")

def cust_transfer():
    try:
        from_acc = int(input("Enter your account number: "))
        if from_acc not in customers:
            print("Your account doesn't exist")
            return
        to_acc = int(input("Enter recipient's account number: "))
        if to_acc not in customers:
            print("Recipient's account doesn't exist")
            return
        amount = float(input("Enter amount to transfer: "))
        if amount <= 0:
            print("Error: Transfer amount must be greater than zero.")
            return
        elif amount > customers[from_acc]['balance']:
            print("Error: Insufficient funds.")
            return
        elif customers[from_acc]['balance'] - amount < customers[from_acc]['min_balance']:
            print(f"Error: Insufficient funds. Minimum balance of {customers[from_acc]['min_balance']} must be maintained.")
            return
        else:
            customers[from_acc]['balance'] -= amount
            customers[to_acc]['balance'] += amount
            print(f"Transferred Succesfully {amount} from account number {from_acc} to {to_acc}. New balance: {customers[from_acc]['balance']}")
    except ValueError:
        print("Error: Invalid Input")






def customer_menu():
    while True:
        print("\nCustomer Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer") 
        print("4. Display")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            cust_deposit()
        elif choice == '2':
            cust_withdraw()
        elif choice == '3':
            cust_transfer()
        elif choice == '4':
            cust_display()    
        elif choice == '4':
            print("Exiting Customer Menu.")
            return
        else:
            print("Invalid choice, please try again.")
# Bank CMS with Admin and Customer functionalities
def login():
    print("\nLogin Menu:")
    username = input("Enter username: ")
    password = input("Enter password: ")
    

    if username == "admin" and password == "password":
        print("Login successful Welcome Admin\n")
        admin_menu()
        
    elif username == "customer" and password == "customer123":
        print("Login successful Welcome Customer\n")
        customer_menu()
        
    else:
        print('Invalid Credentials')
        
    
if __name__ == "__main__":

    print("Welcome to the Bank CMS")

    print("Enter the login Credentials:")
    while True:
        login()
    