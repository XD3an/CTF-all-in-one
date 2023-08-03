# Sleuthkit Intro

## Information

### Description

Download the disk image and use mmls on it to find the size of the Linux partition. Connect to the remote checker service to check your answer and get the flag.
Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.
Download disk image
Access checker program: nc saturn.picoctf.net 52279

###

(None)

## Solution
* **mmls**:  Display the partition layout of a volume system(partition tables)
* 先解壓縮後再利用 mmls 抓出內容，最後 nc saturn.picoctf.net 52279，再根據問題回答就可以得到 flag 了。
