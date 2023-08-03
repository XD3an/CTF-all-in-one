# Packets Primer

## Information

### Description

Download the packet capture file and use packet analysis software to find the flag.
Download packet capture

### Hints

1. Wireshark, if you can install and use it, is probably the most beginner friendly packet analysis software product.

## Solution

1. strings
```sh
    $ strings network-dump.flag.pcap
```

2. wireshark
* Follow TCP stream
