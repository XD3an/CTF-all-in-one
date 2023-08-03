# Eavesdrop

## Information


### Description

Download this packet capture and find the flag.
* Download packet capture

### Hints

1. All we know is that this packet capture includes a chat conversation and a file transfer.

## Solution
* 透過 Wireshark 觀察封包內容，Hints告訴這是一則對話，從對話中找出關鍵資訊
```
Hey, how do you decrypt this file again?
You're serious?
Yeah, I'm serious
*sigh* openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123
Ok, great, thanks.
Let's use Discord next time, it's more secure.
C'mon, no one knows we use this program like this!
Whatever.
Hey.
Yeah?
Could you transfer the file to me again?
Oh great. Ok, over 9002?
Yeah, listening.
Sent it
Got it.
You're unbelievable
```
```
53616c7465645f5fbf1f3543c1437d489ac5c700f4809146799c9d503b551476a3f06159293bee7c9e5183fb5c4a184c
```
* 再根據資訊內容得到 flag
```sh
    $openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123
    $ cat file.txt                                                      picoCTF{nc_73115_411_0ee7267a}
```



