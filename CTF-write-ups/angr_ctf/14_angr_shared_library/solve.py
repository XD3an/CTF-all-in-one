import angr
import claripy
import sys

def main():
    # load binary
    base = 0x4000000
    proj = angr.Project('./lib14_angr_shared_library.so', 
        load_options={
            'main_opts': {
                'custom_base_addr' : base
            }
    })

    # set validate() address
    validate_address = base + 0x6d7

    # create bitvector value
    buffer_pointer = claripy.BVV(0x3000000, 32)    # any empty address

    # create a SimState object
    init_state = proj.factory.call_state(validate_address, buffer_pointer, claripy.BVV(8, 32))

    # create a symbolic bitvector
    password = claripy.BVS('password', 8*8)
    init_state.memory.store(buffer_pointer, password)

    # create a simulation manager
    simgr = proj.factory.simgr(init_state)

    # explore
    find_address = base + 0x783
    simgr.explore(find=find_address)

    # output result
    if simgr.found:
        solution = simgr.found[0]
        solution.add_constraints(solution.regs.eax != 0)
        flag = solution.solver.eval(password, cast_to=bytes)
        print(flag)
    else:
        print('no result')

if __name__=='__main__':
    main()

