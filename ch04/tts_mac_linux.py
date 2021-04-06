import os

while True: 
    inp = input("What do you want to covert to speech?\n") 
    if inp == "done": 
        print(f"You just typed in {inp}; goodbye!")
        os.system(f'gtts-cli --nocheck "You just typed in {inp}; goodbye!" | mpg123 -q -')
        break
    else: 
        print(f"You just typed in {inp}")
        os.system(f'gtts-cli --nocheck "You just typed in {inp}" | mpg123 -q -')
        continue 
