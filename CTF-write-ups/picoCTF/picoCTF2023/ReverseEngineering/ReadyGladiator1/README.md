# Ready Gladiator 1

## Information

### Description

Can you make a CoreWars warrior that wins?
Additional details will be available after launching your challenge instance.

### Hints

1. You may be able to find a viable warrior in beginner docs

## Solution

### CoreWar

- [CoreWar](https://zh.wikipedia.org/zh-tw/%E6%A0%B8%E5%BF%83%E5%A4%A7%E6%88%98#:~:text=%E3%80%8A%E6%A0%B8%E5%BF%83%E5%A4%A7%E6%88%B0%E3%80%8B%EF%BC%88%E8%8B%B1%E8%AA%9E%EF%BC%9A,%E6%8A%BD%E8%B1%A1%E7%B5%84%E5%90%88%E8%AA%9E%E8%A8%80%E7%B7%A8%E5%AF%AB%E7%9A%84%E3%80%82)：是一款在 1984 年被創造的程式設計遊戲，在遊戲中會有兩個以上的戰鬥程式(戰士)為了控制虛擬電腦而競爭，這些戰鬥程式是用一種叫作 Redcode 的抽象組合語言編寫。
    - 遊戲設定：在遊戲開始時，每個戰鬥程式都被隨機加載到記憶體中，然後每個程式依次執行一條指令。這個遊戲的目標是使對立程式的進程終止（如果它們執行了無效的指令，就會發生這種情況），讓獲勝的程式獨占機器。

- [CoreWar onlnie](https://crypto.stanford.edu/~blynn/play/redcode.html)


### flag

- 目標是只要勝利至少一次即可。

- imp.red
    ```
    ;redcode
    name Imp Ex
    ;assert 1
    jmp 0 , < -2
    end
    ```