#!/usr/bin/python
"""
Purpose:  Grocery Store application

Store items:
    Rice
    wheat
"""
BAG = 50 # kgs

cost_of_rice = 10 # kg 
cost_of_wheat = 23 # kg

# qty_of_rice = 20 # kgs 
# qty_of_wheat = 45 #kgs 

qty_of_rice = 23 * BAG  # 23 bags
qty_of_wheat = 12 * BAG  # 12 bags

sp_rice = cost_of_rice * qty_of_rice
sp_wheat = cost_of_wheat * qty_of_wheat

total_sp = sp_rice + sp_wheat

print('Total cost =',total_sp)


















# # selling price
# rice_selling_price = 52  # per kg
# wheat_selling_price = 40 # per kg

# # quantity (in kgs)
# rice_quantity = 12
# wheat_quantity = 5

# # costs
# cost_of_rice = rice_selling_price * rice_quantity
# cost_of_wheat = wheat_selling_price * wheat_quantity


# # amount to pay
# total_cost = cost_of_rice + cost_of_wheat
# print("total cost is", total_cost)


# # discount of 12% 
# total_discount = (12/total_cost)  * 100
# print("total_discount", total_discount)

# final_price = total_cost - total_discount
# print("final Price", final_price)
