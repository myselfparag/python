##User has a list of items for which they want total bill => ["Deo", "Shampoo"]
##the catch here is that you cannot assume same price for all
##Now you have liberty to create your own price list


### Also now user can apply list of coupons.
### We have to make sure that we only apply one coupon that gives max discount.
products_with_price = {"Deo":200,"Shampoo":220,"Powder":150,"Soap":30,"Specs":1000}

COUPON_LIST = {"happyny22" : 10, "ny22flat" : 12, "spiderman22hm" : 13, "talent22" : 12}

# product_lis = input("Give the list of your product, please use space after each name")
# product_lis = product_lis.split(" ")

def tb_calculator(product):
    if product in products_with_price.keys():
        return products_with_price[product]

def coupon_applier(total_bill, coupon_codes):
    max_value = -1
    for cc in coupon_codes:
        if max_value < COUPON_LIST[cc]:
            print(f"Replacing {max_value} by {COUPON_LIST[cc]}, using_coupon_name : {cc}")
            max_value = COUPON_LIST[cc]
            
        
    return total_bill - (total_bill * max_value * 0.01)
    
product_list = ["Deo","Shampoo","Powder"]
coupon_codes = ["ny22flat", "spiderman22hm", "talent22"]
total_bill = 0
for pl in product_list:
    print(pl)
    product_cost = tb_calculator(pl)
    total_bill += product_cost

final_bill = coupon_applier(total_bill, coupon_codes)
print(f"Total Bill : {total_bill}, Bill after coupon {coupon_codes} : {final_bill}")


    
        
