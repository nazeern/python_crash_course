filename = 'text_files/guest.txt'

while True:
    name = input("\nName (enter 'q' at anytime to quit):")
    if name == 'q':
        break

    response = input("\nDo you like programming? (yes/ no):")
    if response == 'q':
        break
    
    print(name.title() + ", thank you for your response.")
    with open(filename, 'a') as file_object:
        file_object.write("\n" + name.title() + ": " + response.title())

