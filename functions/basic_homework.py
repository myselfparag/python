### Write a function which takes in your travelling expense, 
### eating expense and generates a bill which is total of your expense plus 10 % of expense

def total_exp(travelling_exp,eating_exp):
    total_bill = travelling_exp + eating_exp
    additional_exp = total_bill * 0.1
    #sum_of_bills = additional_exp + total_bill
    print("Your total bill is ",additional_exp + total_bill )


travelling_exp = float(input("Enter your travelling expense:  "))
eating_exp = float(input("Enter your eating expense:  "))

total_exp(travelling_exp,eating_exp)
