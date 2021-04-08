import arrow

# Get today's date
today_date = arrow.now()

# Print today's date in differnt formats
print("today is", today_date.format('MMMM DD, YYYY'))
print("today is", today_date.format('MMM D, YYYY'))
print("today is", today_date.format('MM/DD/YYYY'))
# Print today's weekday in differnt formats
print("today is", today_date.format('dddd'))
print("today is", today_date.format('ddd'))
