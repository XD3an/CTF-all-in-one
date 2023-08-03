import angr
import claripy
import sys
 
def explore(simgr):
    while (simgr.active or simgr.unconstrained) and (not simgr.found):
        for unconstrained_state in simgr.unconstrained:
            eip = unconstrained_state.regs.eip
            if unconstrained_state.satisfiable(extra_constraints=(eip == 0x42585249,)):
                simgr.move('unconstrained', 'found')
        simgr.step()

def main():
    proj = angr.Project('./17_angr_arbitrary_jump')
    init_state = proj.factory.entry_state()
 
    class ReplaceScanf(angr.SimProcedure):
        def run(self, format, input_buffer_address):
            input_buffer = claripy.BVS(
                'input_buffer', 64 * 8) 
            for char in input_buffer.chop(bits=8):
                self.state.add_constraints(char >= '0', char <= 'z')
 
            self.state.memory.store(
                input_buffer_address, input_buffer, endness=proj.arch.memory_endness)
            self.state.globals['solution'] = input_buffer
 
    scanf_symbol = '__isoc99_scanf'
    proj.hook_symbol(scanf_symbol, ReplaceScanf())
 
    simgr = proj.factory.simgr(
        init_state,
        save_unconstrained=True,
        stashes={
            'active':[init_state],
            'unconstrained': [],
            'found': [],
        })
    
    # explore
    explore(simgr)
 
    if simgr.found:
        solution_state = simgr.found[0]
        solution_state.add_constraints(solution_state.regs.eip == 0x42585249)
 
        flag = solution_state.solver.eval(solution_state.globals['solution'], cast_to=bytes)
        print(flag[::-1])
    else:
        print('no result')
 
if __name__ == '__main__':
  main()