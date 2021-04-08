import arrow

# Current time in HH:MM:SS format
current_time = arrow.now().format('H:m:s')
print('the current time is', current_time)
current_time12 = arrow.now().format('hh:mm:ss A')
print('the current time is', current_time12)
# We can also print out hour, minute, and second individually
print("the current hour is", arrow.now().format('H'))
print("the current minute is", arrow.now().format('m'))
print("the current second is", arrow.now().format('s'))
