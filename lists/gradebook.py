last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

subject = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

gradebook = [
    ["physics", 98],
    ["calculus", 97],
    ["poetry", 85],
    ["history", 88],
]

#print(gradebook)

#Adding grade for the computer science class
gradebook.append(["computer science", 100])
#print(gradebook)

#Adding grade for the visual arts class
gradebook.append(["visual arts", 93])
#print(gradebook)

#Accesing grade for visual arts and modifying the grade + 5
gradebook[-1][1] = "98"
#print(gradebook)

#Removing grade from poetry class new grading system Pass/Fail
gradebook[2].remove(85)
gradebook[2].append("Pass")
#print(gradebook)

#Adding last semester grades
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)