# Import the Beautiful Soup library
from bs4 import BeautifulSoup

# Open the local HTML file as a text file
textfile = open("UKYexample.html", encoding='utf8')
# Use the findAll() function to locate all <p> tags
soup = BeautifulSoup(textfile, "html.parser")
ptags = soup.findAll("p")
# Print out <p> tags
print(ptags)
# Find the <a> tag nested in the third <p> tag
atag = ptags[2].find("a")
print(atag)
# Print the web address of the hyperlink
print(atag['href'])
# Print the content of the <a> tag
print(atag.text)



