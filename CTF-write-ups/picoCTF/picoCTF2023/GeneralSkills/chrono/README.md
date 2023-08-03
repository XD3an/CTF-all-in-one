# chrono

## Information

### Description

How to automate tasks to run at intervals on linux servers?
Additional details will be available after launching your challenge instance.

### Hints

(None)

## Solution

- Crash

```sh
picoplayer@challenge:~$ ls -la
total 12
drwxr-xr-x 1 picoplayer picoplayer   44 Mar 15 07:20 .
drwxr-xr-x 1 root       root         24 Mar 15 02:28 ..
-rw-r--r-- 1 picoplayer picoplayer  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 picoplayer picoplayer 3771 Feb 25  2020 .bashrc
drwx------ 2 picoplayer picoplayer   34 Mar 15 07:18 .cache
-rw-r--r-- 1 picoplayer picoplayer  807 Feb 25  2020 .profile
-rw-rw-r-- 1 picoplayer picoplayer    0 Mar 15 07:20 .selected_editor
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
{"flag": "picoCTF{Sch3DUL7NG_T45K3_L1NUX_dac54671}", "username": "picoplayer", "password": "WIDO+9VDTc"}
```