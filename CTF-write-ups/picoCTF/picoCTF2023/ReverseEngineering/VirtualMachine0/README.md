# Virtual Machine 0

## Information

### Description

Can you crack this black box? We grabbed this design doc from enemy servers: Download. We know that the rotation of the red axle is input and the rotation of the blue axle is output. The following input gives the flag as output: Download.

### Hints

1. Rotating the axle that number of times is obviously not feasible. Can you model the mathematical relationship between red and blue?

## Solution

1. 透過以下工具建立模型
    - [https://3dviewer.net/#](https://3dviewer.net/#)

然後會將外部某些組件關閉，然後就可以看到內部的結構，依據題目意思，計算兩個齒輪之間的齒輪比。
    - 齒輪比：40:8 -> 5

2. 取得 flag
    ```py
    from Crypto.Util.number import long_to_bytes

    def main() -> None:
        f = open('input.txt', 'r')
        r = int(f.read())
        hFlag = r*5
        flag = long_to_bytes(hFlag)
        print(flag)

    if __name__=='__main__':
        main()
    ```