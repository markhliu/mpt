from bs4 import BeautifulSoup
import requests
url = 'http://libraries.uky.edu'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
div = soup.find('div', class_="sf-middle")
contact = div.find("div", class_="dashing-li-last")
area = contact.find('span', class_="featured_area")
print(area.text)
atag = contact.find('span', class_="featured_email")
print(atag.text)
