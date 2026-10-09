print("Shopping Receipt")
print("-----------------------")
print("Item 1: $",162 * 1.2 )  # Price per weight
print("Item 2: $", 25 - 3)  # Discounted price
print("-----------------------")
subtotal = (162 * 1.2) + (25 - 3)
print("Subtotal: $", subtotal)
print("Tax (8%): $", subtotal * 0.08)
print("-----------------------")
print("Thank you for shopping!")