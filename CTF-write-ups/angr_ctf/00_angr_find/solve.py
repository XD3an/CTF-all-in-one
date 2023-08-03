import angr

# load binary
proj = angr.Project('./00_angr_find')

# get entry point
init_state = proj.factory.entry_state()

# create a simulation manager, and use init_state to initlize
simgr = proj.factory.simgr(init_state)

# we want to find the addr
find_addr = 0x08048678 

# explore() to explore until find the "find address"
simgr.explore(find=find_addr)

# output result
if simgr.found:
    # get simulation manager 
    simulations = simgr.found[0]
    print(simulations)
    # output all stdin string
    print(simulations.posix.dumps(0))
else:
    print('no result')
