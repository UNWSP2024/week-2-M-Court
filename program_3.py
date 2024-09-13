#ask for item prices
item1 = float(input("Enter item price 1: "))
item2 = float(input("Enter item price 2: ")) 
item3 = float(input("Enter item price 3: "))
item4 = float(input("Enter item price 4: "))
item5 = float(input("Enter item price 5: ")) 
#add item prices
subtotal = item1 + item2 + item3 + item4 + item5
print("your subtotal is", subtotal)
#calculate 7% tax
tax = (item1 + item2 + item3 + item4 + item5) * 0.07
print(float("your tax is", tax)
#calculate total
total = tax + subtotal
print("your total is", total)