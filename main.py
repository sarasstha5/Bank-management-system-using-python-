import json
import random
import string
from pathlib import Path


class Bank:
    database = Path("data.json")
    data = []
    
    try:
        if database.exists():
            with open(database, "r") as file:
                data = json.load(file)         #loads the data from the json file and stores it in the variable data 
        else:
            print("No database found.")
    except Exception as e:
        print(f"Error loading database: {e}")
    
    @staticmethod
    def update():
        try:
            with open(Bank.database, "w") as file:
                file.write(json.dumps(Bank.data))          #dumps the data into the json file
        except Exception as e:
            print(f"Error updating database: {e}")
            
    #function to generate a random account number
    @staticmethod
    def generate_account_number():
        alpha = random.choices(string.ascii_uppercase, k=3) #generates a random string of 3 uppercase letters
        num = random.choices(string.digits, k=4)            #generates a random string of 4 digits
        symbol = random.choices("@#$%&", k=1)               #generates a random symbol from the given list
        id = alpha + num + symbol                          #concatenates the three strings to form the account number
        random.shuffle(id)                                 #shuffles the characters in the account number to make it more random
        return "".join(id)                                 #joins the characters in the shuffled list to form a string and returns it as the account number
     
    #function to create a new bank account
    def create_account(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        address = input("Enter your address: ")
        email = input("Enter your email: ")
        pin = input("Set a 4-digit PIN for your account: ")
        account_details = {
            "name": name,
            "age": age,
            "address": address,
            "email": email,
            "pin": pin,
            "account_number": Bank.generate_account_number(),
            "balance": 0
        }

        if age < 18 or len(str(pin)) != 4:
            print("Invalid age or PIN. Account creation failed.")
        else:
            print("Creating account...")
            Bank.data.append(account_details)

            Bank.update()

            print(f"Account created successfully! Your account :")
            for i in account_details:
                print(f"{i}: {account_details[i]}")
            print("Please keep your account number and PIN safe.")
    
    #function to deposit money into the account
    def deposit(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")
        amount = int(input("Enter the amount to deposit: "))

        for account in Bank.data:
            if account["account_number"] == account_number and account["pin"] == pin:
                account["balance"] += amount
                Bank.update()
                print(f"Deposit successful! Your new balance is: {account['balance']}")
                return
        
        print("Invalid account number or PIN. Deposit failed.")
    
    #function to withdraw money from the account
    def withdraw(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")
        amount = int(input("Enter the amount to withdraw: "))

        for account in Bank.data:
            if account["account_number"] == account_number and account["pin"] == pin:
                if account["balance"] >= amount:
                    account["balance"] -= amount
                    Bank.update()
                    print(f"Withdrawal successful! Your new balance is: {account['balance']}")
                else:
                    print("Insufficient funds.")
                return

        print("Invalid account number or PIN. Withdrawal failed.")

    #function to check the details of the account
    def check_details(self):
        account = input("Enter your account number:")
        pin = input("enter the pin number: ")

        for i in Bank.data:
            if i["account_number"] == account and i["pin"] == pin:
                print("Account details:")
                for key, value in i.items():          #iterates through the key-value pairs in the account details and prints them in a formatted way
                    print(f"{key}: {value}")             
                return
            else:
                print("Invalid account number or PIN. Please try again.")
                return
    
    #function to update the account details
    def update_details(self):
        account = input("Enter your account number:")

        for detail in Bank.data:
            if detail["account_number"] == account:
                print("what do you want to update?")
                print("press 1 to update name")
                print("press 2 to update age")
                print("press 3 to update address")
                print("press 4 to update email")
                print("press 5 to update pin")

                num = int(input("enter the response:- "))

                if num == 1:
                    detail["name"] =input("Enter your new name: ")
                elif num == 2:
                    detail["age"] = input("Enter your new age: ")
                elif num == 3:
                    detail["address"] = input("Enter your new address: ")
                elif num == 4:
                    detail["email"] = input("Enter your new email: ")
                elif num == 5:
                    detail["pin"] = input("Enter your new 4-digit PIN: ")
                else:
                    print("Invalid response. Please try again.")
                    return
                Bank.update()
                print("Account details updated successfully!")
    
    #function to delete the account
    def delete_account(self):
        account = input("Enter your account number:")
        pin = input("enter the pin number: ")

        for i in Bank.data:
            if i["account_number"] == account and i["pin"] == pin:
                Bank.data.remove(i)
                Bank.update()
                print("Account deleted successfully!")
                return
        
        print("Invalid account number or PIN. Please try again.")
    



user = Bank()





print("press 1 to create bank account")
print("press 2 to deposit money")
print("press 3 to withdraw money")
print("press 4 to check the details of the account")
print("press 5 to update the account details")
print("press 6 to delete the account")

num = int(input("enter the response:- "))

if num == 1:
    user.create_account()
elif num == 2:
    user.deposit()
elif num == 3:
    user.withdraw()
elif num == 4:
    user.check_details()
elif num == 5:
    user.update_details()
elif num == 6:
    user.delete_account()