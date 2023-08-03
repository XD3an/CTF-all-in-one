serial = "5B134977135E7D13"
xor_var=[0x10, 0x20, 0x30]


# serial to hex
def serial_to_hex():     
    serial_hex = []
    for i in range(0, len(serial), 2):
        serial_hex.append(int(serial[i]+serial[i+1], 16))
    return serial_hex

# crack to get "name"
def crack_name():
    name = ""
    i = 0
    for i in range(len(serial)):
        name += chr(serial[i] ^ xor_var[i%3])
    return name

if __name__=='__main__':
    serial = serial_to_hex()
    print(crack_name())
