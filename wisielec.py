import random
print("Category: geometric figures")
list1 = ("square", "triangle", "rectangle", "circle", "polygon", "trapeze", "diamond", "oval")
password = random.choice(list1)
length = len(password)
print(f"You have 10 tries")
#######################################
table=list(password)

for i in range(length):
    table[i] = "_"
    ("".join(table))
#########################################
tries = 10

while tries > 0:
    print("".join(table))
    if tries == 0:
        break
#########################################
    yn = input("czy chcesz odgadnąć całe hasło yes/no ").lower()
    if yn == ("yes"):
        password2 = input("Enter the password in full ").lower()
        if password == password2:
            print(f"Congratulations you won, searched password this: {password}")
            break
        else:
            print("Pudło")
    elif yn == ("no"):
#######################################
        print(f"You have {tries} tries")
        tries = tries - 1
        letter = input("Enter the letter from password ").lower()
        if letter in password:
            for i in range(length):
                if password[i] == letter:
                    table[i] = letter
        elif letter != password:
            print("Your letter is bad")
        if password == "".join(table):
            print(f"Congratulations you won, searched password this: {password}")
            break
        elif tries == 0:
            print(f"GAME OVER searched password this: {password}")
            