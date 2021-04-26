
''' Before running this script, add the following in /mpt/mptpkg/__init__.py
from .mymusic import music_play, music_stop
from .mynews import news_brief, news_stop
from .myradio import live_radio, radio_stop
from .myttt import ttt
from .myconn import conn
from .mystock import stock_market, stock_price
from .mytranslate import voice_translate
'''

import random
import json

# Ensure the following functions are imported in /mpt/mptpkg/__init__.py
from mptpkg import voice_to_text, print_say, wakeup, timer,\
 alarm, joke, email, know_all, music_play, music_stop,\
 news_brief, news_stop, live_radio, radio_stop, ttt,\
 conn, stock_price, stock_market, voice_translate

# Open chats.json and put it in a dictionary
with open('chats.json','r') as content:
    chats = json.load(content)
# Put the program in standby
while True:
    # Capture your voice command quietly in standby
    wake_up = wakeup()
    # You can wake up the program by saying "Hello Python"
    while wake_up == "Activated": 
        # Prompt you to ask questions
        print_say("How may I help you?")
        inp = voice_to_text().lower()
        print_say(f'You just said {inp}.')  
        # The program goes back to standby if you choose
        if "back" in inp and "stand" in inp:
            print_say('OK, back to standby, let me know if you need help!')
            break
        # Activate chatting
        elif inp in list(chats.keys()):
            print_say(random.choice(chats[inp]))
            continue  
        # Activate music
        elif "music by" in inp:
            music_play(inp)
            # Say stop to stop the music any time
            while True:
                background = voice_to_text().lower()
                if "stop" in background:
                    music_stop()
                    break
                else:
                    continue
        # Activate news 
        elif "npr news" in inp:
            news_brief()
            # Say stop to stop the news any time
            while True:
                background = voice_to_text().lower()
                if "stop" in background:
                    news_stop()
                    break
                else:
                    continue
        # Activate the radio 
        # Put chromedriver.exe in the same folder as this script 
        elif "live radio" in inp:
            live_radio()
            # Say stop to stop the radio any time
            while True:
                background = voice_to_text().lower()
                if "stop" in background:
                    radio_stop()
                    break
                else:
                    continue
        # Activate the Tic Tac Toe game
        elif "tic" in inp and "tac" in inp and "toe" in inp:
            ttt()
            continue
        # Activate the Connect Four game
        elif "connect" in inp and ('4' in inp or 'four' in inp):
            conn()
            continue
        # Activate the stock price functionality
        elif "stock price of" in inp:
            stock_price(inp)
            continue
        # Get market indexes
        elif "stock market" in inp:
            stock_market()
            continue
        # Activate the voice translator
        elif "how to say" in inp and " in " in inp:
            voice_translate(inp)
            continue
        # Activate the timer
        elif "timer for" in inp and ("hour" in inp or "minute" in inp):
            timer(inp)
            continue        
        # Activate the alarm clock 
        elif "alarm for" in inp and ("a.m." in inp or "p.m." in inp):
            alarm(inp)
            continue
        # Activate joke-telling functionality
        elif "joke" in inp and "tell" in inp:
            joke()
            continue
        # Activate the email-sending functionality
        elif "send" in inp and "email" in inp:
            email()
            continue
        # Activate the know-it-all functionality
        else:
            if len(inp)>6:
                know_all(inp)
            continue
    # You can end the script by inlcuding "stop" in your voice
    if wake_up == "ToQuit":
        print_say("OK, exit the VPA, goodbye!")
        break
