# Put mysr.py and mysay.py in the same folder as this script
from mysr import voice_to_text
from mysay import print_say

# Ask the length of the rectangle
print_say('What is the length of the rectangle?')
# Convert the voice input to a variable inp1
inp1 = voice_to_text()
print_say(f'You just said {inp1}.')
# Ask the width of the rectangle
print_say('What is the width of the rectangle?')
# Save the answer as inp2
inp2 = voice_to_text()
print_say(f'You just said {inp2}.')
# Calculate the area
area = float(inp1)*float(inp2)
# Print and speak the result
print_say(f'The area of the rectangle is {area}.')

