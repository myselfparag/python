#Write a program that calculated bribe on the challan amount
# challan_amount is more than 1200 and is a even number : you should ask for 60% of the challan
# challan_amount is less than 1200 and is a odd number : you should ask for 30% of the challan
#calculate the total_bribe collected for your children's school dress

import random
value = random.randint(200, 2000)
challan_values = [random.randint(200, 2000) for i in range(2)]
print(challan_values)
total = 0
for ele_challan_value in challan_values:
    if ele_challan_value > 1200 and ele_challan_value % 2 ==0:
        ele_challan_value = ele_challan_value * 0.6
    elif ele_challan_value < 1200 and ele_challan_value % 2 != 0:
        ele_challan_value = ele_challan_value * 0.3
    else:
        pass
    total = ele_challan_value + total
print(total)

