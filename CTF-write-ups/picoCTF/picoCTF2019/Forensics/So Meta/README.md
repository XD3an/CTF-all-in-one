# So Meta

## Information

### Description

Find the flag in this picture.

### Hints

1. What does meta mean in the context of files?

2. Ever heard of metadata?

## Solution

- [exiftool](https://github.com/exiftool/exiftool): ExifTool meta information reader/writer

- 透過 exiftool 檢查 meta data。
    ```
     exiftool pico_img.png 
    ```