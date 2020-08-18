# Put mysay.py in the same folder as this script
from mysay import print_say

# Open and load the content of the text file
with open('storm.txt','r') as f:
    content=f.read()
# Let Python print and speak the text in the file   
print_say(content)
