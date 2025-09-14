def atm():
    pin = 5672
    balance = 10000  # starting balance
    temp = int(input("Enter Your Pin : "))

    if pin == temp:
        print("Welcome to Indian Bank!")
        print("1. Withdraw\n2. Deposit\n3. Check Balance")

        ch = int(input("Enter Your Choice : "))

        if ch == 1:
            get = int(input("Enter the Amount You want to Withdraw : "))
            if get <= balance:
                balance -= get
                print(f"Withdrawal Successful! Remaining Balance: ₹{balance}")
            else:
                print("Insufficient Balance!")

        elif ch == 2:
            put = int(input("Enter the Amount You want to Deposit : "))
            balance += put
            print(f"Deposit Successful! New Balance: ₹{balance}")

        elif ch == 3:
            print(f"Your Account Balance is ₹{balance}")

        else:
            print("Enter the Choice Correctly!")

    else:
        print("Wrong pin!")


# Run the program
atm()
