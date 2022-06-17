import json

def set_favorite_number():
    try:
        filename = 'text_files/favorite_number.json'
        favorite_number = input("\nWhat is your favorite number?: ")
    except ValueError:
        print("\nPlease enter a NUMBER!")
    else:
        with open(filename, 'w') as f_obj:
            json.dump(favorite_number, f_obj)
        print("Your favorite number has been set as " + str(favorite_number) +
            "!")

def get_favorite_number():
    filename = 'text_files/favorite_number.json'
    try:
        with open(filename) as f_obj:
            favorite_number = json.load(f_obj)
    except FileNotFoundError:
        return None
    except json.decoder.JSONDecodeError: 
        print("The JSON is empty.")
        set_favorite_number()  
    else:
        test_favorite_number()

def test_favorite_number():
    while True:
        filename = 'text_files/favorite_number.json'
        with open(filename) as f_obj:
            favorite_number = json.load(f_obj)
        correct = input("Is " + str(favorite_number) + 
            " still your favorite number?"
            + "(y/n): ")
        if correct == "y":
            print("Okay bye.")
            break
        elif correct == "n":
            print("Shoot.")
            set_favorite_number()
            break
        else:
            print("Please input (y/n).")

get_favorite_number()