import time

while True:
    #Character choice
    def characters():
        print("\nHey player! Please pick your character.")
        print("\nCharacter 1 (Christopher):")
        print("\t   Attack: 9/10")
        print("\t   Defense: 5/10")
        print("\t   Stamina: 5/10")
        print("")
        print("Character 2 (Bear):")
        print("\t   Attack: 5/10")
        print("\t   Attack: 5/10")
        print("\t   Attack: 7/10")
        print("")
        print("Character 3 (Ash):")
        print("\t   Attack: 4/10")
        print("\t   Attack: 9/10")
        print("\t   Attack: 4/10")
    characters()
    print("")
    character = int(input("Pick your characters! (1-3): "))



    #intro
    def intro():
            print("\nYou were walking joyfully back home with your cat (MEOWWWWS) after a tiring trip from the church. ")
            time.sleep(3)
            print("You overheard someone with a guttural voice. \n\nPlayer: Hmmmmmm seems like some old random dude is shouting. I wonder why?")
            time.sleep(4)
            print("\nLooks like someone got curious and went to take a look. \nHehehehehehe. \nSomeone is not expecting what is gonna happen next!!! OOOOOO spooky.")
            time.sleep(5)
            print ("\nRoyal King: Is there anyone who saw my princess and my pet dog Sandy!?!?!? \n\t    They're were missing for a day!!! :((((")
            time.sleep(5)
            print("\nLooks like someone volunteered to help! Oopsies no one told you what will happened next?")
            time.sleep(3)
            print("\nPlayer: Hey king. My cat (MEOWWWWWWS) and I would love to help you!")
            time.sleep(2)
            print("\nRoyal King: Hey wanderer! Can you help me find my precious? They are both very important to me.\n\t   What's your name?")
            time.sleep(5)
            print("")
            player_name = str(input("Please enter your name: "))
            print(f"\n{player_name}: Sure thing! When was the last time you saw them?")
            time.sleep(2)
            print("\nRoyal King: The last time I saw them was earlier this morning! \n\t    I asked her to pick some apples from the forest to make some apple pies.")
            time.sleep(5)


    #Character 1 story starts
    if character == 1:
        intro()

    #Character 2 story starts
    elif character == 2:
        intro()

    #Character 3 story starts
    elif character == 3:
        intro()

    else:
        print("\nHey buddy. You entered an unvalid choice. Just pick again <3")