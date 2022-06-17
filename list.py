def retrieve_lines():
    try:
        filename = "text_files/list.txt"
    except FileNotFoundError:
        print("The file " + filename + " was not found.")
    else:
        with open(filename) as f_obj:
            lines = f_obj.readlines()
        message = ''
        print("\nHere is your formatted text:")
        for line in lines[:-1]:
            # print(line)
            message += line.rstrip() + ", "
        message += lines[-1].rstrip()
        print(message)

def write_lines():
    filename = "text_files/list.txt"
    print("Give me strings, and I will make a list for you. ('q' to quit).")
    lines = []
    while True:
        line = input(":")
        if line == 'q':
            break
        lines.append(line)
    for line in lines:
        with open(filename, 'a') as f_obj:
            f_obj.write(line + "\n")

def clear_file():
    filename = "text_files/list.txt"
    while True:
        request = input("\nWould you like to clear the original file? (y/n):")
        if request == 'y':
            with open(filename, 'w') as f_obj:
                f_obj.write('')
            break
        elif request == 'n':
            print("Your listed strings will append to the original document.")
            break
        else:
            print("Please enter 'y' or 'n'.")

clear_file()
write_lines()
retrieve_lines()