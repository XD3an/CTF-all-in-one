# Permissions

## Information

### Description

Can you read files in the root file?
Additional details will be available after launching your challenge instance.

### Hints

(None)

## Solution

- Crash
```sh
picoplayer@challenge:~$ ls
picoplayer@challenge:~$ ls -la
total 12
drwxr-xr-x 1 picoplayer picoplayer   20 Mar 15 07:27 .
drwxr-xr-x 1 root       root         24 Mar 15 02:46 ..
-rw-r--r-- 1 picoplayer picoplayer  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 picoplayer picoplayer 3771 Feb 25  2020 .bashrc
drwx------ 2 picoplayer picoplayer   34 Mar 15 07:27 .cache
-rw-r--r-- 1 picoplayer picoplayer  807 Feb 25  2020 .profile
picoplayer@challenge:~$ cd ..
picoplayer@challenge:/home$ ls
picoplayer
picoplayer@challenge:/home$ cd ..
picoplayer@challenge:/$ ls
bin   challenge  etc   lib    lib64   media  opt   root  sbin  sys  usr
boot  dev        home  lib32  libx32  mnt    proc  run   srv   tmp  var
picoplayer@challenge:/$ cd challenge/
picoplayer@challenge:/challenge$ ls
metadata.json
picoplayer@challenge:/challenge$ cat metadata.json
{"flag": "picoCTF{uS1ng_v1m_3dit0r_43f94368}", "username": "picoplayer", "password": "xySNSir+CT"}
```