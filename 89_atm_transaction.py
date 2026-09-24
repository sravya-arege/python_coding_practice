def atm_transaction(balance):
    while True:
        print("1. Check balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            print("Balance:", balance)
        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                print("Deposit successful.")
            else:
                print("Amount must be positive.")
        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            if 0 < amount <= balance:
                balance -= amount
                print("Withdrawal successful.")
            else:
                print("Invalid amount or insufficient balance.")
        elif choice == "4":
            return balance
        else:
            print("Invalid choice.")


initial_balance = float(input("Enter initial balance: "))
final_balance = atm_transaction(initial_balance)
print("Final balance:", final_balance)
