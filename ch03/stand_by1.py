# Make sure you put mysr.py in the same folder as this script
from mysr import voice_to_text

while True:   
    print('Python is listening...')
    inp = voice_to_text()
    print(f'You just said {inp}.')
    if inp == "stop listening":
        print('Goodbye!')
        break
