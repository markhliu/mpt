# Put your web driver in the same folder as this script
from selenium import web driver
browser = webdriver.Chrome(executable_path='./chromedriver')
browser.get("https://onlineradiobox.com/us/")
button = browser.find_element_by_xpath('//*[@id="b_top_play"]')
button.click()
