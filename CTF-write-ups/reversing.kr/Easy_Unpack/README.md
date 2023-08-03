# Easy Unpack

## Information

-  src: [reversing.kr](http://reversing.kr/challenge.php)

## Solution

### method 1

- 透過 x64dbg 追蹤，找出解殼後，一次大 jmp 後的 entry points，即為 OEP。

### method 2

- 透過 IDA 尋找，現今版本 IDA 可以找到此殼下的 OEP。

