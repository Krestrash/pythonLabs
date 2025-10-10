import collections

class InsufficientFundsError(Exception):
    pass


class AccountNotFoundError(Exception):
    pass


class CurrencyAccountExistsError(Exception):
    pass


class ClientNotFoundError(Exception):
    pass


class InvalidCurrencyError(Exception):
    pass




class Account:
    def __init__(self, name, owner_id, balance, currency):
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным.")
        self.owner_id = owner_id
        self.balance = balance
        self.currency = currency
        self.name = name

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        if self.balance < amount:
            raise InsufficientFundsError(f"Недостаточно средств. Текущий баланс: {self.balance:.2f} {self.currency}")
        self.balance -= amount


    def get_owner_id(self):
        return self.owner_id

    def get_balance(self):
        return self.balance

    def get_currency(self):
        return self.currency

    def get_name(self):
        return self.name

    def __str__(self):
        return f"{self.name} ({self.currency}): {self.balance:.2f}"


class Client:
    def __init__(self, client_id, name):
        self.id = client_id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name


class Bank:
    EXCHANGE_RATES = {
        "EUR": 1.0,
        "USD": 1.08,
        "GBP": 0.86,
        "BYN": 3.47
    }

    ALLOWED_CURRENCIES = list(EXCHANGE_RATES.keys())

    def __init__(self):
        self.client_accounts = {}
        self.clients = {}

    def _convert_currency(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount

        rate_from = self.EXCHANGE_RATES.get(from_currency)
        rate_to = self.EXCHANGE_RATES.get(to_currency)

        if not rate_from or not rate_to:

            raise InvalidCurrencyError("Одна из валют не поддерживается для конвертации.")


        amount_in_eur = amount / rate_from


        result = amount_in_eur * rate_to

        return result

    def create_account(self, account):
        currency = account.get_currency().upper()
        if currency not in self.ALLOWED_CURRENCIES:
            raise InvalidCurrencyError(
                f"Валюта '{currency}' не поддерживается. Разрешенные: {', '.join(self.ALLOWED_CURRENCIES)}")

        owner_id = account.get_owner_id()

        if owner_id not in self.client_accounts:
            self.client_accounts[owner_id] = []


        for acc in self.client_accounts[owner_id]:
            if acc.get_currency() == currency:
                raise CurrencyAccountExistsError(f"Счет в валюте '{currency}' уже существует для этого клиента.")


        account.currency = currency
        self.client_accounts[owner_id].append(account)
        print(f"Счет '{account.get_name()}' в {currency} создан успешно.")

    def close_account(self, account):
        owner_id = account.get_owner_id()
        if owner_id in self.client_accounts:
            try:
                self.client_accounts[owner_id].remove(account)
                print(f"Счет '{account.get_name()}' закрыт успешно.")
                if not self.client_accounts[owner_id]:
                    del self.client_accounts[owner_id]
            except ValueError:
                raise AccountNotFoundError("Счет не найден для этого клиента.")
        else:
            raise AccountNotFoundError("У клиента нет счетов.")

    def add_client(self, client):
        client_id = client.get_id()
        if client_id not in self.clients:
            self.clients[client_id] = client
            return True
        return False

    def get_accounts(self, client_id):
        return self.client_accounts.get(client_id, [])

    def print_accounts(self, client_id):
        accounts = self.get_accounts(client_id)
        if accounts:
            print("\n--- Доступные счета ---")
            for i, account in enumerate(accounts):
                print(f"[{i + 1}] {account}")
            print("--------------------------")
        else:
            print("У клиента нет доступных счетов.")
        return accounts

    def get_account(self, client_id, name):
        accounts = self.client_accounts.get(client_id)
        if accounts:
            for acc in accounts:
                if acc.get_name() == name:
                    return acc
        return None

    def transfer_money(self, first_account, second_client_id, second_account_name, amount):

        if second_client_id not in self.clients:
            raise ClientNotFoundError(f"Клиент с ID '{second_client_id}' не найден.")

        second_account = self.get_account(second_client_id, second_account_name)

        if not second_account:
            raise AccountNotFoundError(
                f"Счет получателя '{second_account_name}' не найден для клиента ID '{second_client_id}'.")

        if amount <= 0:
            raise ValueError("Сумма перевода должна быть положительной.")


        from_currency = first_account.get_currency()
        to_currency = second_account.get_currency()

        amount_to_withdraw = amount
        amount_to_deposit = amount
        conversion_info = ""

        if from_currency != to_currency:
            amount_to_deposit = self._convert_currency(amount, from_currency, to_currency)
            conversion_info = (
                f"\nКурс: 1 {from_currency} = {self.EXCHANGE_RATES[to_currency] / self.EXCHANGE_RATES[from_currency]:.4f} {to_currency}\n"
                f"Конвертация: {amount:.2f} {from_currency} -> {amount_to_deposit:.2f} {to_currency}"
            )


        first_account.withdraw(amount_to_withdraw)

        second_account.deposit(amount_to_deposit)

        print("\n--- Перевод успешен ---")
        print(conversion_info)
        print(f"Счет отправителя: {first_account}")
        print(f"Счет получателя: {second_account}")
        print("---------------------------")

    def generate_statement(self, client):
        client_id = client.get_id()
        accounts = self.get_accounts(client_id)

        filename = f"statement_{client_id}.txt"
        total_balance = collections.defaultdict(float)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"*** Банковская выписка для {client.get_name()} (ID: {client_id}) ***\n\n")
            f.write("--- Детали счетов ---\n")

            if not accounts:
                f.write("Активные счета не найдены.\n")
                print("Счета не найдены для создания выписки.")
                return

            for account in accounts:
                balance = account.get_balance()
                currency = account.get_currency()
                f.write(f"Название счета: {account.get_name()}\n")
                f.write(f"Баланс: {balance:.2f} {currency}\n")
                f.write(f"Валюта: {currency}\n")
                f.write("-" * 20 + "\n")


                total_in_eur = self._convert_currency(balance, currency, "EUR")
                total_balance["EUR"] += total_in_eur

            f.write("\n--- Суммарный баланс ---\n")
            total_eur = total_balance["EUR"]
            f.write(f"Общий баланс в EUR: {total_eur:.2f}\n")
            f.write(f"Общий баланс в USD: {self._convert_currency(total_eur, 'EUR', 'USD'):.2f}\n")
            f.write(f"Общий баланс в BYN: {self._convert_currency(total_eur, 'EUR', 'BYN'):.2f}\n")

            print(f"Выписка успешно сохранена в файл {filename}")



