from bank import Bank
from user_admin import Admin

def main():
    b = Bank()
    admin = Admin(b)

    while(True):
        print('1. Create new account.')
        print('2. Deposit.')
        print('3. Withdraw.')
        print('4. Check balance.')
        print('5. Transfer money.')
        print('6. View transaction history.')
        print('7. Request for loan.')
        print('8. Pay loan.')
        print('9. Check details of account.')
        print('10. Check total bank balance.')
        print('11. Check total loan amount.')
        print('12. Change loan status.')
        print('13. Exit.')

        choice = int(input("Enter your choice : "))
        if choice == 1:
            username = input("Enter your username : ")
            b.create_account(username)
            print(f"Succesfully created your account.")

        elif choice == 2:
            name = input("Enter your username : ")
            account = b.show_account(name)
            if account:
                amount = int(input("Enter the amount : "))
                account.deposit_money(amount)
                print("Depositted succesfully.")

            else:
                print("Account not found.")


        elif choice == 3:
            name = input('Enter your username : ')
            account = b.show_account(name)
            if account:
                amount = int(input('Enter the amount : '))
                account.withdraw_money(amount)
                print("Withdraw succesful.")
            else:
                print("Account not found.")

        elif choice == 4:
            name = input('Enter your username : ')
            account = b.show_account(name)
            if account:
                print(f"Your account balance is {account.check_balance()}")
            else:
                print('Account not found.')

        elif choice == 5:
            name = input("Enter the sender username : ")
            receiver = input("Enter the receiver username : ")
            account_sender = b.show_account(name)
            account_receiver = b.show_account(receiver)
            if account_sender and account_receiver:
                amount = int(input('Enter the amount : '))
                account_sender.transfer_money(amount, account_receiver)
                print("Transfer succesful.")
            else:
                print("Account not found.")

        elif choice == 6:
            name = input('Enter your username : ')
            account = b.show_account(name)
            if account:
                print("-------------Transaction History------------")
                transactions = account.check_transactions()
                for i in transactions:
                    print(i)
            else:
                print('Account not found.')

        elif choice == 7:
            name = input('Enter your username : ')
            account = b.show_account(name)
            if account:
                amount = int(input('Enter the amount of loan : '))
                account.loan_request(amount)
                print('Loan taken succesfully.')
            else:
                print('Account not found.')

        elif choice == 8:
            name = input('Enter your username : ')
            account = b.show_account(name)
            if account:
                amount = int(input('Enter the amount to pay loan : '))
                account.pay_loan(amount)
                print("Loan paid.")
            else:
                print("Account not found.")

        elif choice == 9:
            name = input('Enter the username : ')
            print(admin.check_account(name))

        elif choice == 10:
            print(f"Total bank balance is {admin.check_bank_balance()}.")

        elif choice == 11:
            print(f"Total loan given {admin.check_total_loan_given()}.")

        elif choice == 12:
            declare  = admin.switch_loan()

            if declare == 1:
                print(f"Loan is currently enable.")
            else:
                print(f"Loan is currently disable.")

        elif choice == 13:
            break

        else:
            print('Please enter a valid choice.')



if __name__ == '__main__':
    main()