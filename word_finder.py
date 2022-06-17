filename = 'text_files/a_tale_of_two_cities.txt'
with open(filename) as f_obj:
    lines = f_obj.readlines()

sum = 0
for line in lines:
    sum += line.lower().count('the')
    