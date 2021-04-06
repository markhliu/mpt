import requests
import bs4

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
    print(f'News Summary {news_index}')
    # Retrieve and print the h2 tag that contains the title
    h2tag = div_tag.find('h2', class_="title")
    print(h2tag.text)
    # Retrieve and print the p tag that contains the teaser
    ptag = div_tag.find('p', class_="teaser")
    print(ptag.text)
    # Limit to the first 10 news summaries
    news_index += 1
    if news_index>10:
        break













