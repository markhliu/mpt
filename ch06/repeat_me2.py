# Add the one-level-up directory to the searchable space
import sys
sys.path.append('../')

# Import functions from the loacal package
from mypkg.mysr import voice_to_text
from mypkg.mysay import print_say

while True:   
    print('Python is listening...')
    inp = voice_to_text()
    if inp == "stop listening":
        print_say(f'you just said {inp}, Goodbye!')
        break
    else:
        print_say(f'You just said {inp}.')
        continue
