from bs4 import BeautifulSoup
import requests

# Provide the web address of the live web
url = 'http://libraries.uky.edu'
# Obtain information from the live web
page = requests.get(url)
# Parse the page to obtain the parent div tag
soup = BeautifulSoup(page.text, "html.parser")
div = soup.find('div', class_="sf-middle")
# Locate the three child div tags
contacts = div.find_all("div", class_="dashing-li")
# Print out the first child div tag to examine it
print(contacts[0])
# Obtain information from each child tag
for contact in contacts:
    # Obtain the area name
    area = contact.find('span', class_="contact_area")
    print(area.text)
    # Obtain the phone and email
    atags = contact.find_all('a', href = True)
    for atag in atags:
        print(atag.text)
