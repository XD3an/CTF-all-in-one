# 16_angr_arbitrary_write

## Information

- [src](https://github.com/jakespringer/angr_ctf)

## Solution

### solve.py
```py
import angr
import claripy
import sys

# check strmcpy
def check_strncpy(state):
    # get parameter
    strncpy_dest_parameter = state.memory.load(state.regs.esp+4, 4, endness=state.arch.memory_endness)
    strncpy_src_parameter = state.memory.load(state.regs.esp+8, 4, endness=state.arch.memory_endness)
    strncpy_len_parameter = state.memory.load(state.regs.esp+12, 4, endness=state.arch.memory_endness)
    
    # get contents
    src_contents = state.memory.load(strncpy_src_parameter, strncpy_len_parameter)
    #print(strncpy_dest_parameter, strncpy_src_parameter, strncpy_len_parameter, src_contents)
    #print(state.solver.symbolic(strncpy_dest_parameter), state.solver.symbolic(strncpy_src_parameter))

    # check if dest parameter and  src parameter are symbolic
    if state.solver.symbolic(strncpy_dest_parameter) and state.solver.symbolic(src_contents):
        password_string =  'NDYNWEUJ'
        buffer_address = 0x57584344
        
        src_hold_password = src_contents[-1:-64] == password_string
        dest_equal_buffer = strncpy_dest_parameter == buffer_address

        if state.satisfiable(extra_constraints=(src_hold_password, dest_equal_buffer)):
            state.add_constraints(src_hold_password, dest_equal_buffer) 
            return True
    return False
    
def find_condition(state):
    strncpy_addr = 0x08048410
    if state.addr == strncpy_addr:
        return check_strncpy(state)
    else:
        return False

def main():
    # load binary
    proj = angr.Project('./16_angr_arbitrary_write')
    
    # create a SimState object (entry point)
    init_state = proj.factory.entry_state()

    # create a SimProcedure for scanf
    class ReplaceScanf(angr.SimProcedure):
        def run(self, format, check_key_address, input_buffer_address):
            scanf0 = claripy.BVS('scanf0', 4*8)
            scanf1 = claripy.BVS('scanf1', 20*8)

            for char in scanf1.chop(bits=8):
                self.state.add_constraints(char >= '0', char <='z')
 
            self.state.memory.store(check_key_address, scanf0, endness=proj.arch.memory_endness)
            self.state.memory.store(input_buffer_address, scanf1)
 
            self.state.globals['solution0'] = scanf0
            self.state.globals['solution1'] = scanf1
    
    # set hook
    scanf_symbol = '__isoc99_scanf'
    proj.hook_symbol(scanf_symbol, ReplaceScanf())

    # create a simulation manager
    simgr = proj.factory.simgr(init_state)

    # explore
    simgr.explore(find=find_condition)

    # output result
    if simgr.found:
        solution_state = simgr.found[0]
        scanf0 = solution_state.globals['solution0']
        scanf1 = solution_state.globals['solution1']
        print(scanf0, scanf1)
        solution0 = solution_state.solver.eval(scanf0)
        solution1 = solution_state.solver.eval(scanf1, cast_to=bytes)

        print(f'{solution0} {solution1}')
    else:
        print('no result')

if __name__=='__main__':
    main()
```