not_flag = 'jU5t_a_sna_3lpm18g947_u_4_m9r54f'

flag = ''.ljust(32, '1')
flag = list(flag)

print(flag)

for i in range(8):
    flag[i] = not_flag[i]

for i in range(8, 16):
    flag[i] = not_flag[23-i]

for i in range(16, 32, 2):
    flag[i] = not_flag[46-i]

for i in range(31, 16, -2):
    flag[i] = not_flag[i]


print('picoCTF{', ''.join(flag), '}', sep='')