try:
    filename = 'text_files/cat.txt'
    with open(filename) as f_obj:
        lines = f_obj.readlines()
except FileNotFoundError:
    print("The file " + filename + " was not found.")
else:
    for line in lines:
        print(line.rstrip())

print("")

try:
    filename = 'text_files/dog.txt'
    with open(filename) as f_obj:
        lines = f_obj.readlines()
except FileNotFoundError:
    print("The file " + filename + " was not found.")
else:
    for line in lines:
        print(line.rstrip())

# with open(filename, 'a') as f_obj:
#     f_obj.write("\nPuppy")