# current_users = ["gomathig", "nazeer hussain", "nazeern", "harris nazeer", "admin"]
# new_users = ["harris nazeer", "nazeer hussain", "vighnesh"]

# if new_users:
# 	for new_user in new_users:
# 		if new_user in current_users:
# 			print("Hello " + new_user + ", thank you for logging in again.")
# 		else:
# 			print("The username " + new_user + " is available")
# else:
# 	print("There are no users to be logged in.")


numbers = [number for number in range(1,10)]
print(numbers)

for number in numbers:
	if number == 1:
		print(str(number) + "st")
	if number == 2:
		print(str(number) + "nd")
	if number == 3:
		print(str(number) + "rd")
	else:
		print(str(number) + "th")
