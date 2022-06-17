# def make_shirt(size='large', message='I love Python'):
# 	print("The shirt is a " + size + " with the message " + 
# 		message + " printed on it.")

# make_shirt('medium', 'Carpe Diem')
# make_shirt(message='Thug Life', size='small')
# make_shirt()


# def city_country(city, country):
# 	print("\n" + city.title() +
# 		", " + country.title())

# city_country('Edison', 'United States')


# def make_album(artist_name, album_title, num_records=''):
# 	album = {'artist name': artist_name, 'album title': album_title}
# 	if num_records:
# 		album['number of records'] = num_records
# 	return album

# while True:
# 	print("\nPlease enter your favorite album's information (enter 'q' to quit at any time):")

# 	name = input("Artist name:")
# 	if name == 'q':
# 		break
# 	title = input("Album title:")
# 	if title == 'q':
# 		break
# 	records = input("Number of records (leave blank if unknown):")
# 	if records == 'q':
# 		break

# 	your_album = make_album(name, title, records)
# 	for k, v in your_album.items():
# 		print("\nThe " + k + " is " + v.title())
	

def show_magicians(magician_names):
	print("\nThe magicians are:")
	for magician in magician_names:
		print("\t" + magician)

def make_great(magician_names):
	length = len(magician_names)
	for i in range(0, length):
		magician_names[i] = magician_names[i] + " the Great"
	return magician_names

magicians = ['Eduardo', 'David', 'Jeremy', 'Pow Pow']

# great_magicians = make_great(magicians[:])
# show_magicians(magicians)
# show_magicians(great_magicians)


# def make_sandwich(*toppings):
# 	print("\nThe items on the sandwich are:")
# 	for topping in toppings:
# 		print("\t- " + topping)

# make_sandwich('olives', 'lettuce', 'tomato', 'ham', 'provolone', 'turkey')


# def build_profile(f_name, l_name, **user_info):
# 	user = {}
# 	user["First name"] = f_name
# 	user["Last name"] = l_name
# 	for k, v in user_info.items():
# 		user[k] = v
# 	return user

# user1 = build_profile('Nitin', 'Nazeer', location='Edison', education='high school', height='5 feet 7 inches')
# for k, v in user1.items():
# 	print(k.title() + ": " + v)


