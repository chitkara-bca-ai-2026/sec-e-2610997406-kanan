product_name = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
total = price * quantity
total_str = str(total)

print("===Data Types===")
print("Product name type:",type(product_name))
print("Price type:",type(price))
print("Quantity type:",type(quantity))
print("Total type:",type(total))
print("Total string type:",type(total_str))

print("===== INVOICE =====")
print("Product Name:",product_name)
print("Price:",price)
print("Quantity:",quantity)
print("Total Amount: ₹" + total_str)
print("==================")