# Exercises - Day 16

from datetime import datetime

# Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
print(now.day, now.month, now.year, now.hour, now.minute, now.timestamp())

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
print(now.strftime('%m/%d/%Y, %H:%M:%S'))

# Today is 5 December, 2019. Change this time string to time
past = datetime.strptime('5 December, 2019', '%d %B, %Y')

# Calculate the time difference between now and new year
t1 = datetime(year = now.year, month = now.month, day = now.day, hour = now.hour, minute = now.minute, second = now.second)
t2 = datetime(year = 2027, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff)

# Calculate the time difference between 1 January 1970 and now
new_year = datetime(now.year + 1, 1, 1)
epoch = datetime(1970, 1, 1)
print(past, new_year - now, now - epoch)

# datetime is useful for timestamps, schedules, time-series data, and dated posts.
