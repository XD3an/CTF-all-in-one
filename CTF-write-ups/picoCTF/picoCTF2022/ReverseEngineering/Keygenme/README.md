# Keygenme

## Information

### Description

Can you get the flag?
Reverse engineer this binary.

### Hints

(None)

## Solution

### Ghidra
* 可以發現程式中不存在 main function，不過有 entry function 可以下手，於是先從 entry 開始。
```c
void entry(undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  undefined8 in_stack_00000000;
  undefined auStack8 [8];
  
  __libc_start_main(FUN_0010148b,in_stack_00000000,&stack0x00000008,FUN_00101520,FUN_00101590,
                    param_3,auStack8);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}
```
* 跟進去 **FUN_0010148b**。
```c
undefined8 FUN_0010148b(void)

{
  char cVar1;
  long in_FS_OFFSET;
  char buffer [40];
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  printf("Enter your license key: ");
  fgets(buffer,0x25,stdin);
  cVar1 = FUN_00101209(buffer);
  if (cVar1 == '\0') {
    puts("That key is invalid.");
  }
  else {
    puts("That key is valid.");
  }
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```
* 可以從 **FUN_0010148b** 發現會要求使用者輸入，再根據 **FUN_00101209** 的回傳結果判斷是否 valid，嘗試跟進去 **FUN_00101209** 看看。
```c
undefined8 FUN_00101209(char *param_1)

{
  size_t sVar1;
  undefined8 uVar2;
  long in_FS_OFFSET;
  int local_d0;
  int i;
  int j;
  int k;
  int local_c0;
  undefined2 local_ba;
  byte local_b8 [16];
  byte local_a8 [16];
  undefined8 local_98;
  undefined8 local_90;
  undefined8 local_88;
  undefined4 local_80;
  char local_78 [12];
  undefined local_6c;
  undefined local_66;
  undefined local_5f;
  undefined local_5e;
  char local_58 [32];
  char acStack56 [40];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_98 = L'\x6f636970';
  local_90 = L'\x6e317262';
  local_88 = L'\x305f7275';
  local_80 = L'\x005f7933';
  local_ba = L'}';
  sVar1 = strlen((char *)&local_98);
  MD5((uchar *)&local_98,sVar1,local_b8);
  sVar1 = strlen((char *)&local_ba);
  MD5((uchar *)&local_ba,sVar1,local_a8);
  local_d0 = 0;
  for (i = 0; i < 16; i = i + 1) {
    sprintf(local_78 + local_d0,"%02x",(ulong)local_b8[i]);
    local_d0 = local_d0 + 2;
  }
  local_d0 = 0;
  for (j = 0; j < 16; j = j + 1) {
    sprintf(local_58 + local_d0,"%02x",(ulong)local_a8[j]);
    local_d0 = local_d0 + 2;
  }
  for (k = 0; k < 27; k = k + 1) {
    acStack56[k] = *(char *)((long)&local_98 + (long)k);
  }
  acStack56[27] = local_66;
  acStack56[28] = local_5e;
  acStack56[29] = local_5f;
  acStack56[30] = local_78[0];
  acStack56[31] = local_5e;
  acStack56[32] = local_66;
  acStack56[33] = local_6c;
  acStack56[34] = local_5e;
  acStack56[35] = (undefined)local_ba;
  sVar1 = strlen(param_1);
  if (sVar1 == 0x24) {
    for (local_c0 = 0; local_c0 < 0x24; local_c0 = local_c0 + 1) {
      if (param_1[local_c0] != acStack56[local_c0]) {
        uVar2 = 0;
        goto LAB_00101475;
      }
    }
    uVar2 = 1;
  }
  else {
    uVar2 = 0;
  }
LAB_00101475:
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return uVar2;
}
``` 
* 發現 94 行到 110 行做了一連串操作，之後 121 行開始似乎是作比對，再根據結果回傳，猜測是跟 flag 作比較，嘗試動態追蹤 flag。
* 嘗試將 89 行 ~ 93行轉為字元，可以發現 flag 前綴。
```
picoCTF{br1ng_y0ur_0wn_k3y_
```
* 並且根據 121 行可以發現長度應為 0x24=36，將 flag 假設為以下
```
picoCTF{br1ng_y0ur_0wn_k3y_AAAAAAAA}
```
### GDB
```sh
    $ gdb keygenme
```
* 為了找到 flag，則將斷點設在比較之前的 function **strlen**，再用 **continue** 追到比較之前。
```sh
    pwndbg> break strlen
    pwndbg> continue
```
* 或著可以使用 **breakrva** 去追蹤相對位置。
```sh
    pwndbg> breakrva 0x140a
```

* 再去查看 stack ，嘗試找出 flag。
```sh
    pwndbg> x/60s $rsp
```
---
* 可以在追蹤過程中發現比較過程是用 rax 與 rdx 暫存器去作比較，也可以通過紀錄其值再轉為字元，進而找出 flag，但要注意長度必須剛好為 36 才能找出全部。

