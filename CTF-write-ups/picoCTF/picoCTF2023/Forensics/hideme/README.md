# hideme

## Information

### Description

Every file gets a flag.
The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye here.

### Hints

(None)

## Solution

- binwalk 進行分析，但因為其中含有 zip 檔，所以需要加 `-e` 進行自動解壓縮。
    ```sh
    $ binwalk -e flag.png
    ```