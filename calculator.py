price = 25
quantity = 4

print (f"Price: {price}")
print (f"Quantity: {quantity}")

total = price * quantity
print (f"Total: {total}")

is_expensive = total > 50
print (f"Is expensive ? {is_expensive}")

if is_expensive:
    print("This order is expensive !")

else:
    print("This order is affordable !")

for i in range (quantity):
    print(f"Checking the item {i+1}")

prices = [25, 40, 15, 60] #List
print (f"{prices}")
print (prices[0])
print (prices[2])

readings = {"voltage": 3.3, "current": 0.5, "module": "X_123"} #Dictionary
print (f"Voltage: {readings['voltage']}")
print (readings['module'])

def calculate_total (price, quantity): #defining a function
    return price * quantity

total_1 = calculate_total(25,4) #using the function
total_2 = calculate_total(10,2)


print(total_1)
print(total_2)

from helpers import greet_engineer #importing functions from another file

print(greet_engineer("Maniteja_Rayabarapu"))

try:
    result = 10/0
    print(result)
except ZeroDivisionError:
    print("OOPS...!")
    print("Cannot divide by zero !")