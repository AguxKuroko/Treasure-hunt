print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island!!\nYour mission is to find the hidden treasure.")

decision1 = input("You are on the deserted island. You spotted a massive tree on the left,\nbut on the right side, you can see a substantial rock.\nSo, which direction do you go - left or right?\n")
if decision1.count("r") or decision1.count("R") :
    print("Oh, no! You were ambushed by wild animals that were playfully hiding behind that massive rock.\nGAME OVER")
elif decision1.count("l") or decision1.count("L"):
    print("By choosing to go and see the tree, you made a wise decision, and you survived.")
    print("Beneath the tree, your keen eye caught sight of a tiny hole. It appears to lead to a cave with mesmerizing blue water, ")
    print("but from that opening, you can discern eerie and mysterious sounds echoing.")
    print("Will you linger a while longer, captivated by the mystery, or will you embrace the unknown and dive headfirst into")
    print("the enigmatic hole, ready to explore the secrets of the underwater cave?")
    decision1 = input("Wait or swim?\n")
    if decision1.count("s") or  decision1.count("S"):
        print("Wow! What an enchanting place you've stumbled upon!\nYou venture deeper and deeper into the cave.")
        print("Before you are three distinct doors, each displaying a unique color\n")
        decision1 = input("Red, blue, or yellow – which door is yours to open\n")

        if decision1.count("r") or  decision1.count("R"):
            print("Red isn't your color, my friend. After you opened the door, you were shot to death.\nGAME OVER")
        elif decision1.count("b") or  decision1.count("B"):
            print("As you stepped into the room, an ominous presence enveloped you. Without warning, you were ambushed from behind by a rivaltreasure hunter.\nGAME OVER")
        elif decision1.count("Y") or  decision1.count("y"):
            print("As you pushed the door open and stepped inside, your eyes were drawn to a massive, glistening diamond. It awaits you!\nCongratulations!")
            print('''
     __________________
    .-'  \ _.-''-._ /  '-.
  .-/\   .'.      .'.   /\-.
 _'/  \.'   '.  .'   './  \'_
:======:======::======:======:  
 '. '.  \     ''     /  .' .'
   '. .  \   :  :   /  . .'
     '.'  \  '  '  /  '.'
       ':  \:    :/  :'
         '. \    / .'
           '.\  /.'    
             '\/'
''')


        else:
            print("While you hesitated, time slipped away unnoticed, and you failed to notice a small snake that bit your foot")
            print("Unfortunately for you, it turned out to be a poisonous snake. Its venom quickly took hold, immobilizing you completely.\nGAME OVER")


    else:
        print("Since you chose to remain, your food supply dwindled, and eventually, you perished from starvation...\nGAME OVER")