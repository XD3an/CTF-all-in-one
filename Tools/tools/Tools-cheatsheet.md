# Tools-cheatsheet

## Binary

- [IDA Pro](https://hex-rays.com/ida-pro/): A powerful disassembler and a versatile debugger.
    - [IDAPro cheatsheet](https://www.hex-rays.com/products/ida/support/freefiles/IDA_Pro_Shortcuts.pdf)
    - [idaplugins-list](https://github.com/onethawt/idaplugins-list)

- [Ghidra](https://github.com/NationalSecurityAgency/ghidra): Ghidra is a software reverse engineering (SRE) framework.
    - [Ghidra Cheat Sheet](https://ghidra-sre.org/CheatSheet.html)

- [radare](https://rada.re/n/): Libre and Portable Reverse Engineering Framework.

- [GDB](https://www.sourceware.org/gdb/): The GNU Project Debugger.
    - [gef](https://github.com/hugsy/gef)
    - [pwndbg](https://github.com/pwndbg/pwndbg)
    - [peda](https://github.com/longld/peda)
    - [Pwngdb](https://github.com/scwuaptx/Pwngdb)

- [x32/x64dbg](https://x64dbg.com/#): An open-source x64/x32 debugger for windows.
    - [x64dbg plugins](https://github.com/x64dbg/x64dbg/wiki/Plugins)

- [checksec](https://github.com/slimm609/checksec.sh): Checksec is a bash script to check the properties of executables (like PIE, RELRO, Canaries, ASLR, Fortify Source).

- [ROPgadget](https://github.com/JonathanSalwan/ROPgadget): lets you search your gadgets on your binaries to facilitate your ROP exploitation.

- [one_gadget](https://github.com/david942j/one_gadget): The best tool for finding one gadget RCE in libc.so.6.

- [pwntools](https://github.com/Gallopsled/pwntools): CTF framework and exploit development library.

- [PE bear](https://github.com/hasherezade/pe-bear): Portable Executable reversing tool with a friendly GUI.

- [Detect-It-Easy](https://github.com/horsicq/Detect-It-Easy): Program for determining types of files for Windows, Linux and MacOS.

- [Exeinfo](https://exeinfo-pe.en.uptodown.com/windows): is a program that lets you verify .exe files and check out all their properties.

- [Compiler Explorer](https://godbolt.org/): online compiler.

- [Apktool](https://ibotpeaches.github.io/Apktool/): A tool for reverse engineering Android apk files.

- [jadx](https://github.com/skylot/jadx): Dex to Java decompiler.

### Symbolic Execution

- [angr](https://github.com/angr/angr): A powerful and user-friendly binary analysis platform!

## Crypto

- [CyberChef](https://gchq.github.io/CyberChef/): cyber chef.

- [dCode](https://www.dcode.fr/en): is the universal site for decipher coded messages, cheating on letter games, solving puzzles, geocaches and treasure hunts, etc.

- [Vigenere Solver](https://www.guballa.de/vigenere-solver): This online tool breaks Vigenère ciphers without knowing the key. 

- [Morse Code Translator](https://morsecode.world/international/translator.html)

- [gmpy2](https://pypi.org/project/gmpy2/): is an optimized, C-coded Python extension module that supports fast multiple-precision arithmetic.

- [RSACtfTool](https://github.com/RsaCtfTool/RsaCtfTool): RSA attack tool (mainly for ctf) - retreive private key from weak public key and/or uncipher data.

- [hash-identifier](https://www.kali.org/tools/hash-identifier/): Software to identify the different types of hashes used to encrypt data and especially passwords.

## Web

- [BurpSuite](https://portswigger.net/burp): tool for web security testing.

## Penetration Testing

- [Metasploit](https://www.metasploit.com/): Metasploit Framework.

- [Hack-Tools](https://github.com/LasCC/Hack-Tools#install-the-extension): The all-in-one Red Team extension for Web Pentester.

## Network

- [Nmap](https://nmap.org/): A free and open source utility used by millions of people for network discovery, administration, and security auditing.

- [wireshark](https://www.wireshark.org/): network protocol analyzer.

## Forensic

- [AccessData FTK](https://www.pluralsight.com/paths/accessdata-forensic-toolkit-ftk?exp=1): It is a court-accepted, digital investigations software that includes many features and capabilities such as full-disk forensic images, decrypt files and crack passwords, parse registry files, collect, process and analyze datasets, and advanced volatile memory analysis. 

## Steganography

- [binwalk](https://github.com/ReFirmLabs/binwalk): Firmware Analysis Tool.

- [exiftool](https://github.com/exiftool/exiftool): ExifTool meta information reader/writer

- [zsteg](https://github.com/zed-0xff/zsteg): detect stegano-hidden data in PNG & BMP.

- [stegsolve](https://github.com/zardus/ctf-tools/blob/master/stegsolve/install): is a stegano solver for challenges.

- [steghide](https://steghide.sourceforge.net/): is a steganography program that is able to hide data in various kinds of image- and audio-files. The color- respectivly sample-frequencies are not changed thus making the embedding resistant against first-order statistical tests.

- [HxD](https://mh-nexus.de/en/hxd/): is a carefully designed and fast hex editor which, additionally to raw disk editing and modifying of main memory (RAM), handles files of any size.

## Linux commands

- [objdump](https://man7.org/linux/man-pages/man1/objdump.1.html): display information from object files.

- [readelf](https://man7.org/linux/man-pages/man1/readelf.1.html): display information about ELF files.

- [ldd](https://man7.org/linux/man-pages/man1/ldd.1.html): print shared object dependencies.

- [strace](https://man7.org/linux/man-pages/man1/strace.1.html): trace system calls and signals.

- [ltrace](https://man7.org/linux/man-pages/man1/ltrace.1.html): A library call tracer.

- [xxd](https://www.tutorialspoint.com/unix_commands/xxd.htm): make a hexdump or do the reverse.

- [strings](https://man7.org/linux/man-pages/man1/strings.1.html): print the sequences of printable characters in files.

- [strip](https://man7.org/linux/man-pages/man1/strip.1.html): discard symbols and other data from object files.
    - `gcc -s`

## Online Resources

- [c9x.me](https://c9x.me/x86/): x86 Instruction Set Reference.

- [glibc-all-in-one](https://github.com/matrix1001/glibc-all-in-one): A convenient glibc binary and debug file downloader and source code auto builder.

- [Glibc source code](https://elixir.bootlin.com/glibc/glibc-2.31/source): Glibc source code.

## Script Languages

### Bash

- [awesome-cheatsheets/bash.sh](https://github.com/LeCoupa/awesome-cheatsheets/blob/master/languages/bash.sh): A bash cheatsheet.

### Python

- [awesome-cheatsheets/python](https://github.com/LeCoupa/awesome-cheatsheets/blob/master/languages/python.md): A simple python cheatsheet.

- [python-cheatsheet](https://github.com/gto76/python-cheatsheet): A Comprehensive Python Cheatsheet.

- [awesome-python](https://github.com/vinta/awesome-python): A curated list of awesome Python frameworks, libraries, software and resources.

## Others

- [gitleaks](https://github.com/gitleaks/gitleaks): Gitleaks is a SAST tool for detecting and preventing hardcoded secrets like passwords, api keys, and tokens in git repos. 
