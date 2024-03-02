import time
from _datetime import datetime

curr_time = time.time()
scientific_notation = "{:.2e}".format(curr_time)
curr_date = datetime.now()
formatted_date = curr_date.strftime("%b %d %Y")

print("Seconds since January 1, 1970: " + str(curr_time) + " or " + scientific_notation + " in scientific notation.")
print(formatted_date)
