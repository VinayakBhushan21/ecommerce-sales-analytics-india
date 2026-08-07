# Variables holding basic business facts about a single order
order_id = "ORD000001"          # str (text)
sales_amount = 3350.89          # float (decimal number)
quantity = 1                    # int (whole number)
is_delivered = True             # bool (True/False)

print(type(order_id))
print(type(sales_amount))
print(type(quantity))
print(type(is_delivered))


sales_amount = 15000

if sales_amount >= 20000:
    order_tier = "High Value"
elif sales_amount >= 5000:
    order_tier = "Mid Value"
else:
    order_tier = "Low Value"

print(f"This order is: {order_tier}")


top_cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai"]

print(top_cities[0])          # first item
print(len(top_cities))        # how many items
top_cities.append("Pune")     # add a new city
print(top_cities)

for city in top_cities:
    print(f"Processing orders for city: {city}")

order = {
    "order_id": "ORD000001",
    "city": "Jaipur",
    "sales": 3350.89,
    "status": "Cancelled"
}

print(order["sales"])          # access by key
order["profit"] = 511.66       # add a new key
print(order)


def classify_order(sales_amount):
    """Takes a sales amount, returns its value tier."""
    if sales_amount >= 20000:
        return "High Value"
    elif sales_amount >= 5000:
        return "Mid Value"
    else:
        return "Low Value"

# Test it on a few sample values
print(classify_order(25000))
print(classify_order(8000))
print(classify_order(1200))


# Tuple: fixed, unchangeable collection - e.g. a fixed (city, state) pair
location = ("Jaipur", "Rajasthan")
print(location[0], location[1])

# Set: unique values only, no duplicates, no order - e.g. distinct payment modes seen
payment_modes_seen = {"UPI", "UPI", "Cash on Delivery", "Credit Card", "UPI"}
print(payment_modes_seen)     # duplicates automatically removed