guest_list = ["Gandhi", "George Washington", "Donald Trump", "Hillary Clinton"]
print("Hi " + guest_list[0] + ", you are invited!")
print("Hi " + guest_list[1] + ", you are invited!")
print("Hi " + guest_list[2] + ", you are invited!")
print("Hi " + guest_list[3] + ", you are invited!")

print("Actually, Donald Trump is not allowed to attend this party.")
reject_list = []
reject_list.append(guest_list.pop(2))
guest_list.insert(2, "Steve Jobs")
print(guest_list[2] + " is invited instead.")

guest_list.insert(0, "Elon Musk")
guest_list.insert(2, "Robert Downey Jr.")
guest_list.append("This Guy!")
print(guest_list[-1] + " is invited, too")

print("Wait, I can only invite 2 people.")
print("Sorry " + guest_list.pop(-1) + ", you are no longer invited.")
print("Sorry " + guest_list.pop(-1) + ", you are no longer invited.")
print("Sorry " + guest_list.pop(-1) + ", you are no longer invited.")
print("Sorry " + guest_list.pop(-1) + ", you are no longer invited.")
print("Sorry " + guest_list.pop(-1) + ", you are no longer invited.")
print("Sorry " + guest_list.pop(-1) + ", you are no longer invited.")
print("Sorry " + guest_list.pop(-1) + ", you are no longer invited.")

print(guest_list)
