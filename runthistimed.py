from datetime import datetime, time
import time as t
import os
import socket


# NOTE: this will only work on Linux/Unix or Mac. Not tested for Windows
# Runs until set t. 
def main():
    while is_time_between(time(6,30), time(1,30)):
        os.system('python unifipresence.py')
        t.sleep(10)

def is_time_between(begin_time=None, end_time=None):
    check_t = datetime.now().time()
    if begin_time < end_time:
        return check_t >= begin_time and check_t <= end_time
    else: # crosses midnight
        return check_t >= begin_time or check_t <= end_time

if __name__ == '__main__':
	main()