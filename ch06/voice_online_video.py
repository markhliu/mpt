# Import functions from the loacal package
from mptpkg import voice_to_text, print_say

# Put chromedriver.exe in the same folder as this script
from selenium import webdriver

def online_video():
    global button
    browser = webdriver.Chrome(executable_path='./chromedriver')
    browser.get("https://www.nbcnews.com/nightly-news-full-episodes")
    button = browser.find_element_by_xpath\
('//*[@id="content"]/div[6]/div/div[3]/div/\
 section[2]/div[2]/div/div[1]/article/div[1]/h2/a[2]/span')
    button.click()

while True:
    print_say("how may I help you?")
    inp = voice_to_text().lower()
    print_say(f'you just said {inp}')
    if inp == "stop listening":
        print('Goodbye!')
        break
    elif "video" in inp:
        print_say('OK, play online video for you!')
        online_video()
        break