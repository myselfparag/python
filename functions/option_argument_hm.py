#Nykaa

#User will provide you list of items they want to buy : "Lipstick", "Lip Balm", "Eyeliner", "Deo"

#Build a logic:
## If a item is in male list : assume price as 60, give 10% off
## If a item is in female list : assume price 100 give 20% off
## If a item is in unisex list : assume price as 120 give 5% off


## Calculate the total bill, ask for coupon, otherwise assume default coupon NYKAAIPO22, and give 10% off if bill > 500 otherwise don't

male = ["Beard Oil", "Trimmer", "Men Facewash", "Men Soap"]
female = ["Eyeliner", "Lipstick", "Lipbalm", "ColdCream"]
unisex = ["Deo", "Soap", "Perfume", "Sanitizer", "Shampoo"]


def bill_to_pay(bill,coupon = "NYKAAIPO22"):
    if bill >=  65 and coupon == "NYKAAIPO22":
        bill = bill - bill*0.1
    
    else:
        pass

    return bill


def bill_calculator(items):
    total_bill = 0
    print(items)
    for item in items:
        print(item)
        if item in male:
            price = 60
            discount = 0.1 * price
            bill = price - discount
            

        elif item in female:
            price = 100
            discount= 0.2 * price
            bill = price - discount
            
        elif item in unisex:
            price = 120
            discount = 0.05 * price
            bill = price - discount
            
        total_bill +=bill

    total_bill = bill_to_pay(total_bill)
 
    print(f"your total bill is: {total_bill}")




bill_calculator(["Deo","Soap"])


