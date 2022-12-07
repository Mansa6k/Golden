loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
number_of_loans = len(loan_costs)
print(f'The number of loans in the list is: {number_of_loans}')

# What is the total of all loans?
total_loan_cost = sum(loan_costs)
print(f'The total cost of all loans is: {total_loan_cost}')

# What is the average loan amount from the list?
average_loan_cost = total_loan_cost / number_of_loans
print(f'The average loan cost is: {average_loan_cost}')

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print(f'Future Value: {future_value}')
print(f'Remaining Months: {remaining_months}')

# Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the monthly version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
discount_rate = 0.2
present_value = future_value / (1 + discount_rate / 12) ** remaining_months

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
if present_value >= loan["loan_price"]:
    print("The loan is worth at least the cost to buy it.")
else:
    print("The loan is too expensive and not worth the price.")

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Define a new function that will be used to calculate present value.
# This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
# The function should return the `present_value` for the loan.
def present_value_calculator(future_value, remaining_months, annual_discount_rate):
    monthly_discount_rate = annual_discount_rate / 12
    present_value = future_value / (1 + monthly_discount_rate) ** remaining_months
    return present_value


# Use the function to calculate the present value of the new loan given below.
# Use an `annual_discount_rate` of 0.2 for this new loan calculation.
present_value = present_value_calculator(
    future_value=new_loan["future_value"],
    remaining_months=new_loan["remaining_months"],
    annual_discount_rate=0.2
)
print(f"The present value of the loan is: {present_value}")

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create an empty list called `inexpensive_loans`
inexpensive_loans = []

# Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)

# Print the `inexpensive_loans` list
print(f'Inexpensive Loans: {inexpensive_loans}')

import csv
from pathlib import Path

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
with open(output_path, "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())

