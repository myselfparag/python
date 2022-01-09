### Zomato bill calculator
### User provides us two things : total bill and distance from your house

###distance from your house
### if within 2 km : charge 5% of total bill
### otherwise charge : 8% of total bill


### There is a catchup : user will just not pay total bill, he will pay total bill , delivery charges and taxes on total bill after coupon
### if user passes any coupon : use that, otherwise use NEWYEAR22 as coupon which gives you 18% off

def calculate_delivery_charge(total_bill, distance_km):
    if distance_km >= 2:
        delivery_charge = total_bill * 0.08
    else:
        delivery_charge = total_bill * 0.05

    return delivery_charge

def calculate_zomato_bill(total_bill, distance_km, coupon = "NEWYEAR22"):
    delivery_charge = calculate_delivery_charge(total_bill, distance_km)

    if coupon == "NEWYEAR22":
        # total_bill = total_bill - total_bill * 0.18, below line means the same thing
        total_bill -= total_bill * 0.18

    total_tax = total_bill * 0.12

    user_bill = total_bill + total_tax + delivery_charge


    print(f"You have to pay {user_bill}")



calculate_zomato_bill(100, 5, "SHARASHARARA")
