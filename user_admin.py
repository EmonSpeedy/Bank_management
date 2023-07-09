from bank import Bank

class Admin:
    def __init__(self, bank) -> None:
        self.b = bank

    def check_all_account(self):
        self.b.show_all_accounts()

    def check_account(self, username):
        account = self.b.show_account(username)

        if account:
            return account.get_details()
        else:
            return f"Not found."
        
    def check_bank_balance(self):
        total = 0
        for account in self.b.all_accounts:
            total += account.current_balance
        return total
    
    def check_total_loan_given(self):
        total = 0
        for account in self.b.all_accounts:
            total += account.total_loan_taken
        return total
    
    def switch_loan(self):
        if self.b.switch_loan_status == 1:
            self.b.swich_loan_status = 0
        else:
            self.b.switch_loan_status = 1

        return self.b.switch_loan_status