bank = Bank()

client_a = Client("1001", "Марк")
bank.add_client(client_a)
bank.create_account(Account("Основа", "1001", 1500.00, "EUR"))
bank.create_account(Account("Доллары", "1001", 500.00, "USD"))

client_b = Client("1002", "Андрей")
bank.add_client(client_b)
bank.create_account(Account("Рубли", "1002", 10500.00, "BYN"))

while True:
    print("\n" + "=" * 40)
    user_id = input("Введите Ваш ID клиента (или 'exit' для выхода): ").strip()
    if user_id.lower() == 'exit':
        break

    client = bank.clients.get(user_id)
    if not client:
        print(f"ID клиента {user_id} не найден.")
        new_name = input("Введите Ваше имя для регистрации нового клиента: ").strip()
        client = Client(user_id, new_name)
        bank.add_client(client)
        print(f"Добро пожаловать, {client.get_name()}! Вы зарегистрированы.")

    print(f"\nС возвращением, {client.get_name()}!")

    menu_choice = input(
        "Что Вы хотите сделать? \n"
        " 1: Открыть счет \n"
        " 2: Снять средства \n"
        " 3: Пополнить счет \n"
        " 4: Закрыть счет \n"
        " 5: Перевести деньги \n"
        " 6: Просмотреть счета \n"
        " 7: Сформировать выписку \n"
        " 8: Сменить клиента (Выйти) \n"
        "> "
    ).strip()

    if menu_choice == "8":
        continue

    current_client_id = client.get_id()

    try:

        if menu_choice == "1":
            name = input("Как назвать Ваш счет? ").strip()
            if not name: raise ValueError("Название счета не может быть пустым.")

            print(f"Доступные валюты: {', '.join(bank.ALLOWED_CURRENCIES)}")
            curr = input("Какая валюта счета (например, EUR, USD)? ").strip().upper()
            if not curr: raise ValueError("Валюта не может быть пустой.")
            if curr not in bank.ALLOWED_CURRENCIES:
                raise InvalidCurrencyError(f"Валюта '{curr}' не поддерживается.")

            initial_balance_str = input("Начальный депозит (необязательно, по умолчанию 0): ").strip()
            initial_balance = float(initial_balance_str) if initial_balance_str else 0.0

            account = Account(name, current_client_id, initial_balance, curr)
            bank.create_account(account)


        elif menu_choice in ["2", "3", "4", "5"]:

            available_accounts = bank.print_accounts(current_client_id)
            if not available_accounts:
                continue


            source_account_name = input("Введите НАЗВАНИЕ Вашего счета: ").strip()
            source_account = bank.get_account(current_client_id, source_account_name)

            if not source_account:
                raise AccountNotFoundError(f"Счет '{source_account_name}' не найден для Вашего ID.")


            if menu_choice == "2":
                amount = float(input("Сколько Вы хотите снять? ").strip())
                source_account.withdraw(amount)
                print(f"Снятие успешно. Новый баланс: {source_account}")


            elif menu_choice == "3":
                amount = float(input("Сколько Вы хотите внести? ").strip())
                source_account.deposit(amount)
                print(f"Пополнение успешно. Новый баланс: {source_account}")


            elif menu_choice == "4":
                confirm = input(f"Вы уверены, что хотите закрыть '{source_account_name}'? (да/нет): ").strip().lower()
                if confirm == 'да':
                    bank.close_account(source_account)
                else:
                    print("Закрытие счета отменено.")


            elif menu_choice == "5":
                target_client_id = input("Введите ID клиента-ПОЛУЧАТЕЛЯ: ").strip()
                target_account_name = input("Введите НАЗВАНИЕ счета ПОЛУЧАТЕЛЯ: ").strip()

                if target_client_id == current_client_id and target_account_name == source_account_name:
                    print("Нельзя перевести средства на тот же самый счет.")
                    continue

                amount = float(input(f"Сколько {source_account.get_currency()} Вы хотите перевести? ").strip())


                bank.transfer_money(source_account, target_client_id, target_account_name, amount)


        elif menu_choice == "6":
            bank.print_accounts(current_client_id)


        elif menu_choice == "7":
            bank.generate_statement(client)

        else:
            print("Неверный выбор. Пожалуйста, выберите опцию от 1 до 8.")

    except (ValueError, InsufficientFundsError, AccountNotFoundError, CurrencyAccountExistsError, ClientNotFoundError,
            InvalidCurrencyError) as e:
        print(f"\n!!! ОШИБКА: {e} !!!")
    except Exception as e:
        print(f"\n!!! Произошла непредвиденная ошибка: {e} !!!")