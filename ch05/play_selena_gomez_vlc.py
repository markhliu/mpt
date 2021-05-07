'''
For copyright reasons, put your own songs in /mpt/ch05/chat/

You must have the VLC player installed on your computer
Go to https://www.videolan.org/index.html and download the software and install it. 
In Linux, install using this command
sudo apt-get install vlc 

To install the vlc Python module, use the following command with your virtual environment activated
pip install python-vlc 

If vlc doesn't work, use pygame or playsound or pydub
e.g., the script pay_selena_gomez.py uses pygame 

'''

import os
import random
from vlc import MediaPlayer

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
    # If 'play' is in voice command, music mode is activated
    elif "play" in inp:
        # Remove the word play from voice command
        inp = inp.replace('play ', '')
        # Separate first and last names
        names = inp.split()
        # Extract the first name
        firstname = names[0]
        # Extract the last name
        if len(names) > 1:
            lastname = names[1]
        # If no last name, use the first name as last name;  
        else:
            lastname = firstname
        # Create a list to contain songs 
        mysongs = []
        # If either first name or last name in the file name, put in list
        with os.scandir("./chat") as files:
            for file in files:
                if (firstname in file.name or lastname in file.name) \
                        and "mp3" in file.name:
                    mysongs.append(file.name)
        # Randomly select one from the list and play
        mysong = random.choice(mysongs)
        print_say(f"Play the song {mysong} for you.")
        player = MediaPlayer(f'./chat/{mysong}')
        player.play()
        break
