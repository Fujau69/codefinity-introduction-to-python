seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100

#is item an overstock risk?
overstock_risk = seasonal and current_stock > high_stock_threshold
##print(overstock_risk)

#eligeable to distcount?
discount_eligible = not selling_well and not on_sale

##print(discount_eligible)

#make_discount
make_discount = overstock_risk or discount_eligible

print("Should the item be discounted?", make_discount)