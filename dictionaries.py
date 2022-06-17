# favorite_number = {'Harris': '5', 'Gomathi': '5', 'Nitin': '21', 'Nazeer': '7'}

# for name, number in favorite_number.items():
# 	print(name + "'s favorite number is " +
# 		number)

favorite_languages = {
	'Nitin': 'Python',
	'Nazeer': 'Scala',
	'Harris': 'Unknown',
	'Gomathi': 'Java'
	}
users = ['Nitin', 'Vighnesh', 'Regina', 'Harris', 'Spruha']

for user in users:
	if user in favorite_languages:
		print(user + ", thank you for participating in this survey!" + 
			"\nYour favorite coding language is " + 
			favorite_languages[user].lower())
	else:
		print(user + ", please participate in our survey.")