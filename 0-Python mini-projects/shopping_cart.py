print("WELCOME TO OUR FAMOUS STORE")
print("*" * 30)

item = input("What item are you purchasing: ")
price = float(input(f"what is the price of {item}: $ "))
quantity = int(input(f"how many {item} are there: "))

print(f"added {quantity} {item}(s) to shopping cart!")
subtotal = quantity * price
print(f"Your total is: $ {subtotal}")
      
