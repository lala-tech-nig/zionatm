accountnumber = 1111111111
pin = 2016
deposit_amount = 1000

print("Welcome to Praise Bank")
print("Insert your Card")
print("Here is your Account Number :", accountnumber)
userpin = int(input("Input your pin number: "))
# print(type(userpin))


if userpin == pin:
    print("Access Granted")
    print("Select an Option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your current balance is $1000")
    elif choice == 2:
        deposit_amount = int(input("Enter the amount to deposit: "))
        print("Deposit successful. New balance is:", deposit_amount + 1000)
    elif choice == 3:
        withdraw_amount = int(input("Enter the amount to withdraw: "))
        if withdraw_amount > 1000:
            print("Insufficient funds. Your current balance is:", deposit_amount)
        else:
            print("Withdrawal successful. New balance is:", 1000 - withdraw_amount)
else:
    print("wrong pin number")
