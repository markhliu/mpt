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
    # If 'play' is in voice command, music mode is activated
    elif "play" in inp:
        # Remove the word play from voice command
        inp=inp.replace('play ','')
        # Separate first and last names
        names=inp.split()
        # Extract the first name
        firstname=names[0]
        # Extract the last name
        if len(names)>1:
            lastname=names[1]
        # If no last name, use the first name as last name;  
        else:
            lastname=firstname
        # Create a list to contain songs 
        mysongs=[]
        # If either first name or last name in the file name, put in list
        with os.scandir("./chat") as files:
            for file in files:
                if (firstname in file.name or lastname in file.name) and "mp3" in file.name:
                    mysongs.append(file.name)
        # Randomly select one from the list and play
        mysong=random.choice(mysongs)
        print_say(f"Play the song {mysong} for you.")
        mixer.init()
        mixer.music.load(f'./chat/{mysong}')
        mixer.music.play()
        # Say stop to stop the music any time
        while True:
            background=voice_to_text().lower()
            if "stop" in background:
                mixer.music.stop()
                break
            else:
                continue
