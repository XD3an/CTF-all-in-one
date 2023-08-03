encrypted = [0x8A, 0x50, 0x92, 0xC8, 0x06, 0x3D, 0x5B, 0x95, 0xB6, 0x52, 0x1B,
            0x35, 0x82, 0x5A, 0xEA, 0xF8, 0x94, 0x28, 0x72, 0xDD, 0xD4, 0x5D,
            0xE3, 0x29, 0xBA, 0x58, 0x52, 0xA8, 0x64, 0x35, 0x81, 0xAC, 0x0A,
            0x64]

def Decrypt(data):
    decrypted = ""
    for i in range(len(data)):
        byte = (data[i] - 8 )&0xff
        byte = (((byte >> ((i ^ 9) & 3)) | (byte << (8 - ((i ^ 9) & 3))))&0xff)^i
        decrypted += chr(byte)
    return decrypted

def main():
    print(Decrypt(encrypted))

if __name__=='__main__':
    main()