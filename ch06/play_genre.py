import os
import random
from pygame import mixer

# Add the one-level-up directory to the searchable space
import sys
sys.path.append('../')

# Import functions from the local package
from mypkg.mysr import voice_to_text
from mypkg.mysay import print_say

# Start an infinite loop to take your voice commands
while True:   
    print_say("how may I help you?")
    inp=voice_to_text()
    print_say(f"you just said {inp}")
    # Stop the program if you say 'stop listening'
    if inp=="stop listening":
        print_say("Goodbye!")
        break
    # If 'play a' and 'song" are in voice command, it is activated
    elif "play a" in inp and "song" in inp:
        # Remove 'play a' and 'song' so that only the genre name is left
        inp=inp.replace('play a ','')
        inp=inp.replace(' song','')
        # Go to the genre folder and randomly selects a song
        with os.scandir(f"./chat/{inp}") as entries:
            mysongs=[entry.name for entry in entries]
        # Use pygame mixer to play the song
        mysong=random.choice(mysongs)
        print_say(f"play the song {mysong} for you")
        mixer.init()
        mixer.music.load(f"./chat/{inp}/{mysong}")
        mixer.music.play()
        # Say stop to stop the music any time
        while True:
            background=voice_to_text().lower()
            if "stop" in background:
                mixer.music.stop()
                break
            else:
                continue
