class Account:
    def __init__(self, username) -> None:
        self.username = username
        self.current_balance = 0
        self.transactions = []
        self.total_loan_taken = 0

    def deposit_money(self, amount):
        if amount > 0:
            self.current_balance += amount
            self.transactions.append(f"Total {amount} has been deposited in your balance")
            print(f"Congratulations!! {amount} is deposited. Your new balance is {self.current_balance}")
    
        else:
            print("No money added.")

    def withdraw_money(self, amount):
        if amount > 0:
            if amount <= self.current_balance:
                self.current_balance -= amount
                self.transactions.append(f"{amount} has been taken from your account.")
                print(f"Congratulations!! {amount} whitdraw succesful. Your new balance {self.current_balance}")
            
            else:
                print("Insufficiant balance.")
        else:
            print("Please enter a valid amount.")

    
    def check_balance(self):
        return self.current_balance

    def transfer_money(self, amount, receiver):
        if amount > 0:
            if amount <= self.current_balance:
                self.current_balance -= amount
                self.transactions.append(f"{amount} has been transfered to {receiver.username}")
                print(f"Your new balance is {self.current_balance}.")
                receiver.current_balance += amount
                receiver.transactions.append(f"{amount} added to your balance from {self.username}")

            else:
                print('Insufficiant balance.')
        else:
            print(f'Enter a valid amount.')

    def check_transactions(self):
        return self.transactions

    def loan_request(self, amount):
        max_loan = 2 * self.current_balance
        if amount > 0 and amount <= max_loan:
            self.current_balance += amount
            self.total_loan_taken += amount
            self.transactions.append(f"{amount} taken as loan succesfully. Your new balance {self.current_balance} and total loan payable {self.total_loan_taken}")

        else:
            print(f"Your are limited within {max_loan}.")

    def pay_loan(self, amount):
        if amount > 0:
            self.current_balance -= amount
            self.total_loan_taken -= amount
            self.total_loan_taken -= amount
            self.transactions.append(f"{amount} has been paid remaining payable balance {self.total_loan_taken}")

        else:
            print("Enter a valid amount.")

    def get_details(self):
        list = []
        list.append(f"Username : {self.username}")
        list.append(f"Account balance : {self.current_balance}")
        list.append(f"Total loan taken : {self.total_loan_taken}")
        return list

            