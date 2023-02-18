# Easy Keygen

## Information

- src: [reversing.kr](http://reversing.kr/challenge.php)

## Solution


### 觀察程式相關資訊

```
ReversingKr KeygenMe

Find the Name when the Serial is 5B134977135E7D13
```

![Untitled](Easy%20Keygen%204e71afd6024740e481771d3541a35a32/Untitled.png)


![Untitled](Easy%20Keygen%204e71afd6024740e481771d3541a35a32/Untitled%201.png)

- 沒殼

### 分析

- 程式會要求輸入 name 與 serial，serial 會根據 name 所變動，會將 name 與 [0x10, 0x20, 0x30]的循環作 xor 運算取得正確的 serial，根據輸入的 serial 作比對，以判斷是否成功。

### Flag

- flag.py
    
    ```python
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
    ```