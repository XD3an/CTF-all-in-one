from Crypto.Util.number import long_to_bytes

def main() -> None:
    f = open('input.txt', 'r')
    r = int(f.read())
    hFlag = r*5
    flag = long_to_bytes(hFlag)
    print(flag)

if __name__=='__main__':
    main()