# angr-cheatsheet

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
    >> import angr #the main framework
    >> import claripy #the solver engine
    ```

- Load binary
    ```py
    # load a binary
    >> proj = angr.Project('./path/to/binary')
    ```
- Properties
    ```py
    # return the arch of proj
    >>> proj.arch
    <Arch X86 (LE)>
    
    # return the entry point  
    >>> proj.entry
    134513744
    >>> hex(proj.entry)
    '0x8048450'
    
    # return filename
    >>> proj.filename
    './test'
    ```

- The Loader
    ```py
    # maps
    >>> proj.loader
    <Loaded true, maps [0x400000:0x5004000]>
    ```

- The Factory: 將物件實例化。
    - Blocks    
        ````py
        # is used to extract a basic block of code from a given address
        >>> block = proj.factory.block(proj.entry)
        
        # block type
        >>> block
        <Block for 0x8048450, 33 bytes>
        
        # the address of all instructions from a basic block
        >>> block.instruction_addrs
        (134513744, 134513746, 134513747, 134513749, 134513752, 134513753, 134513754, 134513755, 134513760, 134513765, 134513766, 134513767, 134513772)
        
        # perfect print 
        >>> block.pp()
                _start:
        8048450  xor     ebp, ebp
        8048452  pop     esi
        8048453  mov     ecx, esp
        8048455  and     esp, 0xfffffff0
        8048458  push    eax
        8048459  push    esp
        804845a  push    edx
        804845b  push    __libc_csu_fini
        8048460  push    __libc_csu_init
        8048465  push    ecx
        8048466  push    esi
        8048467  push    main
        804846c  call    __libc_start_main
        ```
    - 輸出所有 block。
        ```py
        proj = angr.Project('/path/to/binary')
        init_state = proj.factory.entry_state()
        simgr = proj.factory.simgr(init_state)
        while simgr.active:
            print(proj.factory.block(simgr.active[0].addr).pp())
            simgr.step()
        ````
    - States
        ```py
        # create a SimState object from a given address (entry point)
        >>> state = proj.factory.entry_state()
        <SimState @ 0x401670>

        # get the current instruction pointer
        >>> state.regs.rip        
        <BV64 0x401670>
        >>> state.regs.rax
        <BV64 0x1c>

        # interpret the memory at the entry point as a C int
        >>> state.mem[proj.entry].int.resolved  
        <BV32 0x8949ed31>
        ```
    - Simulation Managers 
        ```py
        # create a simulation manager
        >>> simgr = proj.factory.simulation_manager(state)
        <SimulationManager with 1 active>
        
        # active state
        >>> simgr.active
        [<SimState @ 0x401670>]
        
        # step a basic block
        >>> simgr.step()
        ```

## Loading a Binary
- [angr-Documentation - Loading a Binary](https://docs.angr.io/core-concepts/loading#the-loader)
    - [Loaded Object](https://docs.angr.io/core-concepts/loading#loaded-objects)
    - [Symbols and Relocations](https://docs.angr.io/core-concepts/loading#symbols-and-relocations)
    - [Loading Options](https://docs.angr.io/core-concepts/loading#loading-options)
        - [Backends](https://docs.angr.io/core-concepts/loading#backends)
        - [Symbolic Function Summaries](https://docs.angr.io/core-concepts/loading#symbolic-function-summaries)
- 載入執行檔。
    ```py
    >>> proj.loader
    <Loaded 00_angr_find, maps [0x8048000:0x8707fff]>

    >>> proj.loader.min_addr
    134512640
    
    >>> proj.loader.max_addr
    141590527

    >>> proj.loader.main_object
    <ELF Object 00_angr_find, maps [0x8048000:0x804a03f]>

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
    >> sym_size = 8
    >> sym_arg = claripiy.BVS('sym_arg', 8*sym_size)
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
        >> state = proj.factory.entry_state()
        ```
- blank_state
    - 指定特定記憶體位址，使用 blank_state() 回傳 SimState 物件。
        ```py
        # set start address
        >> start_address = 0x08048980
        # use blank_state() to create a SimState object
        >> init_state = proj.factory.blank_state(addr=start_address)
        ```
- [full_init_state](https://api.angr.io/angr.html#angr.factory.AngrObjectFactory.full_init_state): 創建一個完整的 SimState 物件，包含其中所有的狀態。

- [call_state](https://api.angr.io/angr.html#angr.factory.AngrObjectFactory.call_state): 回傳指定 function 的 SimState 物件。


## Simulation Manager

- [angr Documentation - Simulation Manager](https://docs.angr.io/core-concepts/pathgroups)
    - [Stepping](https://docs.angr.io/core-concepts/pathgroups#stepping)
    - [Stash Management](https://docs.angr.io/core-concepts/pathgroups#stash-management)
    - [Stash types](https://docs.angr.io/core-concepts/pathgroups#stash-types)
    - [Simple Exploration](https://docs.angr.io/core-concepts/pathgroups#simple-exploration)
    - [Exploration Techniques](https://docs.angr.io/core-concepts/pathgroups#exploration-techniques)

- Simulation Manager 
    ```py
    >> simgr = proj.factory.simulation_manager(state)
    >> simgr = proj.factory.simgr(state)
    ```   

### Stepping

- [step](https://api.angr.io/angr.html#angr.sim_state.SimState.step): 使用 Symbolic Execution 執行一個 [basic block](https://en.wikipedia.org/wiki/Basic_block)。

### Explore

- 選擇其他 exploring startegy。
    - [Exploration Technique](https://api.angr.io/angr.html#angr.exploration_techniques.ExplorationTechnique)
    ```py
    >> simgr.use_technique(angr.exploration_techniques.DFS())
    ```
- Explore
    ```py
    >> simgr.explore(find=find_condition, avoid=avoid_condition)
    ```
- After Explore
    ```py
    >> found = simgr.found[0] # A state that reached the find condition from explore
    >> found.solver.eval(sym_arg, cast_to=bytes) # Return a concrete string value for the sym arg to reach this state
    ```
- Symbolica Execute 直到 lambe expression 成立為 `True`。
    ```py
    >> simgr.step(until=lambda sm: sm.active[0].addr >= first_jmp)
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
    >> proj = angr.Project('/path/to/binary', use_sim_procedures=True)
    >> proj.hook(addr, angr.SIM_PROCEDURES['libc']['atoi']())
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
    >> proj = angr.Project('/path/to/binary')
    >> bb = proj.factory.block(proj.entry)
    >> print(angr.block.CapstoneBlock)

    # addrss
    >>> print(hex(bb.capstone.addr))
    0x8048450
    
    # arch
    >> print(bb.capstone.arch)
    <Arch X86 (LE)>
    
    # bytes
    >> print(bb.bytes)
    b'1\xed^\x89\xe1\x83\xe4\xf0PTRh\x10\x87\x04\x08h\xb0\x86\x04\x08QVh\xc7\x85\x04\x08\xe8\xaf\xff\xff\xff'

    # the number of instructions
    >> print(bb.instructions)
    13

    # list each instruction of the basic block
    >> print(bb.capstone.insns)
    [<DisassemblerInsn "xor" for 0x8048450>, <DisassemblerInsn "pop" for 0x8048452>, <DisassemblerInsn "mov" for 0x8048453>, <DisassemblerInsn "and" for 0x8048455>, <DisassemblerInsn "push" for 0x8048458>, <DisassemblerInsn "push" for 0x8048459>, <DisassemblerInsn "push" for 0x804845a>, <DisassemblerInsn "push" for 0x804845b>, <DisassemblerInsn "push" for 0x8048460>, <DisassemblerInsn "push" for 0x8048465>, <DisassemblerInsn "push" for 0x8048466>, <DisassemblerInsn "push" for 0x8048467>, <DisassemblerInsn "call" for 0x804846c>]

    # pretty print
    >> print(bb.capstone.pp())
    0x8048450:      xor     ebp, ebp
    0x8048452:      pop     esi
    0x8048453:      mov     ecx, esp
    0x8048455:      and     esp, 0xfffffff0
    0x8048458:      push    eax
    0x8048459:      push    esp
    0x804845a:      push    edx
    0x804845b:      push    0x8048710
    0x8048460:      push    0x80486b0
    0x8048465:      push    ecx
    0x8048466:      push    esi
    0x8048467:      push    0x80485c7
    0x804846c:      call    0x8048420
    ```
- CapstoneInsn: CPU指令。
    ```py
    # insns address
    >> print(hex(bb.capstone.insns[0].address))
    '0x8048450'

    # mnemonic
    >> print(bb.capstone.insns[0].mnemonic)
    'xor'

    # operands
    >> print(bb.capstone.insns[0].op_str)
    'ebp, ebp'
    ```

## Further Reading

- [angr Documentation](https://docs.angr.io/)
- [angr API documentation](https://api.angr.io/index.html)
- [angr-doc-CHEATSHEET.md](https://github.com/angr/angr-doc/blob/master/CHEATSHEET.md)
