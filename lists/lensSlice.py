toppings = [
    "pepperoni",
    "pineapple",
    "cheese",
    "sausage",
    "olives",
    "anchovies",
    "mushrooms"
]

prices = [
    2,
    6,
    1,
    3,
    2,
    7,
    2
]

#Counting 2$ occurences
num_two_dollar_slices = prices.count(2)
#print(num_two_dollar_slices)

#Finding the length of toppings
num_pizzas = len(toppings)
#print(num_pizzas)

print("We sell" + " " + str(num_pizzas) + " " + "different kinds of pizza!")

#Creating a new two-dimenional list
pizza_and_prices = [
    [2, "pepperoni"],
    [6, "pineapple"],
    [1, "cheese"],
    [3, "sausage"],
    [2, "olives"],
    [7, "anchovies"],
    [2, "mushrooms"]
]

#print(pizza_and_prices)

#sorting new two_dimensional list
pizza_and_prices.sort()
#print(pizza_and_prices)

#storing the cheapest_pizza
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

#Most expensive_pizza

priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

#Removing the pizza we don't have anymore
pizza_and_prices.pop()
#print(pizza_and_prices)

#Adding a new pizza
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

#3 Cheapest pizzas
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)