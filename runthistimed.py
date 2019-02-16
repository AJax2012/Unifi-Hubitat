from datetime import datetime, time
import os

# NOTE: this will only work on Linux/Unix or Mac. Not tested for Windows
# Runs until set time. 
def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.utcnow().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time

while is_time_between(time(6,30), time(1,30), datetime._local_timezone):
    os.system('python unifipresence.py')
    time.sleep(10)