from random import choice

import requests
import bs4
from pygame import mixer

# Define news_brief() function
def news_brief():
    # Locate the website for the NPR news brief
    url = 'https://www.npr.org/podcasts/500005/npr-news-now'
    # Convert the source code to a soup string
    response = requests.get(url)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, 'html.parser')   
    # Locate the tag that contains the mp3 files
    casts = soup.findAll('a', {'class': 'audio-module-listen'})
    # Obtain the weblink for the mp3 file related to the latest news brief
    cast = casts[0]['href']
    pos = cast.find("?")
    # Download the mp3 file
    mymp3 = cast[0:pos]
    x = choice(range(1000000))
    mymp3_file = requests.get(mymp3)
    with open(f'f{x}.mp3','wb') as f:
        f.write(mymp3_file.content)
    # Play the mp3 file
    mixer.init()
    mixer.music.load(f'f{x}.mp3')
    mixer.music.play()

# Define the news_stop() function
def news_stop():
    try:
        mixer.music.stop()
    except:
        print('no news to stop')
