# Print names from a list
names = ["Nitin", "Harris", "Amma", "Bappa"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# print message for the first name in the list
print("Hello " + names[0] + ", how are you?")

# print message for the last & second to last name in the list
print("Hello " + names[-1] + ", how are you?")
print("Hello " + names[-2] + ", how are you?")

# Add to the list using .append()
names.append("Uppa")
print(names)

del names[-1]
print(names)