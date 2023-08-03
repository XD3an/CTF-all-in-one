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
    proj = angr.Project('./03_angr_symbolic_registers')
    # get state
    # start_address will specify where the symbolic execution engine should begin.
    start_address = 0x08048980
    # use blank_state() to create a SimState object
    init_state = proj.factory.blank_state(addr=start_address)

    # Create a symbolic bitvector (the datatype Angr uses to inject symbolic
    # values into the binary.)
    password0_size_in_bits = 32 # :integer
    password0 = claripy.BVS('password0', password0_size_in_bits)

    password1_size_in_bits = 32 # :intger
    password1 = claripy.BVS('password1', password1_size_in_bits)

    password2_size_in_bits = 32 # :integer
    password2 = claripy.BVS('password2', password2_size_in_bits)
    #print(password0, password1, password2)

    # set init registers
    init_state.regs.eax = password0
    init_state.regs.ebx = password1
    init_state.regs.edx = password2

    # create a simulation manager
    simgr = proj.factory.simgr(init_state)

    # explore()
    simgr.explore(find=find_condition, avoid=avoid_condition)

    # output result
    if simgr.found:
        solution_state = simgr.found[0]
        # Solve for the symbolic values. If there are multiple solutions, we only
        # care about one, so we can use eval, which returns any (but only one)
        # solution. Pass eval the bitvector you want to solve for.      
        solution0 = solution_state.solver.eval(password0)
        solution1 = solution_state.solver.eval(password1)
        solution2 = solution_state.solver.eval(password2)
        
        #solution = ' '.join(map('{:x}'.format, [ solution0, solution1, solution2 ]))  # :string
        #print(solution)
        print(f'{solution0:x} {solution1:x} {solution2:x}')
    else:
        print('no result')

if __name__=='__main__':
    main()