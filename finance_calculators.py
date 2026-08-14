import math

#investement calculators
#ask the user to calculater the amount of interest they will earn on their investment   
#ask the user to calculate the amount they will have to pay on a home loan (bond)

# if user selects investment, the program should calculate the amount of interest earned on the investment
# The program should ask the user to input:
# The amount of money they are depositing
# The interest rate (as a percentage)
# The number of years they plan on investing
# Whether they want simple or compound interest
# The program should then output the total amount of money they will have in the account at the end of the investment period
# The formulae used to calculate simple and compound interest are as follows:
# Simple Interest: A = P(1 + rt)
# Compound Interest: A = P(1 + r)^t
#where:
# A = the total amount after interest   
# P = the principal amount (the initial amount invested)
# r = the annual interest rate (in decimal form)
# t = the number of years the money is invested for


#check if user user selected investement or bond
def finance_calculators():
    print("Choose either 'investment' or 'bond' from the menu below to proceed:")
    print("investment - to calculate the amount of interest you'll earn on your investment")
    print("bond       - to calculate the amount you'll have to pay on a home loan")
    
    user_choice = input("Enter your choice here: ").strip().lower()      
    
    
    if user_choice == "investment":
        # Get investment details from the user  
        P = float(input("Enter the amount of money you are depositing: "))
        r = float(input("Enter the interest rate (as a percentage): ")) / 100
        t = int(input("Enter the number of years you plan on investing: "))
        interest_type = input("Do you want 'simple' or 'compound' interest? ").strip().lower()
        
        if interest_type == "simple":
            A = P * (1 + r * t)
        elif interest_type == "compound":
            A = P * math.pow((1 + r), t)
        else:
            print("Invalid interest type selected.")
            return
        
        print(f"The total amount after {t} years will be: {A:.2f}")
    
    elif user_choice == "bond":
        # Get bond details from the user
        P = float(input("Enter the present value of the house: "))
        r = float(input("Enter the annual interest rate (as a percentage): ")) / 100 / 12
        n = int(input("Enter the number of months you plan to take to repay the bond: "))
        
        # Calculate monthly repayment
        repayment = (r * P) / (1 - math.pow((1 + r), -n))
        
        print(f"The monthly repayment will be: {repayment:.2f}")
    
    else:
        print("Invalid choice. Please select either 'investment' or 'bond'.")
        
# Call the function to run the program

def get_float(prompt):
    """Ask for a positive float and handle invalid input."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_int(prompt):
    """Ask for a positive integer and handle invalid input."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a number greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")

# --- Main program ---

print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond       - to calculate the amount you'll have to pay on a home loan.")
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower().strip()

if user_choice == "investment":
    print("\n--- Investment Calculator ---")
    P = get_float("Enter the amount you are depositing (R): ")
    rate = get_float("Enter the interest rate (without % sign): ")
    t = get_int("Enter the number of years you plan on investing: ")
    interest_type = input("Enter the type of interest ('simple' or 'compound'): ").lower().strip()

    r = rate / 100  # Convert percentage to decimal

    if interest_type == "simple":
        A = P * (1 + r * t)
    elif interest_type == "compound":
        A = P * math.pow((1 + r), t)
    else:
        print("Invalid interest type. Please choose either 'simple' or 'compound'.")
        exit

    print(f"\n After {t} years at {rate:.2f}% interest, your total investment will be: R{A:.2f}")


elif user_choice == "bond":
    print("\n--- Bond Repayment Calculator ---")
    P = get_float("Enter the present value of the house (R): ")
    rate = get_float("Enter the annual interest rate (without % sign): ")
    n = get_int("Enter the number of months you plan to repay the bond: ")

    i = (rate / 100) / 12  # Monthly interest rate
    repayment = (i * P) / (1 - (1 + i) ** (-n))

    print(f"\n Your monthly repayment will be: R{repayment:.2f}")

else:
    print("Invalid selection. Please choose either 'investment' or 'bond'.")

    
    





    



