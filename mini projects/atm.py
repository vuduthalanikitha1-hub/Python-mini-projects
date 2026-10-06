balance = 1000

while True:

    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        print("Your balance is:", balance)

    elif choice == "2":

        amount = int(input("Enter deposit amount: "))

        balance += amount

        print("Money deposited successfully")

    elif choice == "3":

        amount = int(input("Enter withdraw amount: "))

        if amount <= balance:

            balance -= amount

            print("Please collect your cash")

        else:

            print("Insufficient balance")

    elif choice == "4":

        print("Thank you for using ATM")
        break

    else:

        print("Invalid choice")