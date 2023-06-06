import time
import datetime as dt

now = dt.datetime.now()
timestamp = time.time()

print("Seconds since January 1, 1970: " + '{:,.4f}'.format(timestamp) + " or " + '{:.2e}'.format(timestamp) + " in scientific notation")
print(now.strftime("%b %d %Y"))