# 12_angr_veritesting

## Information

- [src](https://github.com/jakespringer/angr_ctf)


## Solution

### 觀察程式相關資訊

### 分析

- 注意 Path Explode 問題。

- 這裡使用 **veritesting** 技術，來解決路徑爆炸(Path Explode) 的問題。
    - [Enhancing symbolic execution with veritesting
](https://dl.acm.org/doi/10.1145/2568225.2568293)

### angr

- simgr(veritesting)
    ```py
    # create a simulation manager (with veritesting)
    simgr = proj.factory.simgr(init_state, veritesting=True)
    ```

### solve.py
```py
import angr
import claripy
import sys

def find_condition(state):
    stdout_output = state.posix.dumps(sys.stdout.fileno())
    return b'Good Job.' in stdout_output

def avoid_condition(state):
    stdout_output = state.posix.dumps(sys.stdout.fileno())
    return b'Try Again.' in stdout_output

def main():
    # load binary
    proj = angr.Project('./12_angr_veritesting')
    
    # create a SimState object (entry point)
    init_state = proj.factory.entry_state()

    # create a simulation manager (with veritesting)
    simgr = proj.factory.simgr(init_state, veritesting=True)

    # explore
    simgr.explore(find=find_condition, avoid=avoid_condition)

    # output result
    if simgr.found:
        solution = simgr.found[0]
        flag = solution.posix.dumps(sys.stdin.fileno())
        print(flag)
    else:
        print('no result')

if __name__=='__main__':
    main()
```