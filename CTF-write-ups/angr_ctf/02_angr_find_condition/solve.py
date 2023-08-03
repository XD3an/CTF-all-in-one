import angr

def find_condition(state):
    stdout_output = state.posix.dumps(1)
    return b'Good Job.' in stdout_output

def avoid_condition(state):
    stdout_output = state.posix.dumps(1)
    return b'Try Again.' in stdout_output

def main():
    # load binary
    proj = angr.Project('./02_angr_find_condition')
    # get entry point
    init_state = proj.factory.entry_state()
    # create a simulation manager, and use init_state (entry point) to initialize
    simgr = proj.factory.simgr(init_state)

    # explore()
    # use find_condition to judge if it is in find condition
    # use avoid_condition to judge if it is in avoid condition
    simgr.explore(find=find_condition, avoid=avoid_condition)

    # output result
    if simgr.found:
        sim = simgr.found[0]
        print(sim.posix.dumps(0))
    else:
        print("no result")

if __name__=='__main__':
    main()