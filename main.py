user_name = input('Enter your name: ')
amount1 = float(input("Enter your amount 1: "))
amount2 = float(input("Enter your amount 2: "))
amount3 = float(input("Enter your amount 3: "))
amount4 = float(input("Enter your amount 4: "))
amount5 = float(input("Enter your amount 5: "))

total_amount = amount1 + amount2 + amount3 + amount4 + amount5

if total_amount > 0:
    print(f"{user_name}, your account balance is ${total_amount:.2f}")

elif total_amount == 0:
    print(f"{user_name}, your account balance is zero.")

else:
    print(f"{user_name}, your account is overdrawn by ${abs(total_amount):.2f}")
