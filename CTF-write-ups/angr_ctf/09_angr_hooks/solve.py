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
    proj = angr.Project('./09_angr_hooks')

    # create a SimState object
    init_state = proj.factory.entry_state()

    # set check_equals address
    check_address = 0x080486B3

    # define hook
    skip_len = 5
    @proj.hook(check_address, length=skip_len)
    def skip_check(state):
        print('hooking!')
        buffer_addr = 0x0804A054
        load_buffer_symbol = state.memory.load(buffer_addr, 16)
        check_str = 'XYMKBKUHNIQYNQXE'
        # create a bitvector value
        state.regs.eax = claripy.If(
            load_buffer_symbol == check_str,
            claripy.BVV(1, 32),
            claripy.BVV(0, 32)
        )

    # create a simulation manager
    simgr = proj.factory.simgr(init_state)
        
    # explore
    simgr.explore(find=find_condition, avoid=avoid_condition)

    # output result
    if simgr.found:
        solution_state = simgr.found[0]
        flag = solution_state.posix.dumps(sys.stdin.fileno())
        print(flag)
    else:
        print('no result')

if __name__=='__main__':
    main() 