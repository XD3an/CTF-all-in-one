import base64

str = 'JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTY1JTMzJTMxJTM1JTMyJTYyJTY2JTM0'

url_encode = base64.b64decode(str).decode().split("%")
print(url_encode)


flag='picoCTF{'
for i in url_encode:
    if i == '':
        continue
    flag += chr(int(i, 16))
flag+='}'

print(flag)
