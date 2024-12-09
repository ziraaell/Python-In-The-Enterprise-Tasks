class BankAcount:
    def __init__(self, ID, name, surname, age, country, city):
        self.ID = ID
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country
        self.city = city
        self.funds = 0

    def display_not_enough_funds(self):
        print(f"Not enough funds\nYour current funds: {self.funds}\n")

    def add_money(self, cash_input):
        self.funds += cash_input
    
    def withdraw(self, cash_output):
        if self.funds - cash_output >= 0:
            self.funds -= cash_output
        else:
            self.display_not_enough_funds()
    
    def transfer_money(self, amount_money_to_transfer, to_client):
        self.withdraw(amount_money_to_transfer)
        to_client.add_money(amount_money_to_transfer)

    def __str__(self):
        return f'Bank account: name = {self.name}, surname: {self.surname}, age: {self.age}, country = {self.country}, city = {self.city}\nCurrent funds = {self.funds}\n'

class Bank:
    def __init__(self):
        self.bank_accounts = []

    def add_account(self, account_to_add):
        self.bank_accounts.append(account_to_add)
    
    def __str__(self):
        accounts_str = ''
        for account in self.bank_accounts:
            accounts_str += str(account)
        return accounts_str
    
if __name__ == "__main__":
    bank_account1 = BankAcount(1, "Jan", "Nowak", 42, "Poland", "Cracow")
    bank_account2 = BankAcount(2, "John", "Smith", 22, "England", "London")
    bank_account3 = BankAcount(3, "Trevor", "Philips", 50, "Canada", "Ottawa")
    bank = Bank()
    bank.add_account(bank_account1)
    bank.add_account(bank_account2)
    bank.add_account(bank_account3)

    bank_account1.add_money(300)
    bank_account2.add_money(15000)
    bank_account3.add_money(10000000)
    print(bank)

    bank_account1.withdraw(400)
    bank_account2.withdraw(5000)
    bank_account3.withdraw(1000000)
    print(bank)

    bank_account3.transfer_money(500, bank_account1)
    print(bank_account1)
    print(bank_account3)