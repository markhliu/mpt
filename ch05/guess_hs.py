import time
import sys

# Import functions from the loacal package
from mptpkg import voice_to_text, print_say

# Print and announce the rules of the game in a human voice
print_say('''Please think of an integer, 
      bigger or equal to 1 but smaller or equal to 9, 
      and write it on a piece of paper''')
print_say("You have 5 seconds to write down.")
# Wait for five seconds for you to write down the number
time.sleep(5)
print_say('''Now let's start. I will guess a number and you can say: 
    too high, that is right, or too small''')
# Python asks in a human voice whether the number is 5
print_say("Is it 5?")
# Capture your response and save it as re1
# Your response has to be 'too high', 'that is right', or 'too small'
while True:
    re1 = voice_to_text()
    print_say(f"You said {re1}")
    if re1 in ("too high", "that is right", "too small"):
        break
# If you say "that is right", game over
if re1 == "that is right":
    print_say("Yay, lucky me!")
    sys.exit
# If you say "too high", the computer keeps guessing
elif re1 == "too high":
    # The computer guesses 3 the second round
    print_say("Is it 3?")
    # The computer is trying to get your response to the second guess
    while True:
        re2 = voice_to_text()
        print_say(f"You said {re2}")
        if re2 in ("too high", "that is right", "too small"):
            break
    # If the second guess is right, game over
    if re2 == "that is right":
        print_say("Yay, lucky me!")
        sys.exit
        # If the second guess is too small, the computer knows it's 4
    elif re2 == "too small":
        print_say("Yay, it is 4!")
        sys.exit
    # If the second guess is too high, the computer guesses the third time
    elif re2 == "too high":
        # The third guess is 1
        print_say("Is it 1?")
        # The computer is getting your response to the third guess
        while True:
            re3 = voice_to_text()
            print_say(f"You said {re3}")
            if re3 in ("too high", "that is right", "too small"):
                break
                # If the third guess is too small, the computer knows it's 2
        if re3 == "too small":
            print_say("It is 2!")
            sys.exit
        # If the thrid guess is right, game over
        elif re3 == "that is right":
            print_say("Yay, lucky me!")
            sys.exit
        # If you say "too small", the computer keeps guessing
elif re1 == "too small":
    # The computer guesses 7 the second round
    print_say("Is it 7?")
    # The computer is trying to get your response to the second guess
    while True:
        re2 = voice_to_text()
        print_say(f"You said {re2}")
        if re2 in ("too high", "that is right", "too small"):
            break
            # If the second guess is right, game over
    if re2 == "that is right":
        print_say("Yay, lucky me!")
        sys.exit
    # If the second guess is too high, the computer knows it's 6
    elif re2 == "too high":
        print_say("Yay, it is 6!")
        sys.exit
    # If the second guess is too small, the computer guesses the third time
    elif re2 == "too small":
        # The third guess is 8
        print_say("Is it 8?")
        while True:
            re3 = voice_to_text()
            print_say(f"You said {re3}")
            if re3 in ("too high", "that is right", "too small"):
                break
                # If the third guess is too small, the computer knows it's 9
        if re3 == "too small":
            print_say("It is 9!")
            sys.exit
        # If the third guess is right, game over
        elif re3 == "that is right":
            print_say("Yay, lucky me!")
            sys.exit










