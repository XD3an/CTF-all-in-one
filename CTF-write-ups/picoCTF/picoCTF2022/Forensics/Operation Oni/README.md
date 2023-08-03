# Operation Oni

## Information

### Description

Download this disk image, find the key and log into the remote machine.
Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.
Download disk image
Remote machine: ssh -i key_file -p 62300 ctf-player@saturn.picoctf.net

Note: you must launch a challenge instance in order to view your disk image download link.

### Hints

(None)

## Solution

這裡要通過給予的映像檔中提取 .ssh 的 key ，再通過 key 進行 ssh 登入，登入後就可以看到 flag.txt。


