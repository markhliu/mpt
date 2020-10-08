from myplot import price_plot
from mychart import candle_stick
from mptpkg import voice_to_text, print_say

# Start an infinite loop
while True:
    # Obtain voice input from you
    print_say("How may I help you?")
    inp = voice_to_text()
    print_say(f"You said {inp}.")
    # If you want to stop, say "stop listening"
    if "stop listening" in inp:
        print_say("Nice talking to you, goodbye!")
        break
    # If "price pattern for" in voice, activate plot functionality
    elif "price pattern for" in inp:
        pos = inp.find('price pattern for ')
        firm = inp[pos+len('price pattern for '):]
        price_plot(firm)
        continue
    # If "candlestick chart for" in voice, activate chart functionality
    elif "chart for" in inp:
        pos = inp.find('chart for ')
        firm = inp[pos+len('chart for '):]
        candle_stick(firm)
        continue
    # Otherwise, go to the next iteration
    else:
        continue
        
