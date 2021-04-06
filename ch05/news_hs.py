import requests
import bs4
import sys

# Import functions from the loacal package
from mptpkg import voice_to_text, print_say

# Define the news_teaser() function
def news_teaser():
    # Obtain the source code from the news website
    res = requests.get('https://www.npr.org/sections/news/')
    res.raise_for_status()
    # Use beautiful soup to parse the code
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # Get the div tags that contain titles and teasers
    div_tags = soup.find_all('div',class_="item-info")
    # Index different news
    news_index=1
    # Go into each div tag to retrieve the title and the teaser
    for div_tag in div_tags:
        # Print the news index to separate different news
        print_say(f'News Summary {news_index}')
        # Retrieve and print the h2 tag that contains the title
        h2tag = div_tag.find('h2', class_="title")
        print_say(h2tag.text)
        # Retrieve and print the p tag that contains the teaser
        ptag = div_tag.find('p', class_="teaser")
        print_say(ptag.text)
        # Limit to the first 10 news summaries
        news_index += 1
        if news_index>10:
            break
# Print and ask you if you like to hear the news summary
print_say("Would you like to hear the NPR news summary?")
# Capture your voice command
inp=voice_to_text().lower()
# If you answer yes, activate the newscast
if inp=="yes":
    news_teaser()
# otherwise, exit the script
else: 
    sys.exit

























