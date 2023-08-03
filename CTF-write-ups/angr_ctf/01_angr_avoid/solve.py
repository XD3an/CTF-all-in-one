import angr

# Load Binary
proj = angr.Project('./01_angr_avoid')

# get entry point
init_state = proj.factory.entry_state()

# create simulation manager, and use init_state(entry point) to initialize
simgr = proj.factory.simgr(init_state)

# avoid address & find address
avoid_addr = 0x080485A8
find_addr = 0x080485E0

# explore() to explore until find the "find address" and avoid the "avoid address"
simgr.explore(find=find_addr, avoid=avoid_addr)

# output result
if simgr.found:
    sim = simgr.found[0]
    print(sim.posix.dumps(0))
else:
    print("no result")