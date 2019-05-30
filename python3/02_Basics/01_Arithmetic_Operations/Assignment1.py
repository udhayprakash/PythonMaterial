#!/usr/bin/python
"""
Purpose: 
    Assignment 1:  
    Create a grocery store application where following commodities are sold.
        item        cost            quantity
        ---------------------------------------
        hair oil  67/1 ltr      ==> 3 ltrs 
        apples    12.3/1 dozen  ==> 8 dozen
        mangos    15 /1 piece   ==> 32 pieces
    HINT: dozen = 12

"""
# cost
cost_of_hair_oil =  67 #  ltr 
cost_of_apples = 12.3  # dozen
cost_of_mango = 15 # 1 piece 

# quantity 
qty_of_hair_oil = 3 # ltrs
qty_of_apples = 8 # dozen 
qty_of_mangos = 32 # pieces

# price = cost * quantity
sp_hair_oil = cost_of_hair_oil * qty_of_hair_oil
sp_apples = cost_of_apples * qty_of_apples
sp_mangos = cost_of_mango * qty_of_mangos

# print('sp_hair_oil')
# print(sp_hair_oil)
# print(sp_hair_oil2)

total_sp = sp_hair_oil + sp_apples + sp_mangos
# print('total_sp =')
# print(total_sp)

print('total_sp =', total_sp)

# assignment 2 
# discount = 17.35 % on hair oil 
# discount = 10.12 % on others 

# GST = 15.99 % 

