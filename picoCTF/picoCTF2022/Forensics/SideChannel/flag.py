#! /usr/bin/python

import time, os

LEN = 8
CHOICES = "0123456789"

% check each digit
def check(prefix):
    max_time = -1
    res = ""
    for c in CHOICES:
        current = f"{prefix}{c}".ljust(8,'0')
        print(f"try {current}")
        total_time = 0
        for _ in range(3):
            start_time = time.time()
            os.system(f"echo {current} | ./pin_checker > /dev/null")
            total_time += (time.time() - start_time)
        avg_time = total_time/10
        if avg_time > max_time:
            max_time = avg_time
            res = c
    return res

if __name__=="__main__":
    prefix = ""
    % check 1-7 digit
    for i in range(7):
        c = check(prefix)
        prefix = f"{prefix}{c}"
    % try to input PIN to program
    for c in CHOICES:
        current = f"{prefix}{c}"
        print(f" try {current}")
        os.system(f"echo {current} | ./pin_checker")


