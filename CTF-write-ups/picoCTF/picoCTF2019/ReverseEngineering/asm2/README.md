# vault-door-4

## Information

### Description

What does asm2(0x4,0x2d) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. Source

### Hints

1. assembly conditions

## Solution

- 按照指令順序執行。
    ```
    asm2:
        <+0>:	push   ebp
        <+1>:	mov    ebp,esp
        <+3>:	sub    esp,0x10
        <+6>:	mov    eax,DWORD PTR [ebp+0xc]
        <+9>:	mov    DWORD PTR [ebp-0x4],eax
        <+12>:	mov    eax,DWORD PTR [ebp+0x8]
        <+15>:	mov    DWORD PTR [ebp-0x8],eax
        <+18>:	jmp    0x50c <asm2+31>
        <+20>:	add    DWORD PTR [ebp-0x4],0x1
        <+24>:	add    DWORD PTR [ebp-0x8],0xd1
        <+31>:	cmp    DWORD PTR [ebp-0x8],0x5fa1
        <+38>:	jle    0x501 <asm2+20>
        <+40>:	mov    eax,DWORD PTR [ebp-0x4]
        <+43>:	leave  
        <+44>:	ret    

- 注意 Stack layout
    +------------+
        old ebp    <- ebp
    +------------+
        ret        <- ebp+0x4
    +------------+
        arg1       <- ebp+0x8
    +------------+
        arg2       <- ebp+0xc
    +------------+