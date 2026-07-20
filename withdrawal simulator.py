# Smart ATM Withdrawal Simulator

# Fixed bank balance
balance = 500.00

# Ask the user for the withdrawal amount
withdrawal = float(input("Enter the amount you want to withdraw (R): "))

# Check the withdrawal request
if withdrawal <= balance and withdrawal > 0:
    balance = balance - withdrawal
    print(f"Withdrawal successful! Remaining balance: R{balance:.2f}")
elif withdrawal <= 0:
    print("Invalid amount. You must withdraw more than R0.")
else:
    print("Declined. Insufficient funds.")