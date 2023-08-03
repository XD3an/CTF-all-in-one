# SideChannel

## Information

### Description

There's something fishy about this PIN-code checker, can you figure out the PIN and get the flag?
Download the PIN checker program here pin_checker
Once you've figured out the PIN (and gotten the checker program to accept it), connect to the master server using nc saturn.picoctf.net 52680 and provide it the PIN to get your flag.

### Hints

1. Read about "timing-based side-channel attacks."

2. Attempting to reverse-engineer or exploit the binary won't help you, you can figure out the PIN just by interacting with it and measuring certain properties about it.

3. Don't run your attacks against the master server, it is secured against them. The PIN code you get from the pin_checker binary is the same as the one for the master server.

## Solution
* 側信道攻擊(side channel attack): 透過基於密碼系統的物理實現方式中獲取資訊而非破壞其演算法。
    * 計時攻擊 (Timing Attack、Timing-Based Side-Channel Attacks)
    * 快取攻擊 (Cache Side-Channel Attack)
    * 能量分析（Power analysis）
    * 電磁攻擊 (Electromagnetic Attack)
    * ...
```py
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
```

