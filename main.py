print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')

print("Welcome to treasure island")
print("Your mission is to find the treasure")

choice1 = input('you\'re at a crossroad, where do you want to go? Type "left" or "right" \n').lower()

if choice1 == "left":
    choice2 = input('''You\'ve come to a lake. There is an island in the middle of the lake.
Type "wait" to wait for the boat.Type "swim" to swim across\n''').lower()
    if choice2 == "wait":
        choice3 = input('''You arrived at the island unharmed.
There is a house with 3 Doors. one red one yellow and one blue,
which color do you choose\n''').lower()
        if choice3 == "red":
            print("its a room full of fire, GAME OVER")
        elif choice3 == "yellow":
            print("You found the Treasure! YOU WIN!")
        elif choice3 == "blue":
            print("You enter a room of beast, GAME OVER")
        else:
            print("You choosed a door that dosen't exist, GAME OVER! ")
    else:
        print("You got attacked by angry trout, GAME OVER! ")
else:
    print("You fell into a hole, GAME OVER!")
