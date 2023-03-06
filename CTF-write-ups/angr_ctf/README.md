# angr cheatsheet

### Table of Contents
- [Modules]()
- [Install]()
- [Getting Started]()
- [The Factory]()
- [Loading a Binary]()
- [Solver Engine]()
- [Program States]()
- [Simulation Manager]()
- [Execution Engines]()
- [Analyzes]()
- [More]()
- [Further Reading]()
        
## Modules
- **CLE, The loader**: 將程式載入的載入器。
- **Archinfo, the architecture DB**: 用於獲取程式對應的架構 ( 如 x86, Arm 等)。
- **SimEngine, the simulated executer**: 用於模擬程式分析的模擬器。
- **PyVEX, the lifter**: 用於將程式從機器語言轉換為中間表示碼 Vex，因為無法直接對機器語言進行分析。
- **Claripy, the solver**: 將程式轉換成符號表示式並得出路徑解。
- **SimOS, the rest of the nasty bits**: 用於紀錄程式分析過程中的狀態。

## Install

- [angr Documenattion - installing](https://docs.angr.io/introductory-errata/install)

## Getting Started

- import
    ```py
    import angr #the main framework
    import claripy #the solver engine
    ```

- Load binary
    ```py
    proj = angr.Project('./path/to/binary')
    ```
- Properties
    ```py
    >>> proj.arch
    <Arch AMD64 (LE)>
    >>> proj.entry
    4198480
    >>> hex(proj.entry)
    '0x401050'
    >>> proj.filename
    './test'
    ```

## The Factory

```py
>>> block = proj.factory.block(proj.entry)

>>> block
<Block for 0x401050, 33 bytes>

>>> block.instructions
11

>>> block.instruction_addrs
(4198480, 4198482, 4198485, 4198486, 4198489, 4198493, 4198494, 4198495, 4198498, 4198500, 4198507)

>>> block.pp()
        _start:
401050  xor     ebp, ebp
401052  mov     r9, rdx
401055  pop     rsi
401056  mov     rdx, rsp
401059  and     rsp, 0xfffffffffffffff0
40105d  push    rax
40105e  push    rsp
40105f  xor     r8d, r8d
401062  xor     ecx, ecx
401064  mov     rdi, main
40106b  call    qword ptr [0x403fd8]
```
- 輸出所有 block。
    ```py
    proj = angr.Project('/path/to/binary')
    init_state = proj.factory.entry_state()
    simgr = proj.factory.simgr(init_state)
    while simgr.active:
        print(proj.factory.block(simgr.active[0].addr).pp())
        simgr.step()
    ```

## Loading a Binary
- [angr-Documentation - Loading a Binary](https://docs.angr.io/core-concepts/loading#the-loader)
    - [Loaded Object](https://docs.angr.io/core-concepts/loading#loaded-objects)
    - [Symbols and Relocations](https://docs.angr.io/core-concepts/loading#symbols-and-relocations)
    - [Loading Options](https://docs.angr.io/core-concepts/loading#loading-options)
        - [Backends](https://docs.angr.io/core-concepts/loading#backends)
        - [Symbolic Function Summaries](https://docs.angr.io/core-concepts/loading#symbolic-function-summaries)
```py
>>> proj.loader
<Loaded test, maps [0x400000:0xa07fff]>

>>> proj.loader.shared_objects
OrderedDict([('test', <ELF Object test, maps [0x400000:0x404027]>), ('libc.so.6', <ELF Object libc.so.6, maps [0x500000:0x6e0f4f]>), ('ld-linux-x86-64.so.2', <ELF Object ld-linux-x86-64.so.2, maps [0x700000:0x7332d7]>), ('extern-address space', <ExternObject Object cle##externs, maps [0x800000:0x87ffff]>), ('cle##tls', <ELFTLSObjectV2 Object cle##tls, maps [0x900000:0x91500f]>)])

>>> proj.loader.min_addr
4194304

>>> proj.loader.max_addr
10518527

>>> proj.loader.main_object
<ELF Object test, maps [0x400000:0x404027]>

>>> proj.loader.main_object.execstack
False

>>> proj.loader.main_object.pic
False
```

## Solver Engine

- [angr Documentation - Solver Engine](https://docs.angr.io/core-concepts/solver)
    - [Working with Bitvectors](https://docs.angr.io/core-concepts/solver#working-with-bitvectors)
    - [Symbolic Constraints](https://docs.angr.io/core-concepts/solver#symbolic-constraints)
    - [Constraints Solving](https://docs.angr.io/core-concepts/solver#constraint-solving)
    - [Floating point numbers](https://docs.angr.io/core-concepts/solver#floating-point-numbers)
    - [More Solving Methods](https://docs.angr.io/core-concepts/solver#more-solving-methods)

- 創建 Symbolic 物件 (Bitvectors)。
    ```py
    sym_size = 8
    sym_arg = claripiy.BVS('sym_arg', 8*sym_size)
    ```

- 限制 sym_arg 的 char 範圍。
    ```py
    for byte in sym_arg.chop(8):
        initial_state.add_constraints(byte >= '\x20') # ' '
        initial_state.add_constraints(byte <= '\x7e') # '~'
    ```

- 用 symbolic argument 創建 state。
    ```py
    for byte in sym_arg.chop(8):
        initial_state.add_constraints(byte >= '\x20') # ' '
        initial_state.add_constraints(byte <= '\x7e') # '~'
    ```


## Program States

- [angr Documentation - Program State](https://docs.angr.io/core-concepts/states)
    - [Basic Execution](https://docs.angr.io/core-concepts/states#basic-execution)
    - [State Presents](https://docs.angr.io/core-concepts/states#state-presets)
    - [Low level interface for memory](https://docs.angr.io/core-concepts/states#low-level-interface-for-memory)
    - [State Options](https://docs.angr.io/core-concepts/states#state-options)
    - [State Plugins](https://docs.angr.io/core-concepts/states#state-plugins)
    - [More about I/O: Files, file systems, and network sockets](https://docs.angr.io/core-concepts/states#more-about-i-o-files-file-systems-and-network-sockets)

- entry_state
    - entry point
    ```py
    state = proj.factory.entry_state()
    ```
- blank_state
    - 指定特定記憶體位址，使用 blank_state() 回傳 SimState 物件。
    ```py
    # set start address
    start_address = 0x08048980
    # use blank_state() to create a SimState object
    init_state = proj.factory.blank_state(addr=start_address)
    ```
- [full_init_state](https://api.angr.io/angr.html#angr.factory.AngrObjectFactory.full_init_state)

- [call_state](https://api.angr.io/angr.html#angr.factory.AngrObjectFactory.call_state)
    - 回傳指定 function 的 SimState 物件。



## Simulation Manager

- [angr Documentation - Simulation Manager](https://docs.angr.io/core-concepts/pathgroups)
    - [Stepping](https://docs.angr.io/core-concepts/pathgroups#stepping)
    - [Stash Management](https://docs.angr.io/core-concepts/pathgroups#stash-management)
    - [Stash types](https://docs.angr.io/core-concepts/pathgroups#stash-types)
    - [Simple Exploration](https://docs.angr.io/core-concepts/pathgroups#simple-exploration)
    - [Exploration Techniques](https://docs.angr.io/core-concepts/pathgroups#exploration-techniques)

- Simulation Manager 
    ```py
    simgr = proj.factory.simulation_manager(state)
    simgr = proj.factory.simgr(state)
    ```   

### Stepping

- [step](https://api.angr.io/angr.html#angr.sim_state.SimState.step): 使用 Symbolic Execution 執行一個 basic block。

### Explore

- 選擇其他 exploring startegy。
    - [Exploration Technique](https://api.angr.io/angr.html#angr.exploration_techniques.ExplorationTechnique)
    ```py
    simgr.use_technique(angr.exploration_techniques.DFS())
    ```
- Explore
    ```py
    simgr.explore(find=find_condition, avoid=avoid_condition)
    ```
- After Explore
    ```py
    found = simgr.found[0] # A state that reached the find condition from explore
    found.solver.eval(sym_arg, cast_to=bytes) # Return a concrete string value for the sym arg to reach this state
    ```
- Symbolica Execute 直到 lambe expression 成立為 `True`。
    ```py
    simgr.step(until=lambda sm: sm.active[0].addr >= first_jmp)
    ```
### Manually Exploring

- [ref](https://github.com/angr/angr-doc/blob/master/CHEATSHEET.md#manually-exploring)

## Execution Engines

- [angr Documentations - Executation Engines](https://docs.angr.io/core-concepts/simulation)
    - [SimSuccessors](https://docs.angr.io/core-concepts/simulation#simsuccessors)
    - [Breakpoints](https://docs.angr.io/core-concepts/simulation#breakpoints)

## Analyzes

- [angr Documentations - Analyzes](https://docs.angr.io/core-concepts/analyses)
    - [Built-in Analyses](https://docs.angr.io/core-concepts/analyses#built-in-analyses)
    - [Resilience](https://docs.angr.io/core-concepts/analyses#resilience)

- [CFG](https://docs.angr.io/built-in-analyses/cfg): Control-Flow Graph

## More

### SimProcedures

- 用於將自訂義編寫的函數取代原來的函數。
    ```py
    >>> project = Project('examples/fauxware/fauxware')

    >>> class BugFree(SimProcedure):
        def run(self, argc, argv):
            print('Program running with argc=%s and argv=%s' % (argc, argv))
            return 0
    # this assumes we have symbols for the binary
    >>> project.hook_symbol('main', BugFree())
    ```

### Bitvectors

- [BVS](https://api.angr.io/claripy.html#claripy.ast.bv.BVS): Creates a bit-vector symbol (i.e., a variable).

- [BVV](https://api.angr.io/claripy.html#claripy.ast.bv.BVV): Creates a bit-vector value (i.e., a concrete value).

### Hooking

- 用 angr 已經包好的 Symbol。
    ```py
    proj = angr.Project('/path/to/binary', use_sim_procedures=True)
    proj.hook(addr, angr.SIM_PROCEDURES['libc']['atoi']())
    ```

- 使用 SimProcedure。
    ```py
    class fixpid(angr.SimProcedure)。。
    def run(self):
            return 0x30

    proj.hook(0x4008cd, fixpid())
    ```
### Capstone

- angr 的反組譯器， 負責轉換為組合語言（CapstonenInsn），之後會將組合語言轉換為 basic block （CapstoneBlock）。

- CapstoneBlock: 用於表示一個 basic block，內容包含記憶體位址、CPU指令、CPU架構等。
    ```py
    proj = angr.Project('/path/to/binary')
    bb = proj.factory.block(proj.entry)
    print(angr.block.CapstoneBlock)

    # addrss
    print(hex(bb.capstone.addr))

    # arch
    print(bb.capstone.arch)

    # bytes
    print(bb.bytes)

    # the number of instructions
    print(bb.instructions)

    # list each instruction of the basic block
    print(bb.capstone.insns)
    
    # pretty print
    print(bb.capstone.pp())
    ```
- CapstoneInsn: CPU指令。
    ```py
    # list each instruction of the basic block
    print(bb.capstone.insns)

    # pretty print
    print(bb.capstone.pp())

    # insns address
    print(bb.capstone.insns[0].address)

    # mnemonic
    print(bb.capstone.insns[0].mnemonic)

    # operands
    print(bb.capstone.insns[0].op_str)
    ```

## Further Reading

- [angr Documentation](https://docs.angr.io/)
- [angr API documentation](https://api.angr.io/index.html)
- [angr-doc-CHEATSHEET.md](https://github.com/angr/angr-doc/blob/master/CHEATSHEET.md)
