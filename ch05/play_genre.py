import os
import random
from pygame import mixer

# Import functions from the loacal package
from mptpkg import voice_to_text, print_say

# Start an infinite loop to take your voice commands
while True:
    print_say("how may I help you?")
    inp = voice_to_text()
    print_say(f"you just said {inp}")
    # Stop the program if you say 'stop listening'
    if inp == "stop listening":
        print_say("Goodbye!")
        break
    # If 'play a' and 'song" are in voice command, it is activated
    elif "play a" in inp and "song" in inp:
        # Remove 'play a' and 'song' so that only the genre name is left
        inp = inp.replace('play a ', '')
        inp = inp.replace(' song', '')
        # Go to the genre folder and randomly selects a song
        with os.scandir(f"./chat/{inp}") as entries:
            mysongs = [entry.name for entry in entries]
        # Use pygame mixer to play the song
        mysong = random.choice(mysongs)
        print_say(f"play the song {mysong} for you")
        mixer.init()
        mixer.music.load(f"./chat/{inp}/{mysong}")
        mixer.music.play()
        break
