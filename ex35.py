from sys import exit # imports exit function from sys module

def gold_room(): # defines gold_room function which takes no parameter
    print("This room is full of gold. How much do you take?") # prints a question

    choice = input("> ") # takes input from user as a string and assigns to variable name choice
    if "0" in choice or "1" in choice: # if string contains character 0 or 1 then run code block below
        how_much = int(choice) # assigns the contents of choice as an integer to variable name how_much
    else: # if string doesn't contain character 0 or 1 then above code is skipped and else code block runs
        dead("Man, learn to type a number.") # calls dead function with string as parameter (see dead function defined below)

    if how_much < 50: # if integer assigned to how_much is less than 50 then run following code block
        print("Nice, you're not greedy, you win!") # print string
        exit(0) # then exit script
    else: # if integer assigned to how_much is greater or equal to 50 then above code block is skipped and following code block is run
        dead("You greedy bastard!") # calls dead function with string as parameter (see dead function defined below)

def bear_room(): # defines bear_room function which takes no parameter
    print("There is a bear here.") # prints string
    print("The bear has a bunch of honey.") # prints string
    print("The fat bear is in front of another door.") # prints string
    print("How are you going to move the bear?") # prints string
    bear_moved = False # assigns Boolean false to variable name bear_moved

    while True: # begins while-loop which runs for as long as a condition is met and the Boolean state is set as True
        choice = input("> ") # prompts for user inout in response to question above and assigns it to variable name choice

        if choice == "take honey": # if string assigned to choice is exactly equal to "take honey" then run code block below
            dead("The bear looks at you then slaps your face off.") # calls dead function with string parameter (see dead function defined below) so comes out of while-loop
        elif choice == "taunt bear" and not bear_moved: # else (skip above code block) and if string assigned to choice is exactly equal to "taunt bear" AND Boolean state is True (not False) (ie. bear has not moved yet) then run following code block (if latter is False (not True) then skips to next code block)
            print("The bear has moved from the door.") # prints string
            print("You can go through it now.") # prints string
            bear_moved = True # taunting the unmoved bear causes. Condition of while-loop has been met so state is True and another iteration is run but now this block is skipped
        elif choice == "taunt bear" and bear_moved: # else (skips both code blocks above) and if string assigned to choice is exactly equal to "taunt bear" AND Boolean state is False (ie. bear not moved) then run following code block
            dead("The bear gets pissed off and chews your legs off.") # calls dead function with string as parameter (see dead function defined below). Comes out of while-loop
        elif choice == "open door" and bear_moved: # else (skips all three code blocks above) and if string assigned to choice is exactly equal to "open door" (second or more iteration of while-loop) AND Boolean state is True (bear has moved) then run following code block
            gold_room() # calls gold_room function with no parameter (defined above). Comes out of while-loop
        else: # non of above requirements met then all previous code blocks skipped and following code block runs
            print("I got no idea what that means.") # prints string which implies that user has inputted a string that is not recognised. A condition of the while-loop has been met so state is therefore True and another iteration is run from the beginning

def cthulhu_room(): # defines cthulhu_room function which takes no parameter
    print("Here you see the great evil Cthulhu.") # prints string
    print("He, it, whatever stares at you and you go insane.") # prints string
    print("Do you flee for your life or eat your head?") # prints string

    choice = input("> ") # prompts for input from user and assigns to variable name choice (overriding any previous assignment)
# using if x in y format allows for more inputs from user to achieve a story branch provided they in some way contain the keyword
    if "flee" in choice: # if string "flee" is in anyway contained in the string assigned to choice, then the below code block runs
        start() # calls start function (defined below) effectively restarting the game
    elif "head" in choice: # else skips above code block and if string "head" is contained within the string assigned to choice, then the below code block requirements
        dead("Well that was tasty!") # calls dead function with string as parameter
    else: # if none of the above is true then above code blocks are skipped and the below code block is run instead
        cthulhu_room() # input wasn't recognised so is prompted for again (cthulhu_room function runs again) until user realises to type flee or head, bet that's annoying


def dead(why): # defines dead function which takes (as it happens) a string as a parameter and assigns it to the variable name why
    print(why, "Good job!") # prints string associated to why and string "Good job!"
    exit(0) # exits script (ends game)

def start(): # defines start function which takes no parameter
    print("You are in a dark room.") # prints string
    print("There is a door to your right and left.") # prints string
    print("Which one do you take?") # prints string

    choice = input("> ") # prompts user for input and assigns said input as string to variable name choice (over riding any previous assignment)
    if choice == "left": # if string assigned to choice is exactly equal to "left" then runs below code block
        bear_room() # calls bear_room function with no parameter
    elif choice == "right": # else skips code block and if string assigned to choice is exactly equal to "right" then runs below code block
        cthulhu_room() # calls cthulhu_room function with no parameter
    else: # neither criterion met then skips both code blocks and runns below code block instead
        dead("You stumble around the room until you starve.") # calls dead function with a string as parameter

start() # having defined everything we need we finally call start function to begin the game
