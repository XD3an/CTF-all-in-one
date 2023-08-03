# Let's get dynamic

## Challenge

### Description
Can you tell what this file is reading? [chall.S](https://mercury.picoctf.net/static/0ae77c18ca85211e6439e5e710657a54/chall.S)

### Hints
1. Running this in a debugger would be helpful

## Solution
* Decompiler (Ghidra)
    ```c
    bool main(void) {
        int iVar1;
        size_t sVar2;
        long in_FS_OFFSET;
        int local_11c;
        byte local_118 [64];
        char local_d8 [64];
        undefined8 local_98;
        undefined8 local_90;
        undefined8 local_88;
        undefined8 local_80;
        undefined8 local_78;
        undefined8 local_70;
        undefined2 local_68;
        undefined8 local_58;
        undefined8 local_50;
        undefined8 local_48;
        undefined8 local_40;
        undefined8 local_38;
        undefined8 local_30;
        undefined2 local_28;
        long local_20;
        
        local_20 = *(long *)(in_FS_OFFSET + 0x28);
        local_98 = 0x9ca22a2c6e25f4bb;
        local_90 = 0xf48a0773939cacbd;
        local_88 = 0xaea4d74d7bf0305;
        local_80 = 0x1af35b3168a434ab;
        local_78 = 0x2eb55ce116f3170f;
        local_70 = 0xb398b1ef10a7b466;
        local_68 = 0x47;
        local_58 = 0xf3f1687811578fd8;
        local_50 = 0xb7f42801bfebcfc2;
        local_48 = 0x519c7a0abb8a6f32;
        local_40 = 0x64cd254b55f24d91;
        local_38 = 0x45ec1fb015b15063;
        local_30 = 0xbb90ede51bfbb868;
        local_28 = 0x19;
        fgets(local_d8,0x31,stdin);
        local_11c = 0;
        while( true ) {
            sVar2 = strlen((char *)&local_98);
            if (sVar2 <= (ulong)(long)local_11c) break;
            local_118[local_11c] =
                (byte)local_11c ^
                *(byte *)((long)&local_98 + (long)local_11c) ^ *(byte *)((long)&local_58 + (long)local_11 c)
                ^ 0x13;
            local_11c = local_11c + 1;
        }
        iVar1 = memcmp(local_d8,local_118,0x31);
        if (iVar1 == 0) {
            puts("No, that\'s not right.");
        }
        else {
            puts("Correct! You entered the flag.");
        }
        if (local_20 != *(long *)(in_FS_OFFSET + 0x28)) {
                            /* WARNING: Subroutine does not return */
            __stack_chk_fail();
        }
        return iVar1 == 0;
    }
    ```
### Debugging with gdb
可以根據上面分析的結果發現程式中有儲存一段字串組合，程式會對其進行特殊處理後再與使用者的輸入比較，再對結果進行輸出。
綜上分析，可以得知此字串可能有著特殊意義，可以嘗試找出來。
* 嘗試利用 gdb 去 try 看看過程。
    ```sh
        gef➤  b main
        Breakpoint 1 at 0x117d
        gef➤  r
        gef➤  disassemble main
        Dump of assembler code for function main:
        0x0000555555555179 <+0>:     push   rbp
        0x000055555555517a <+1>:     mov    rbp,rsp
        => 0x000055555555517d <+4>:     push   rbx
        0x000055555555517e <+5>:     sub    rsp,0x128
        0x0000555555555185 <+12>:    mov    DWORD PTR [rbp-0x124],edi
        0x000055555555518b <+18>:    mov    QWORD PTR [rbp-0x130],rsi
        0x0000555555555192 <+25>:    mov    rax,QWORD PTR fs:0x28
        0x000055555555519b <+34>:    mov    QWORD PTR [rbp-0x18],rax
        0x000055555555519f <+38>:    xor    eax,eax
        0x00005555555551a1 <+40>:    movabs rax,0x9ca22a2c6e25f4bb
        0x00005555555551ab <+50>:    movabs rdx,0xf48a0773939cacbd
        0x00005555555551b5 <+60>:    mov    QWORD PTR [rbp-0x90],rax
        0x00005555555551bc <+67>:    mov    QWORD PTR [rbp-0x88],rdx
        0x00005555555551c3 <+74>:    movabs rax,0xaea4d74d7bf0305
        0x00005555555551cd <+84>:    movabs rdx,0x1af35b3168a434ab
        0x00005555555551d7 <+94>:    mov    QWORD PTR [rbp-0x80],rax
        0x00005555555551db <+98>:    mov    QWORD PTR [rbp-0x78],rdx
        0x00005555555551df <+102>:   movabs rax,0x2eb55ce116f3170f
        0x00005555555551e9 <+112>:   movabs rdx,0xb398b1ef10a7b466
        0x00005555555551f3 <+122>:   mov    QWORD PTR [rbp-0x70],rax
        0x00005555555551f7 <+126>:   mov    QWORD PTR [rbp-0x68],rdx
        0x00005555555551fb <+130>:   mov    WORD PTR [rbp-0x60],0x47
        0x0000555555555201 <+136>:   movabs rax,0xf3f1687811578fd8
        0x000055555555520b <+146>:   movabs rdx,0xb7f42801bfebcfc2
        0x0000555555555215 <+156>:   mov    QWORD PTR [rbp-0x50],rax
        0x0000555555555219 <+160>:   mov    QWORD PTR [rbp-0x48],rdx
        0x000055555555521d <+164>:   movabs rax,0x519c7a0abb8a6f32
        0x0000555555555227 <+174>:   movabs rdx,0x64cd254b55f24d91
        0x0000555555555231 <+184>:   mov    QWORD PTR [rbp-0x40],rax
        0x0000555555555235 <+188>:   mov    QWORD PTR [rbp-0x38],rdx
        0x0000555555555239 <+192>:   movabs rax,0x45ec1fb015b15063
        0x0000555555555243 <+202>:   movabs rdx,0xbb90ede51bfbb868
        0x000055555555524d <+212>:   mov    QWORD PTR [rbp-0x30],rax
        0x0000555555555251 <+216>:   mov    QWORD PTR [rbp-0x28],rdx
        0x0000555555555255 <+220>:   mov    WORD PTR [rbp-0x20],0x19
        0x000055555555525b <+226>:   mov    rdx,QWORD PTR [rip+0x2dde]        # 0x555555558040 <stdin@GLIBC_2.2.5>
        0x0000555555555262 <+233>:   lea    rax,[rbp-0xd0]
        0x0000555555555269 <+240>:   mov    esi,0x31
        0x000055555555526e <+245>:   mov    rdi,rax
        0x0000555555555271 <+248>:   call   0x555555555070 <fgets@plt>
        0x0000555555555276 <+253>:   mov    DWORD PTR [rbp-0x114],0x0
        0x0000555555555280 <+263>:   jmp    0x5555555552c4 <main+331>
        0x0000555555555282 <+265>:   mov    eax,DWORD PTR [rbp-0x114]
        0x0000555555555288 <+271>:   cdqe
        0x000055555555528a <+273>:   movzx  edx,BYTE PTR [rbp+rax*1-0x90]
        0x0000555555555292 <+281>:   mov    eax,DWORD PTR [rbp-0x114]
        0x0000555555555298 <+287>:   cdqe
        0x000055555555529a <+289>:   movzx  eax,BYTE PTR [rbp+rax*1-0x50]
        0x000055555555529f <+294>:   xor    edx,eax
        0x00005555555552a1 <+296>:   mov    eax,DWORD PTR [rbp-0x114]
        0x00005555555552a7 <+302>:   xor    eax,edx
        0x00005555555552a9 <+304>:   xor    eax,0x13
        0x00005555555552ac <+307>:   mov    edx,eax
        0x00005555555552ae <+309>:   mov    eax,DWORD PTR [rbp-0x114]
        0x00005555555552b4 <+315>:   cdqe
        0x00005555555552b6 <+317>:   mov    BYTE PTR [rbp+rax*1-0x110],dl
        0x00005555555552bd <+324>:   add    DWORD PTR [rbp-0x114],0x1
        0x00005555555552c4 <+331>:   mov    eax,DWORD PTR [rbp-0x114]
        0x00005555555552ca <+337>:   movsxd rbx,eax
        0x00005555555552cd <+340>:   lea    rax,[rbp-0x90]
        0x00005555555552d4 <+347>:   mov    rdi,rax
        0x00005555555552d7 <+350>:   call   0x555555555040 <strlen@plt>
        0x00005555555552dc <+355>:   cmp    rbx,rax
        0x00005555555552df <+358>:   jb     0x555555555282 <main+265>
        0x00005555555552e1 <+360>:   lea    rcx,[rbp-0x110]
        0x00005555555552e8 <+367>:   lea    rax,[rbp-0xd0]
        0x00005555555552ef <+374>:   mov    edx,0x31
        0x00005555555552f4 <+379>:   mov    rsi,rcx
        0x00005555555552f7 <+382>:   mov    rdi,rax
        0x00005555555552fa <+385>:   call   0x555555555060 <memcmp@plt>
        0x00005555555552ff <+390>:   test   eax,eax
        0x0000555555555301 <+392>:   je     0x555555555316 <main+413>
        0x0000555555555303 <+394>:   lea    rdi,[rip+0xcfe]        # 0x555555556008
        0x000055555555530a <+401>:   call   0x555555555030 <puts@plt>
        0x000055555555530f <+406>:   mov    eax,0x0
        0x0000555555555314 <+411>:   jmp    0x555555555327 <main+430>
        0x0000555555555316 <+413>:   lea    rdi,[rip+0xd0a]        # 0x555555556027
        0x000055555555531d <+420>:   call   0x555555555030 <puts@plt>
        0x0000555555555322 <+425>:   mov    eax,0x1
        0x0000555555555327 <+430>:   mov    rcx,QWORD PTR [rbp-0x18]
        0x000055555555532b <+434>:   xor    rcx,QWORD PTR fs:0x28
        0x0000555555555334 <+443>:   je     0x55555555533b <main+450>
        0x0000555555555336 <+445>:   call   0x555555555050 <__stack_chk_fail@plt>
        0x000055555555533b <+450>:   add    rsp,0x128
        0x0000555555555342 <+457>:   pop    rbx
        0x0000555555555343 <+458>:   pop    rbp
        0x0000555555555344 <+459>:   ret
        End of assembler dump.
        gef➤  b *0x00005555555552fa
        Breakpoint 2 at 0x5555555552fa
        gef➤  x/gs $rcx
        warning: Unable to display strings with size 'g', using 'b' instead.
        0x7fffffffdf00: "picoCTF{dyn4m1c_4n4ly1s_1s_5up3r_us3ful_56e35b54}\337\377\377\377\177"
    ```
可以發現處理後的字串就是我們要的 flag。