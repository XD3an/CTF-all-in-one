flag = ''
with open('recv_this', 'r') as f:
    flag = list(f.read())

for i in range(0, 23):
    if i <= 7:
        flag[i]=flag[i]
    elif i>=8 and i<=22 and i&1!=0:
        flag[i]=chr(ord(flag[i])+2)
    else:
        flag[i]=chr(ord(flag[i])-5)
    
print(''.join(flag))