# Password generator with selections
import random
#ADD NUMBERS
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
punctuation = "!@#$%^&*()<>?/."
numbers = "0123456789"
selection = ""



length = int(input("Enter the desired length of your new password: "))
upper = str(input("Do you want your password to contain uppercase letters?('y or n'): "))
lower = str(input("Do you want your password to conatain lowercase letters?('y or n'): "))
special = str(input("Do you want your password to contain special characters?('y or n'): "))
num = str(input("Do you want your password to contain numbers?('y or n'): "))

class Passwd:
    def __init__(self, length, upper, lower, special):
        self.length = length
        self.upper = upper
        self.lower = lower
        self.special = special

    def make_passwd(self):
        global selection
        if upper == "y":
            selection += uppercase
        if lower == "y":
            selection += lowercase
        if special == "y":
            selection += punctuation
        if num == "y":
            selection += numbers
        if upper == "n" and lower == "n" and special == "n":
            print ("You need to select at least one character type for your password.")
            exit()

        password = []
        for i in range(length):
            password.append(random.choice(selection))
        print("".join(password))


p = Passwd(length, upper, lower, special)
p.make_passwd()