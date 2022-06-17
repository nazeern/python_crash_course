# prompt = "If you provide your first name, we can search for your credit history."
# prompt += "\nWhat is your first name?: "
# name = input(prompt)
# print("Hi " + name + ", you have no credit history.")

name = input("Welcome to Nitin's amusement park! Do you want to ride a coaster?: ").lower()

if name == 'yes':
	height = int(input("Okay. Please enter your height in inches: "))
	if height < 60:
		print("Sorry bub, you need to be at least 60 inches tall to ride. Go play with the other kiddies.")
	elif height < 107:
		print("Okay, you're cool enough to ride. Plus, you get Lord Nitin's autograph. Now buzz off, mate.")
	else:
		print("Go away buddy, what are you, Hagrid?")
else:
	print("Okay, so why are you even here? Just leave.")

