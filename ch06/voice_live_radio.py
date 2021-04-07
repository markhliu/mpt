# Put chromedriver.exe in the same folder as this script
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  

# Import functions from the loacal package
from mptpkg import voice_to_text, print_say

# Define a live_radio() function
def live_radio():
    global button
    chrome_options = Options()  
    chrome_options.add_argument("--headless") 
    browser = webdriver.Chrome\
    (executable_path='./chromedriver',chrome_options=chrome_options)
    browser.get("https://onlineradiobox.com/us/")
    button = browser.find_element_by_xpath('//*[@id="b_top_play"]')
    button.click()
# Start the loop
while True:   
    print_say("How may I help you?")
    inp = voice_to_text().lower()
    print_say(f'You just said {inp}.')
    if inp == "stop listening":
        print_say('Goodbye!')
        break
    elif "radio" in inp: 
        print_say('OK, play live radio online for you!')
        live_radio()
        # Say stop playing to stop the radio any time
        while True:
            background = voice_to_text().lower()
            if "stop playing" in background:
                button.click()
                break
            else:
                continue
