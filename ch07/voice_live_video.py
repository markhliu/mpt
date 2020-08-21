# Put chromedriver.exe in the same folder as this script
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  

# Add the one-level-up directory to the searchable space
import sys
sys.path.append('../')

# Import functions from the local package
from mypkg.mysr import voice_to_text
from mypkg.mysay import print_say

# Define a live_radio() function
def live_video():
    global button
    browser = webdriver.Chrome(executable_path='./chromedriver')
    browser.get("https://www.nbcnews.com/nightly-news-full-episodes")
    button = browser.find_element_by_xpath('//*[@id="__next"]/div[2]/div[4]/div/div[3]/div/section[1]/div/article/div[1]/h2/a[2]/span')
    button.click()
# Start the loop
while True:   
    print('Python is listening...')
    print_say("How may I help you?")
    inp=voice_to_text().lower()
    print_say(f'You just said {inp}.')
    if inp=="stop listening":
        print_say('Goodbye!')
        break
    elif "video" in inp: 
        print_say('OK, play live video online for you!')
        live_video()
        # Say stop to stop the radio any time
        while True:
            background=voice_to_text().lower()
            if "stop" in background:
                button.click()
                break
            else:
                continue
