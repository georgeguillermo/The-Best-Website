import random
floor = 'bottom'
strength = 0
game_running = True
first_time_bottom = True
first_time_right = True
first_time_middle = True
puzzle_1 = False
puzzle_2 = False
puzzle_3 = False

while game_running:
    if floor == 'bottom':
        if first_time_bottom == True:
            print("You have found yourself at the bottom of a multi-floored dungeon. You are in an unknown room, but you see two doors, one to your left, and the other to your right.")
            print("")
            print("The door to the left has heavy breathing behind it, as if there's an enemy waiting behind the door, ready to knock you out when you open it.")
            print("")
            print("The door to the right is eerily silent, leaving the mystery of what's behind it.")
            print("")
            print("Do you choose door 1, the door to your left, or door 2, the door to your right?")
        else:
            print("You have found yourself back at the crossroads from the beginning of your journey, which door will you choose now, door 1 on the left, or door 2 on your right?")
        answer_1 = int(input(""))
        if answer_1 == 1 and strength == 0:
            print("A monster jumps out from behind the door and knocks you out, leaving you in the same room you were in before. :(")
            first_time_bottom = False
        elif answer_1 == 1 and strength != 0:
            print("You successfully battle the monster and, after fighting with all your might, manage to knock it out, leaving the monster sitting on the floor against the wall.")
            print("You have made it to the next floor! :)")
            floor = 'middle'
        if answer_1 == 2 and first_time_right == True:
            print("You have found your trusty bat and hastily put it on before any other monsters attack.")
            strength += 1
            first_time_bottom = False
            first_time_right = False
        elif answer_1 == 2 and first_time_right == False:
            print("There is nothing else except eerie silence left in this room.")
        if answer_1 != 1 and answer_1 != 2:
            print("That is not a valid door number :(.")
    if floor == 'middle':
        if first_time_middle == True:
            print("")
            print("You have found yourself in a strangely peculiar room.")
            print("")
            print("There are three doorways in front of you:")
            print("")
        elif first_time_middle == False:
            print("You are back, standing before 3 doorways with puzzles in them.")
            print("")
        print("To your right, there is a doorway with a math sign above it.")
        print("")
        print("To your left, there is a doorway with a chemistry sign above it.")
        print("")
        print("In front of you, there is a doorway with a literary sign above it, but there's an odd sense of doom coming from it, as if there's someone, or something, really powerful behind it.")
        print("")
        print("Which doorway will you go through?")
        print("1. To the right")
        print("2. To the left")
        print("3. Straight ahead")
        first_time_middle = False
        answer_1 = int(input(""))

        if answer_1 == 1:
            if puzzle_1 == False:            
                print("Before you, you see a locked glass box containing a helmet.")
                print("However, it isn't just any helmet, it's your old helmet you used to wear when going on adventures all the time")
                print("You see a sign above it that says 'Who is the inventor of Calculus?'")
                print("1. Archimedes")
                print("2. Issac Newton")
                print("3. Albert Einstein")
                print("4. Nikola Tesla")
                answer_1 = int(input(""))
                if answer_1 != 2:
                    print("An EXTREMELY loud incorrect buzzer rings throughout the entire room, shaking the floor.")
                    print("You can only assume that you got the question wrong because the glass door has not opened :(.")
                elif answer_1 == 2:
                    print("Hidden confetti cannon explode into the rooms, celebrating your correct answer!!!")
                    print("The locked glass box pops open, letting you grab your helmet!")
                    print("You put on your helmet and feel its embrace fit snugly onto your head.")
                    strength += 1
                    puzzle_1 = True
            elif puzzle_1 == True:
                print("You have already completed this puzzle, so you go back to the main room.")
        elif answer_1 == 2:
            if puzzle_2 == False:
                print("The first thing you see is a very bright monitor that asks 'what is the element with 3 protons?'")
                print("The burning in your eyes reminds you that you haven't seen the sun in a lot of time and that this dungeon is very dimly lit.")
                print("A microphone appears before you along with a periodic table, as if wanting you to say the answer.")
                print("What element do you respond with")
                answer_2 = input("")
                if answer_2.lower() == "lithium":
                    print("An extremely loud correct buzzer sounds though the room, the screen showing a smiley face for your amazing work.")
                    print("From the ceiling, your chestplate falls onto your head, hurting you a bit, but at least you have the rest of your armor!")
                    puzzle_2 = True
                    strength += 1
                elif puzzle_1 == True:
                    print("A frowny face appears on the screen and you instinctively cover your ears, but only a sad 'boo womp' sound is played.")
                else:
                    print("A sad 'boo womp' sound is played from a speaker somewhere in the room.")
                    print("You probably got the answer wrong :(.")
            elif puzzle_2 == True:
                print("There is nothing left in this room apart from the monitor with a smiley face, so you go back to the main room.")
        elif answer_1 == 3:
            print("As soon as you enter the room, a sword comes swinging at you.")
            print("Luckily, you are able to dodge in time, and see the thing that attacked you, another giant monster blindly swinging at you.")
            print("It seems as if the literary sign was a red herring...")
            if strength == 1:
                print("You quickly run out the room, barely getting grazed by the monster's sword as you do, however, it's too big to fit through the doorway, so you are safe for now in the main room.")
            elif strength == 2:
                print("You know you have been outmatched, so you quickly run back into the main room before the monster actually hits you.")
                print("The monster is too large to fit through the doorway, meaning you are safe in the main room.")
                print("(Seems like the designer of this dungeon wasn't too bright)")
            elif strength >= 3:
                print("You are just barely able to fend off the monster, knocking your bat on its head as hard as you can, making it go to sleep temporarily.")
                print("Behind the monster, you see it was guarding a wooden door, so you enter it because there is nowhere else for you to go")
                floor = 'top'
    if floor == 'top':
        monster_health = 5
        monster_magic = 0
        your_health = 5
        rng = random.randint(1, 5)
        print("You find yourself at the top floor, feeling as if you are near the end of the dungeon.")
        print("A monster suited in armor stands menacingly in front of you with a blunt sword.")
        print("Seeing that this monster looks actually suited for battle, you assume this is the mastermind of the dungeon since he seems smart enough to make one, but not smart enough to sharpen his sword apparently.")
        print("The monster charges at you, and you have no choice but to fight it.")
        while monster_health > 0:
            rng = random.randint(0, 4)
            if rng == 0:
                print("It raises its sword above its head while rushing at you, probably preparing to hit you when you get close enough.")
            elif rng == 1:
                print("It raises its sword, but there's something off about the attack.")
            elif rng == 2:
                print("It raises its sword in a defensive way, seemingly preparing to block an incoming attack.")
            elif rng == 3:
                print("It doesn't raise its sword, instead, it seems to be preparing to charge up some magic.")
            elif rng == 4:
                print("It raises its sword, but it seems to be preparing to cast some magic.")
            print("What do you do:")
            print("1. Try to dodge")
            print("2. Try to block")
            print("3. Try to attack")
            answer_2 = int(input(""))
            if rng == 0:
                if answer_2 == 1:
                    print("You manage to just barely dodge the attack, managing to land a counter attack on the monster, dealing 1 damage to it.")
                    monster_health -= 1
                elif answer_2 == 2:
                    if monster_magic == 0:
                        print("You manage to block the monster's attack, negating the danage it'll do.")
                    else:
                        print("You successfully block the monster's attack and shove it back, seemingly making it lose concentration on its spell.")
                        monster_magic -= 1
                elif answer_2 == 3:
                    print("You try to attack the monster, but it's strength overpowers you and take 1 damage.")
                    your_health -= 1
            elif rng == 1:
                if answer_2 == 1:
                    print("You fall for the monster's feint, dodging right into its attack. Due to you falling for the monster's feint, it manages to land a hit on you, dealing 1 damage to you.")
                    your_health -= 1
                elif answer_2 == 2:
                    if monster_magic == 0:
                        print("You stay on your guard through its feint, managing to block its attacking that it tried to land after the feint, managing to land a counter attack on the monster.")
                        monster_health -= 1
                    else:
                        print("You stay on your guard through its feint, managing to block its attacking that it tried to land after the feint, managing to land a counter attack on the monster.")
                        print("Your counter attack seems to have made the monster lose concentration on its spell!")
                        monster_health -= 1
                        monster_magic -= 1
                elif answer_2 == 3:
                    print("You try to attack the monster, but it seems to have been expecting that and manages to land a hit on you, dealing 1 damage to you.")
                    your_health -= 1
            elif rng == 2:
                if answer_2 == 1:
                    print("You try to do nothing, the monster is left confused because it was preparing for an attack.")
                elif answer_2 == 2:
                    print("You both try to block a non-existent attack...")
                elif answer_2 == 3:
                    print("You try to attack the monster, but it manages to block your attack and land a hit on you, dealing 1 damage to you.")
                    your_health -= 1
            elif rng == 3:
                if answer_2 == 1:
                    print("You dodge nothing, the monster is able to charge up some of its magic before returning to an offensive position.")
                    monster_magic += 1
                elif answer_2 == 2:
                    print("You try to block, expecting it to cast a spell, but it was only charging up a spell.")
                    monster_magic += 1
                elif answer_2 == 3:
                    print("You interrupt the monster's spell charging, dealing 1 damage to it.")
                    monster_health -= 1
            elif rng == 4:
                if monster_magic != 3:
                    print("The monster casts a spell, but it seems to have been a dud, as nothing happens.(LOL)")
                    print("You attack him while he is distracted, dealing 1 damage to him.")
                    monster_health -= 1
                elif monster_magic >= 3:
                    print("The monster casts a powerful spell, as a beam of purple light rushes at you.")
                    if answer_2 == 1:
                        print("You try to dodge, but the spell is too fast and you take 2 damage.")
                        your_health -= 2
                        monster_magic = 0
                    elif answer_2 == 2:
                        print("You manage to successfully block the spell, but it leaves you dazed, allowing the monster to get a hit on you.")
                        your_health -= 1
                        monster_magic = 0
                    elif answer_2 == 3:
                        print("You try to attack the monster, just barely interrupting its spell before it fully casts it.")
                        monster_health -= 1
                        monster_magic = 0
        print("You have defeated the monster, and you see a door behind it, so you enter it.")
        print("You see the beautiful outside as you escape the dungeon once and for all.")
        game_running = False