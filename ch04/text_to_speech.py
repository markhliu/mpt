import pyttsx3

engine = pyttsx3.init()
while True:
    inp = input("What do you want to covert to speech?\n")
    if inp == "done":
         print(f"You just typed in {inp}, goodbye!")
         engine.say(f"You just typed in {inp}, goodbye!")
         engine.runAndWait()        
         break
    else:
        print(f"You just typed in {inp}")
        engine.say(f"You just typed in {inp}")
        engine.runAndWait()
        continue

