# Put mysr.py and mysay.py in the same folder as this script
from mysr import voice_to_text
from mysay import print_say

while True:   
    print('Python is listening...')
    inp = voice_to_text()
    if inp == "stop listening":
        print_say(f'You just said {inp}, goodbye!')
        break
    else:
        print_say(f'You just said {inp}')
        continue 
