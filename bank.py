from user_account import Account

class Bank:
    def __init__(self) -> None:
        self.all_accounts = []
        self.switch_loan_status = 1

    def create_account(self, username):
        account = Account(username)
        self.all_accounts.append(account)

    def show_all_accounts(self):
        for account in self.all_accounts:
            print(account)

    def show_account(self, username):
        for account in self.all_accounts:
            if account.username == username:
                return account

        return None
                