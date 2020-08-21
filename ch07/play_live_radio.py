# Put chromedriver.exe in the same folder as this script
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  

chrome_options = Options()  
chrome_options.add_argument("--headless") 
browser = webdriver.Chrome(executable_path='./chromedriver',chrome_options=chrome_options)
browser.get("https://onlineradiobox.com/us/")
button = browser.find_element_by_xpath('//*[@id="b_top_play"]')
button.click()
