# Import needed modules
import requests
import bs4
import webbrowser

# Locate the website for the NPR news brief
url = 'https://www.npr.org/podcasts/500005/npr-news-now'
# Convert the source code to a soup string
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
# Locate the tag that contains the mp3 files
casts = soup.findAll('a', {'class': 'audio-module-listen'})
print(casts)
# Obtain the weblink for the mp3 file related to the latest news brief
cast = casts[0]['href']
print(cast)
# Remove the unwanted components in the link
pos = cast.find('?')
print(cast[0:pos])
# Extract the mp3 file link, and play the file
mymp3 = cast[0:pos]
webbrowser.open(mymp3)