import angr
import claripy
import glob

def number(state, n):
    return state.se.And(n <= '9', n >= '0')

FIND = 0x40203c
AVOID = 0x40205a
# bins = glob.glob("binaries/*.exe")
bins = ["./binaries/00000.exe"]
for binary in bins:
    p = angr.Project(binary)
    state = p.factory.blank_state()

    _input = claripy.BVS("input", 32, explicit_name=True)

    state.add_constraints(_input < 2147483648)
    state.add_constraints(_input >= 0)

    path = p.factory.path(state)
    pg = p.factory.path_group(state)
    pg.explore(find=FIND, avoid=AVOID)

    for pp in pg.deadended:
        print pp.state.posix.dumps(0)
    # print pg.deadended[0]
    # pg.explore(find=FIND, avoid=AVOID)
    found = pg.found[0].state

    flag = found.se.BVS("input", 32, explicit_name="True")

    # print found.se.any_n_int(found.stack_pop(), 10)
    # ex = p.surveyors.Explorer(start=path, find=FIND, avoid=AVOID)

    # print('running explorer')
    # ex.run()

    # print('found solution')
    # found = ex._f.state#.posix.dumps(0) # ex._f is equiv. to ex.found[0]
    # print ex._f.state.posix.dumps(0)
    # sols = found.se.any_n_int(found.stack_pop(), 10)
    # for sol in sols:
    #     print sol
    # pg = p.factory.path_group(state)

    # pg.explore(find=FIND, avoid=AVOID)

    # found = pg.deadended[0].state

    # solutions = found.se.any_n_int(found.stack_pop(), 10) # ask for up to 10 solutions if possible
    # for solution in solutions:
    #     print solution
    # print found.se.any_int(found.stack_pop())
    # print found
    # print pg.found
    # print "'%s'" % found
