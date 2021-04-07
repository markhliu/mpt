from random import choice

import requests
import bs4
from pygame import mixer

# Import functions from the loacal package
from mptpkg import voice_to_text, print_say


# Define the news_brief() function
def news_brief():
    # Locate the website for the NPR news brief
    url = 'https://www.npr.org/podcasts/500005/npr-news-now'
    # Convert the source code to a soup string
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    # Locate the tag that contains the mp3 files
    casts = soup.findAll('a', {'class': 'audio-module-listen'})
    # Obtain the weblink for the mp3 file
    cast = casts[0]['href']
    # Remove the unwanted components in the link
    pos = cast.find('?')
    # Download the mp3 file
    mymp3 = cast[0:pos]
    x = choice(range(1000000))
    mymp3 = requests.get(mymp3)
    with open(f'f{x}.mp3', 'wb') as f:
        f.write(mymp3.content)
    # play the mp3 file
    mixer.init()
    mixer.music.load(f'f{x}.mp3')
    mixer.music.play()


# Start the loop
while True:
    print('Python is listening...')
    print_say("How may I help you?")
    inp = voice_to_text().lower()
    print_say(f'You just said {inp}.')
    if inp == "stop listening":
        print_say('Goodbye!')
        break
    elif "news" in inp:
        news_brief()
        # Say stop to stop the music any time
        while True:
            background = voice_to_text().lower()
            if "stop" in background:
                mixer.music.stop()
                break
            else:
                continue
