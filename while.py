pizza_toppings = []

# while True:
# 	topping = input("\nWhat pizza topping would you like?" + 
# 		"\n(type 'stop' to exit):")
# 	if topping == 'stop':
# 		break
# 	else:
# 		pizza_toppings.append(topping)
# 		print(topping + " has been added to your list of toppings.")

# print("Your pizza toppings are: ")
# for topping in pizza_toppings:
# 	print(topping)

# while active:
# 	topping = input("\nWhat pizza topping would you like?" + 
# 		"\n(type 'stop' to exit):")
# 	if topping == 'stop':
# 		active = False
# 	else:
# 		pizza_toppings.append(topping)
# 		print(topping + " has been added to your list of toppings.")

# print("Your pizza toppings are: ")
# for topping in pizza_toppings:
# 	print(topping)

# sandwich_orders = ['ham', 'meatball parm', 'pastrami', 'hot dog', 'avocado toast', 'pastrami', 'grilled cheese', 'turkey provolone', 'pastrami']
# finished_sandwiches = []

# print("Sorry! There is no more pastrami.")
# while 'pastrami' in sandwich_orders:
# 	sandwich_orders.remove('pastrami')

# while sandwich_orders:
# 	order = sandwich_orders.pop()
# 	print('The ' + order.title() + ' sandwich is finished.')
# 	finished_sandwiches.append(order)

# print("\nThe final sandwich list is:")
# for sandwich in finished_sandwiches:
# 	print(sandwich)

poll_results = {}
polling_active = True
while polling_active:
	user = input("What is your name?:")
	result = input("If you could go to one place in the world, where would you go?:")
	poll_results[user] = result

	cancel = input("Are there more participants? (yes/ no)")
	if cancel == 'no':
		polling_active = False

print("\nPoll Results:")
for name, result in poll_results.items():
	print("\t" + name.title() + " wants to go to " + result.title())

