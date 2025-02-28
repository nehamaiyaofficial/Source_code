balance = float(input("Enter your bank account balance: "))
withdraw_amount = float(input("Enter the amount you want to withdraw: "))
if balance >= withdraw_amount:
    if withdraw_amount >= 1000:
        print("Transaction Successful! ₹", withdraw_amount, "withdrawn.")
        balance -= withdraw_amount  
        print("Remaining Balance: ₹", balance)
    else:
        print("Error! Minimum withdrawal amount is ₹1000.")
else:
    print("Insufficient balance! Transaction failed.")



