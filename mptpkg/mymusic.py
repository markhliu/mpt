import os
import random
from pygame import mixer

from mptpkg import print_say

# Define a function to play music
def music_play(v_inp):   
    # Extract artist name
    pos = v_inp.find("music by ")
    v_inp = v_inp[pos+len('music by '):]
    # Separate first and last names
    names = v_inp.split()
    # Extract the first name
    firstname = names[0]
    # Extract the last name
    if len(names)>1:
        lastname = names[1]
    # If no last name, use first name as placeholder  
    else:
        lastname = firstname
    # Create a list to contain songs 
    mysongs = []
    # If either first name or last name in the file name, put in list
    with os.scandir("../ch05/chat") as files:
        for file in files:
            if (firstname in file.name.lower() or lastname\
                in file.name.lower()) and "mp3" in file.name:
                mysongs.append(file.name)
    # Let you know if no song by the artist
    if len(mysongs) == 0:
        print_say(f"I cannot find any song by {names}.")
    else:
        # Randomly select one from the list and play
        mysong = random.choice(mysongs)
        print_say(f"play the song {mysong} for you.")
        mixer.init()
        mixer.music.load(f'../ch05/chat/{mysong}')
        mixer.music.play()

# Define a function to stop music
def music_stop(): 
    try:
        mixer.music.stop()
    except:
        print('no music to stop')

