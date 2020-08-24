from sys import exit
from sys import argv
ant_colony = []

script, poem = argv

def start():
    print("--------------------------------")
    print("You are on the kitchen floor of a 5-star restaurant and you are a bug.")
    print("\tWhat kind of bug are you?")
    print("""
    1. ant
    2. spider
    """)

    bug = input("> ")

    if "1" in bug or "ant" in bug:
        ant()
    elif "2" in bug or "spider" in bug:
        spider()
    else:
        die("That wasn't on the list, you dumb-dumb.")

def ant():
    print("--------------------------------")
    print("Small and mighty, you are an ant, and you are part of a large colony.")
    print("Enter some names of members of your colony: ")

    desire = True

    while desire:
        name = input("> ")
        ant_colony.append(name)
        print("The names of your colony members are: ", ant_colony)
        print("\tWould you like to add more? ")

        more = input("> ")

        if "yes" in more:
            if len(ant_colony) > 3:
                die("You spent so much time listing your colony that you didn't see the delivery boy squash you under that morning's shipment of beets.")
            print("Add name")
        elif "no" in more:
            desire = False
        else:
            die("Well what does that even mean? Learn to answer yes or no.")


    print("A chef's apprentice enters and starts preparing that morning's food.")
    print("They toss a rotting apple and it misses the trashbin.")
    print("\tGo to apple or escape kitchen?")

    choice = input("> ")

    if "apple" in choice:
        apple()
    elif "escape" in choice:
        escape()
    else:
        die("Well, that wasn't a very good choice.")

def apple():
    window_blocked = True
    print("~" * 30)
    print("You rush towards the apple and see a hole in its skin. It smells delicious.")
    print("\tWhat do you do?")
    print("""\t1. Enter
        2. Leave it be""")

    choice = input("> ")

    if "enter" in choice or "1" in choice:
        print("You begin to eat when the apprentice returns to throw the apple away again.")
        print("The apple lands in compost and you are in a heaven of more food. Great job!")
        exit(0)
    elif "leave" in choice or "2" in choice:
        print("There is an partly open window near you.")
        print("There is also a glass hanging close to the edge of a counter.")
        print("More restaurant staff arrive and stand in front of the window.")
        print("How will you get to the window?")

        while True:
            window = input("> ")
            if "window" in choice and window_blocked:
                dead("Though you move quietly, you are spotted and killed.")
            elif "window" in choice and not window_blocked:
                print("Good work! You've made it outside.")
                exit(0)
            elif "glass" in choice:
                print("You climb the counter and push the glass until it drops and breaks.")
                print("The apprentice rushes to clean up the glass. The window is unblocked!")
                window_blocked = False
            else:
                print("I don't know what that means.")
    else:
        die("What kind of move was that?")

def escape():
    print("~" * 30)
    print("There is gap between the counter and the wall just big enough for a bug.")
    print("A cockroach is just inside and will not let you pass.")
    print("You must create a 3 line poem complimenting it.")

    line_1 = input("First line: ")
    line_2 = input("Second line: ")
    line_3 = input("Third line: ")

    poem_file = open(poem, 'w')
    poem_file.write(line_1)
    poem_file.write("\n")
    poem_file.write(line_2)
    poem_file.write("\n")
    poem_file.write(line_3)
    poem_file.close()

    print("Here is your poem: ")
    my_poem = open(poem)
    print(my_poem.read())

    if "ugly" in my_poem.read() or "gross" in my_poem.read():
        die("How dare you! The cockroach throws you into the open and you are killed.")
    elif "gorgeous" in my_poem.read() or "beautiful" in my_poem.read() or "amazing" in my_poem.read():
        print("Aww, what a nice thing to say!")
        print("You are allowed to pass and survive.")
        exit(0)
    elif "die" in my_poem.read() or "dirt" in my_poem.read() or "nasty" in my_poem.read():
        die("How dare you! The cockroach throws you into the open and you are killed.")
    elif "fuck" in my_poem.read() or "shit" in my_poem.read():
        die("Now that's just unclean. And you think cockroaches are dirty.")
    else:
        print("The cockroach accepts the poem and let's you through.")
        print("You survive!")
        exit(0)


def spider():
    print("--------------------------------")
    print("Living on the wall, you are a spider living in the corning of the ceiling.")
    print("There is a crate of carrots on the ground")
    print("\tSpin a web or move to crate?")
    choice = input("> ")

    if "web" in choice:
        print("A fly gets caught in your web.")
        print("Eat fly or free it?")

        decision = input("> ")

        if "eat" in decision:
            print("The fly wriggles a lot as you near it, making noise.")
            print("At that moment, a group of chef's enter the kitchen and see your web.")
            die("They destroy it and you.")
        elif "free" in decision:
            print("At that moment a group of chef's enter the kitchen. They see the fly and kill it.")
            print("They don't see you, but you grow wary of your position.")
            print("Move or stay put?")

            option = input("> ")
            if "move" in option:
                crate()

    elif "crate" in choice:
        print("You prefer to travel. That's nice!")
        crate()
    else:
        die("That's not a good decision to make as a spider.")


def crate():
    print("~" * 30)
    print("You go into the crate and settle among the leafy stems of the carrots.")
    print("But at that moment a group of chefs enter the kitchen.")
    print("One of them lifts the carrot you're on.")
    print("Run or stay still?")

    decision = input("> ")

    if "run" in decision:
        print("Your sudden actions make the chef panic.")
        print("They smash the carrot onto a counter, crushing you.")
        die("Welp.")
    elif "stay" in decision:
        print("The chef slowly moves the carrot towards a window and allows you to exit.")
        print("Great job!")
        exit(0)

def die(death_reason):
    print("--------------------------------")
    print(death_reason, "You've died and ended the game.")
    exit(0)


start()
