#shopping_cart.py
#Imported to print checkout time
import datetime
#Time in imported to simulate thinking
import time
delay = 1.5



#database of store items
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#function that converts int, str, or float to USD format
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output

print("Hello and welcome to Mary's Market")

# INFO CAPTURE 
receiptSubTotal = 0
taxRate = .0875
productIDs = []
storeIDs = []

#puts all of the item IDs in the database into a list 
for ID in products:
  storeID = str(ID["id"])
  storeIDs.append(storeID)

while True:
    #Collecting users items
    productID = input("Please enter a product identifier. Type done if your shopping is complete").lower()
    #Cross reference to check if ID is valid or if user enters done
    #This avoids the program crashing because of invalid user input
    if productID in storeIDs or productID == "done":
        if productID == "done":
            break
        else:
            productIDs.append(productID)
    else:
        time.sleep(delay)
        print("Hmm...it appears, you've entered an invalid entry! Try again")

time.sleep(delay*1.5)


#RECEIPT PRINTOUT
print("")
print("")
print("")
print("---------------------------------")
print("MARY'S MARKET")
print("WWW.MARYS-MARKET.COM")
print("---------------------------------")
now = datetime.datetime.now()
print("CHECKOUT AT:", now.strftime("%Y-%m-%d %I:%M %p"))
print("---------------------------------")
print("SELECTED PRODUCTS:")
#Uses for loop to print out price and name based on id number
for productID in productIDs:
        corresponding_products = [item for item in products if str(item["id"])== str(productID)]
        corresponding_product = corresponding_products[0]
        receiptSubTotal = receiptSubTotal + corresponding_product["price"]
        print("..." + corresponding_product["name"] + " " + "(" + to_usd(corresponding_product["price"])+")")
print("---------------------------------")
print("SUBTOTAL:",to_usd(receiptSubTotal))
tax = taxRate * receiptSubTotal
print("TAX:",to_usd(tax))
receiptTotal = to_usd(tax + receiptSubTotal)
print("TOTAL:",receiptTotal)
print("---------------------------------")
print("THANKS, WE'LL SEE YOU AGAIN SOON")