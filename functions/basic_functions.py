### This file is dedicated to creating basic function

def find_discount_tagline(total_bill):
    if total_bill >= 1000:
        print("Congratulations your lucky ass just won 10% off")
    elif total_bill >= 500 and total_bill < 1000:
        print("Congratulation guess what you just won 3% off")
    else:
        print("Congratulations!! you just won a lucky voucher which is worth 10rs")


def calculate_discount_amount(total_bill):
    if total_bill >= 1000:
        total_discount = total_bill * 0.10
    elif total_bill >= 500 and total_bill < 1000:
        total_discount = total_bill * 0.03
    else:
        total_discount = 10

    return total_discount

user_value = float(input("Enter the amount to find discount : "))
find_discount_tagline(user_value)

user_value_discount = calculate_discount_amount(user_value)
print(user_value_discount)


