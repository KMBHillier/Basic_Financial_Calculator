import math

# Explain what Bond and Investment mean so the user can easily choose which function to use

print("Investment - To calculate the amount of interest you'll earn on your investment.")
print("Bond - To calculate the amount you'll have to pay on a home loan")
calculator_type = input("Choose either investment or bond to proceed: ")
valid_calculator_type = calculator_type.lower()

# Validate all possible correctly spelt answers by using the lower method so all forms of the word are correct
# Wrongly spelt answers should return an error message
# as some input requests are the same for investments and bonds I tried to make the variable names as clear as possible
# also wanted to make sure all capitalisation's of simple and compound return valid responses
# also wanted the printed statement to read as a sentence rather than just a number


if valid_calculator_type == "investment":
    investment_money = float(input("How much money will you be depositing:  "))
    investment_interest_rate = float(input("What is the interest rate:  "))
    investment_time = int(input("How many years will you hold this investment:  "))
    interest_type = str(input("Would you like simple or compound interest:  "))
    valid_interest_type = interest_type.lower()
    if valid_interest_type == "simple":
        simple_interest = investment_money * (1 + ((investment_interest_rate/100)*investment_time))
        print(f"In {investment_time} years, your investment will be worth" + " " + str(round(simple_interest, 2)))
    if valid_interest_type == "compound":
        compound_interest = investment_money * math.pow((1+(investment_interest_rate/100)),investment_time)
        print(f"In {investment_time} years, your investment will be worth" + " " + str(round(compound_interest, 2)))

# tried to simplify the equation by creating the monthly interest rate variable

elif valid_calculator_type == "bond":
    bond_house_value = float(input("How much does the house cost:  "))
    bond_interest_rate = float(input("What is the interest rate:  "))
    repayment_time = int(input("How many months will you take to repay the bond:  "))
    monthly_interest_rate = bond_interest_rate / 12
    bond_repayment = (monthly_interest_rate * bond_house_value) / (1 - (1 + monthly_interest_rate)**(-repayment_time))
    print("You will have to pay this amount each month:" + " " + str(round(bond_repayment,2)))

# Tried to make error message as clear as possible for the user

elif valid_calculator_type != "investment" or "bond":
    print("I'm sorry, that response is invalid. Please try again and enter either investment or bond.")
