# with open('text_files/pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents)

# with open('text_files/pi_digits.txt') as file_object:
#     for line in file_object:
#         print(line.strip())

# with open('pycc_resources//chapter_10/pi_digits.txt') as file_object:
#     lines = file_object.readlines()
# for line in lines:
#     print(line.rstrip())

with open('pycc_resources/chapter_10/pi_million_digits.txt') as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

def bday_in_pi():
    bday = input("Enter your birthday in the form mmddyy (ex: 020102)")
    if bday in pi_string:
        print("Your birthday (" + bday + ") is in the digits of pi!")
    else:
        print("Sorry, your birthday is not in the digits of pi.")

bday_in_pi()
# with open('text_files/learning_python.txt') as file_object:
#     lines = file_object.readlines()
# for line in lines:
#     print(line.rstrip())
#     print(line.replace('Python', "C"))