"""
Example of "constant expression" propagation.
A "constant expression" is an expression based on constants or init regs.

"""

from argparse import ArgumentParser

from miasm2.arch.x86.disasm import dis_x86_32 as dis_engine
from miasm2.analysis.machine import Machine
from miasm2.analysis.binary import Container
from miasm2.analysis.cst_propag import propagate_cst_expr
from miasm2.analysis.data_flow import dead_simp, \
    merge_blocks, remove_empty_assignblks
from miasm2.expression.simplifications import expr_simp


parser = ArgumentParser("Constant expression propagation")
parser.add_argument('filename', help="File to analyze")
parser.add_argument('address', help="Starting address for disassembly engine")
parser.add_argument('-s', "--simplify", action="store_true",
                    help="Apply simplifications rules (liveness, graph simplification, ...)")

args = parser.parse_args()


machine = Machine("x86_32")

cont = Container.from_stream(open(args.filename))
ira, dis_engine = machine.ira, machine.dis_engine
mdis = dis_engine(cont.bin_stream)
ir_arch = ira(mdis.loc_db)
addr = int(args.address, 0)

asmcfg = mdis.dis_multiblock(addr)
ircfg = ir_arch.new_ircfg_from_asmcfg(asmcfg)
entry_points = set([mdis.loc_db.get_offset_location(addr)])

init_infos = ir_arch.arch.regs.regs_init
cst_propag_link = propagate_cst_expr(ir_arch, ircfg, addr, init_infos)

if args.simplify:
    ircfg.simplify(expr_simp)
    modified = True
    while modified:
        modified = False
        modified |= dead_simp(ir_arch, ircfg)
        modified |= remove_empty_assignblks(ircfg)
        modified |= merge_blocks(ircfg, entry_points)


open("%s.propag.dot" % args.filename, 'w').write(ircfg.dot())
