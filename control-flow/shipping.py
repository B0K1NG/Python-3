weight = 1.5

#Ground Shipping 🚚

if weight <= 2:
  cost_ground = weight * 1.50 + 20.00
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3.00 + 20.00
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4.00 + 20.00
else:
  cost_ground = weight * 4.75 + 20.00

#Checking if the function works correctly
#print(cost_ground)

#Ground Shipping Premium 🚚💨

cost_ground_premium = 125.00
print("The fee for the premium flat is: " + str(cost_ground_premium) + "$")

#Drone Shipping 🛸

if weight <= 2:
  cost_air = weight * 4.50
elif weight > 2 and weight <= 6:
  cost_air = weight * 9.00
elif weight > 6 and weight <= 10:
  cost_air = weight * 12.00
else:
  cost_air = weight * 14.25

#Checking if the function works correctly
#print(cost_air)

