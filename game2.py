import random

print("Rules for Stone paper scissor game are as follows: \n"
      + "Stone vs paper - paper wins \n"
      + "Stone vs scissor - Stone wins \n"
      + "paper vs scissor - scissor wins \n")

while True:
    print("Enter your choice \n 1. Stone \n 2. paper \n 3. scissor \n")

    choice = int(input("User turn: "))

    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))

    if choice == 1:
        choice_name = 'Stone'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'

    print("User choosed :" + choice_name)
    print("\nNow its computer turn.......")

    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'

    print("Computer choosed: " + comp_choice_name)

    print(choice_name + " V/s " + comp_choice_name)

    if ((choice == 1 and comp_choice == 2) or
            (choice == 2 and comp_choice == 1)):
        print("paper wins. ", end="")
        result = "paper"

    elif ((choice == 1 and comp_choice == 3) or
          (choice == 3 and comp_choice == 1)):
        print("Rock wins. ", end="")
        result = "Rock"
    else:
        print("scissor wins. ", end="")
        result = "scissor"

    if result == choice_name:
        print("User wins this battle")
    else:
        print("Computer wins this battle")