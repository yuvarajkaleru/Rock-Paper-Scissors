import random
def win(comp , user):
    if user == comp:
        return None
    elif user == "r":
        if comp == "s":
           return True
        elif comp == "p":
           return False
    elif user == "p":
        if comp == "r":
           return True
        elif comp == "s":
           return False
    elif user == "s":
        if comp == "p":
           return True
        elif comp == "r":
           return False
compinput = random.randint(1, 3)
if compinput == 1:
    comp = "r"
elif compinput == 2:
    comp = "p"
elif compinput == 3:
    comp = "s"
user = input("your turn = rock(r), paper(p), scissors(s): ")
while user not in ["r", "p", "s"]:
    print("Invalid input. Please enter 'r', 'p', or 's'.")
    user = input("your turn = rock(r), paper(p), scissors(s): ")
print(f"computer choose : {comp}")
print(f"you choose : {user}")
a = win(comp, user)
if a == None:
    print("It's a tie")
elif a == True:
    print("You win")
else:
    print("You lose")