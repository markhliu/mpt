import arrow

# Current time in HH:MM:SS format
current_time = arrow.utcnow().format('H:m:s')
print('the current time is', current_time)
current_time12 = arrow.utcnow().format('hh:mm:ss A')
print('the current time is', current_time12)
# We can also print out hour, minute, and second individually
print("the current hour is",arrow.utcnow().format('H'))
print("the current minute is",arrow.utcnow().format('m'))
print("the current second is",arrow.utcnow().format('s'))
