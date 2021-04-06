import wikipedia

# Import functions from the loacal package
from mptpkg import voice_to_text, print_say

# Ask what you want to know
print_say("What do you want to know?")
# Capture your voice input
my_query = voice_to_text()
print_say(f"you said {my_query}")
# Obtain answer from Wikipedia
ans = wikipedia.summary(my_query)
# Speak the answer in a human voice
print_say(ans[0:200])
