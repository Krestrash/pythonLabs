import collections


class Bank:
    def __init__(self):
        self.client_accounts = {}
        self.clients = []
    def create_account(self, account):
        if self.client_accounts.get(account.get_owner_id()):
            for acc in self.client_accounts.get(account.get_owner_id()):
                if acc.get_currency() == account.get_currency():
                    print(f"Account with this currency already exists")
                    return
        else:
            self.client_accounts[account.get_owner_id()] = []
        self.client_accounts[account.get_owner_id()].append(account)

    def close_account(self, account):
        if self.client_accounts.get(account.get_owner_id()):
            self.client_accounts.get(account.get_owner_id()).remove(account)

    def add_client(self, client):
        self.clients.append(client)

    def get_accounts(self, client):
        accounts = self.client_accounts.get(client.get_id())
        if accounts:
            for account in accounts:
                print(f"Name: {account.get_name()}")
                print(f"Balance: {account.get_balance()}")
                print(f"Currency: {account.get_currency()}")

    def get_account(self, client, name):
        if self.client_accounts.get(account.get_owner_id()):
            for acc in self.client_accounts.get(client.get_id()):
                if acc.get_name() == name:
                    return acc
        return None

    def transfer_money(self, first_account, second_account, amount):
        if first_account.get_balance() < amount:
            print("Not enough money")
            return
        first_account.withdraw(amount)
        second_account.deposit(amount)
        print(f"Name: {first_account.get_name()}")
        print(f"Balance: {first_account.get_balance()}")
        print(f"Currency: {first_account.get_currency()}")
        print(f"Name: {second_account.get_name()}")
        print(f"Balance: {second_account.get_balance()}")
        print(f"Currency: {second_account.get_currency()}")

class Account:
    def __init__(self, name, owner_id, balance, currency):
        self.owner_id = owner_id
        self.balance = balance
        self.currency = currency
        self.name = name

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_owner_id(self):
        return self.owner_id

    def get_balance(self):
        return self.balance

    def get_currency(self):
        return self.currency

    def get_name(self):
        return self.name



class Client:
     def __init__(self, id, name):
        self.id = id
        self.name = name

     def get_id(self):
         return self.id

     def get_name(self):
         return self.name

bank = Bank()
while True:

    id = input("Enter ID: ")
    name = input("Enter name: ")
    client = Client(id, name)
    bank.add_client(client)
    str = input("What would you like to do? \n 1: Create account \n 2: Withdraw \n 3: Deposit \n 4: Close account \n 5: Transfer money  ")

    if str == "1":
        name = input("How would you like to name your account? ")
        curr = input("What is the currency of your account? ")
        account = Account(name, client.get_id(), 0, curr)
        bank.create_account(account)
        bank.get_accounts(client)

    if str == "2":
        print(f"Available accounts: {bank.get_accounts(client)}")
        account_name = input("From which would you like to withdraw? ")

        account  = bank.get_account(client, account_name)
        if account:
            amount = int(input("How much would you like to withdraw? "))
            if account.get_balance() >= amount:
                account.withdraw(amount)
            else:
                print("You don't have enough money")

    if str == "3":
        print(f"Available accounts: {bank.get_accounts(client)}")
        account_name = input("Where would you like to deposit? ")

        account = bank.get_account(client, account_name)
        if account:
            amount = int(input("How much would you like to deposit? "))
            account.deposit(amount)

    if str == "4":
        print(f"Available accounts: {bank.get_accounts(client)}")
        account_name = input("What account would you like to close? ")
        account = bank.get_account(client, account_name)
        if account:
            bank.close_account(account)

    if str == "5":
        print(f"Available accounts: {bank.get_accounts(client)}")
        first_account_name = input("From which account would you like to transfer? ")
        second_account_name = input("Where would you like to transfer? ")
        amount = int(input("How much would you like to transfer? "))
        first_account = bank.get_account(client, first_account_name)
        second_account = bank.get_account(client, second_account_name)
        if first_account and second_account:
            bank.transfer_money(first_account, second_account, amount)


