##User has a list of items for which they want total bill => ["Deo", "Shampoo"]
##the catch here is that you cannot assume same price for all
##Now you have liberty to create your own price list


### Also now user can apply list of coupons.
### We have to make sure that we only apply one coupon that gives max discount.
products_with_price = {"Deo":200,"Shampoo":220,"Powder":150,"Soap":30,"Specs":1000}

COUPON_LIST = {"happyny22" : 10, "ny22flat" : 12, "spiderman22hm" : 13, "talent22" : 12}

## Expected Input : List of items
## Expected Output : Total bill after discount
product_name = input("Enter the name of product")
Coupon= input("ENTER THE COUPON FROM THE MENTIONED LIST")

def bill_calculator(product_name,Coupon):
    total_bill = 0
    for item in product_name:
        print(232)
        
