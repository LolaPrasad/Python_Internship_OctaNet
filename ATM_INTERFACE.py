class Account:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def display_balance(self):
        return f"Your balance is ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: +${amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -${amount}")
        else:
            return "Insufficient funds"

    def transfer(self, recipient, amount):
        if amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transfer to {recipient.user_id}: -${amount}")
            recipient.transaction_history.append(f"Transfer from {self.user_id}: +${amount}")
        else:
            return "Insufficient funds"

    def get_transaction_history(self):
        return self.transaction_history


class ATM:
    def __init__(self):
        self.users = {}  # Map user_id to Account

    def create_account(self, user_id, pin):
        if user_id not in self.users:
            self.users[user_id] = Account(user_id, pin)
            return "Account created successfully"
        else:
            return "User ID already exists. Please choose another."

    def login(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            return self.users[user_id]
        else:
            return None


def main():
    atm = ATM()

    while True:
        print("\n1. Create Account\n2. Login\n3. Quit")
        choice = input("Enter your choice No : ")

        if choice == '1':
            user_id = input("Enter a user ID: ")
            pin = input("Enter a PIN: ")
            result = atm.create_account(user_id, pin)
            print(result)

        elif choice == '2':
            user_id = input("Enter your user ID: ")
            pin = input("Enter your PIN: ")
            user_account = atm.login(user_id, pin)

            if user_account:
                while True:
                    print("\n1. Display Balance\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Transactions History\n6. Quit")
                    operation = input("Enter your choice: ")

                    if operation == '1':
                        print(user_account.display_balance())

                    elif operation == '2':
                        amount = float(input("Enter the deposit amount: "))
                        user_account.deposit(amount)
                        print("Deposit successful.")

                    elif operation == '3':
                        amount = float(input("Enter the withdrawal amount: "))
                        result = user_account.withdraw(amount)
                        if result:
                            print(result)
                        else:
                            print("Withdrawal successful.")

                    elif operation == '4':
                        recipient_id = input("Enter the recipient's user ID: ")
                        recipient = atm.users.get(recipient_id)
                        if recipient:
                            amount = float(input("Enter the transfer amount: "))
                            result = user_account.transfer(recipient, amount)
                            if result:
                                print(result)
                            else:
                                print("Transfer successful.")
                        else:
                            print("Recipient not found.")

                    elif operation == '5':
                        print("Transaction History:")
                        for transaction in user_account.get_transaction_history():
                            print(transaction)

                    elif operation == '6':
                        break

                    else:
                        print("Invalid choice. Please try again.")

            else:
                print("Invalid user ID or PIN. Please try again.")

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
