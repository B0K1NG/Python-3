#Customers first names into a list called first_names
first_names =  ["Ainsley", "Ben", "Chani", "Depak"]

#Filling new list preferred_size with the following data
preferred_size = ["Small", "Large", "Medium"]

#Adding Depak’s size is "Medium"
preferred_size.append("Medium")
print(preferred_size)

#Creating a two-dimensional list
customer_data = [
    ["Ainsley", "Small", True], 
    ["Ben", "Large", False], 
    ["Chani", "Medium", True], 
    ["Depak", "Medium", False]
     
]
print(customer_data)

#"Chani" Requested to switch to regular shipping
customer_data[2][2] = False
print(customer_data)

#"Ben" Requested to remove True or False
customer_data[1].remove(False)
print(customer_data)

#Combine our existing list customer_data with our new customer 2d
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)