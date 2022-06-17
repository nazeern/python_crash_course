class User():
    def __init__(self, f_name, l_name, email, pwd):
        self.first_name = f_name
        self.last_name = l_name
        self.full_name = f_name.title() + " " + l_name.title()
        self.email = email
        self.password = pwd
        self.login_attempts = 0

    def describe_user(self):
        print("\nYour full name is " + self.full_name + ".")
        print("Your associated email is " + self.email + ".")
        print("Your associated password is " + self.password + ".")
        if self.login_attempts == 1:
            print("You have had " + str(self.login_attempts) + 
                " login attempt.")
        else:
            print("You have had " + str(self.login_attempts) + 
                " login attempts.")

    def greet_user(self):
        print("\nHi " + self.full_name + ", how are you!")

    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0


# user_nitin = User('Nitin', 'Nazeer', 'nitin.nazeer@gmail.com', 'password')
# user_nitin.increment_login_attempts()
# user_nitin.describe_user()

# user_nitin.reset_login_attempts()
# user_nitin.describe_user()

# user_nitin.greet_user()

class Privileges():
    def __init__(self, privileges=[]):
        self.user_privileges = privileges

    def add_privileges(self, new_privileges):
        for new_privilege in new_privileges:
            self.user_privileges.append(new_privilege)

    def show_privileges(self):
        print("\nPrivileges include:")
        if self.user_privileges:
            for privilege in self.user_privileges:
                print("\t" + privilege + ".")
        else:
            print("\tN/A")

class Admin(User):
    def __init__(self, f_name, l_name, email, pwd):
        super().__init__(f_name, l_name, email, pwd)
        self.privileges = Privileges()

admin1 = Admin("Nitin", "Nazeer", "nitin.nazeer@gmail.com", "password")
admin1.privileges.show_privileges()
admin1.privileges.add_privileges(["can ban users", "can add posts"])
admin1.privileges.show_privileges()
# print(admin1.first_name)

