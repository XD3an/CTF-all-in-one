# 15_angr_arbitrary_read

## Information

- [src](https://github.com/jakespringer/angr_ctf)

## Solution

### solve.py
```py
import angr
import claripy
import sys

# check puts
def check_puts(state):
    puts_parameter = state.memory.load(state.regs.esp+4, 4, endness=state.arch.memory_endness)
    # judge if puts_parameter is symbolic
    if state.solver.symbolic(puts_parameter):
        good_job_address = 0x484F4A47
        # copy state to check
        copied_state = state.copy()
        # check if puts parameter is good job string
        copied_state.add_constraints(puts_parameter==good_job_address)
        if copied_state.satisfiable():
            state.add_constraints(puts_parameter==good_job_address)
            return True
    return False

def find_condition(state):
    puts_address = 0x08048370
    if state.addr == puts_address:
        return check_puts(state)
    return False

    
def main():
    # load binary
    proj = angr.Project('./15_angr_arbitrary_read')

    # create a SimState object
    init_state = proj.factory.entry_state()

    # create a SimProcedures
    class ReplaceScnaf(angr.SimProcedure):
        def run(self, format, check_key_address, input_buffer_address):
            scanf0 = claripy.BVS('scanf0', 4*8)
            scanf1 = claripy.BVS('scanf1', 20*8)

            for char in scanf1.chop(bits=8):
                self.state.add_constraints(char >= '0', char <= 'z')
            
            self.state.memory.store(check_key_address, scanf0, endness=proj.arch.memory_endness)
            self.state.memory.store(input_buffer_address, scanf1)

            self.state.globals['solution0'] = scanf0
            self.state.globals['solution1'] = scanf1

    # set hook
    scanf_symbol = '__isoc99_scanf'
    proj.hook_symbol(scanf_symbol, ReplaceScnaf())

    # create a simulation manager
    simgr = proj.factory.simgr(init_state)

    # explore
    simgr.explore(find=find_condition)

    # output result
    if simgr.found:
        solution_state = simgr.found[0]
        scanf0 = solution_state.globals['solution0']
        scanf1 = solution_state.globals['solution1']
        solution0 = solution_state.solver.eval(scanf0)
        solution1 = solution_state.solver.eval(scanf1)
        print(f'{solution0} {solution1}')
    else:
        print('no result')

if __name__=='__main__':
    main()
```