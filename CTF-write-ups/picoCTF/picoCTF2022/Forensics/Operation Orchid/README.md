# Operation Orchid

## Information

### Description

Download this disk image and find the flag.
Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.
* Download compressed disk image

### Hints

(None)

## Solution

1. 透過映像檔將在 Partition 3 的 /root/root 中可以得到以下檔案
* flag.txt.enc
* .ash_history

2. 透過 .ash_history 中的內容可以知道是利用以下指令進行加密
```sh
    $ openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
```

3. 將 flag.txt.enc 載下來，再根據加密方式反向解密
```sh
    $ openssl aes256 -d -salt -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567
```
