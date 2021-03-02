#
#      Hex-Rays Decompiler project
#      Copyright (c) 2007-2020 by Hex-Rays, support@hex-rays.com
#      ALL RIGHTS RESERVED.
#
#      Sample plugin for Hex-Rays Decompiler.
#      It installs a custom microcode optimization rule:
#        x | ~x => -1
#
#      To see this plugin in action please use be_ornot_be.idb
#

import ida_hexrays
import ida_idaapi

class mop_t_extractor():
    @staticmethod
    def type_cmp(tar : ida_hexrays.mop_t,t) -> bool:
        return tar.t == t
    @staticmethod
    def op_cmp(mop : ida_hexrays.mop_t,tar) -> bool:
        if mop.t != ida_hexrays.mop_d:
            return False
        if mop.d.opcode != tar:
            return False
        return True
    @staticmethod
    def get_tar(target : ida_hexrays.mop_t = None):
        if target is None:
            raise RuntimeError("No target specified")
        m_type = target.t
        if m_type == ida_hexrays.mop_z:
            return None
        elif m_type == ida_hexrays.mop_r:
            return target.r
        elif m_type == ida_hexrays.mop_n:
            return target.nnn
        elif m_type == ida_hexrays.mop_str:
            return target.cstr
        elif m_type == ida_hexrays.mop_d:
            return target.d
        elif m_type == ida_hexrays.mop_S:
            return target.s
        elif m_type == ida_hexrays.mop_v:
            return target.g
        elif m_type == ida_hexrays.mop_b:
            return target.b
        elif m_type == ida_hexrays.mop_f:
            return target.f
        elif m_type == ida_hexrays.mop_l:
            return target.l
        elif m_type == ida_hexrays.mop_a:
            return target.a
        elif m_type == ida_hexrays.mop_h:
            return target.helper
        elif m_type == ida_hexrays.mop_c:
            return target.c
        elif m_type == ida_hexrays.mop_fn:
            return target.fpc
        elif m_type == ida_hexrays.mop_p:
            return target.pair
        elif m_type == ida_hexrays.mop_sc:
            return target.scif
# recognize "x | ~x" and replace by -1
class subinsn_optimizer_t(ida_hexrays.minsn_visitor_t):
    cnt = 0
    def __visit_minsn(self):      # for each instruction...
        ins = self.curins       # take a reference to the current instruction

        # THE CORE OF THE PLUGIN IS HERE:
        # check the pattern "x | ~x"
        if ins.opcode == ida_hexrays.m_or and ins.r.is_insn(ida_hexrays.m_bnot) and ins.l == ins.r.d.l:
            if not ins.l.has_side_effects(): # avoid destroying side effects
                # pattern matched, convert to "mov -1, ..."
                ins.opcode = ida_hexrays.m_mov
                ins.l.make_number(-1, ins.r.size)
                ins.r = ida_hexrays.mop_t()
                self.cnt = self.cnt + 1 # number of changes we made
        return 0 # continue traversal

    def visit_minsn(self):
        ins = self.curins
        if ins.opcode == ida_hexrays.m_xor:
            if  ins.l.t == ida_hexrays.mop_v and ins.l.g == 0x404010 and not ins.l.has_side_effects():
                ins.l.make_number(0,ins.r.size)
                self.cnt = self.cnt + 1
                print("is insn detected")
            elif ins.l.r == ida_hexrays.mop_v and ins.r.g == 0x404010 and not ins.r.has_side_effects():
                ins.r.make_number(0,ins.l.size)
                self.cnt = self.cnt + 1
                print("IS insn detected")
            elif ins.l.t == ida_hexrays.mop_v and ins.l.g == 0x404014 and not ins.l.has_side_effects():
                ins.opcode = ida_hexrays.m_bnot
                ins.l = ins.r
                ins.r = ida_hexrays.mop_t()
                self.cnt = self.cnt + 1
                print("not insn detected")
            elif ins.r.t == ida_hexrays.mop_v and ins.r.g == 0x404014 and not ins.r.has_side_effects():
                ins.opcode = ida_hexrays.m_bnot
                ins.r = ida_hexrays.mop_t()
                self.cnt = self.cnt + 1
                print("NOT insn detected")
        # 识别 ~a & b | a & ~b
        elif ins.opcode == ida_hexrays.m_or \
            and mop_t_extractor.op_cmp(ins.l,ida_hexrays.m_and) \
            and mop_t_extractor.op_cmp(ins.r,ida_hexrays.m_and):
            left_and = ins.l.d
            right_and = ins.r.d
            a = left_and.l
            b = left_and.r
            c = right_and.l
            d = right_and.r
            print("XOR insn detected")
            print(a.t)
            if(a.t == 4):
                print("    ",a.d.opcode)
            print(b.t)
            if(b.t == 4):
                print("    ",b.d.opcode)
            print(c.t)
            if(c.t == 4):
                print("    ",c.d.opcode)
            print(d.t)
            if(d.t == 4):
                print("    ",d.d.opcode)
            if a == None or b == None or c == None or d == None:
                return 0
            if a.t == ida_hexrays.mop_d \
               and a.d.opcode == ida_hexrays.m_bnot \
               and b.t == ida_hexrays.mop_d \
               and b.d.opcode == ida_hexrays.m_ldx \
               and c.t == ida_hexrays.mop_d \
               and c.d.opcode == ida_hexrays.m_bnot \
               and d.t == ida_hexrays.mop_d \
               and d.d.opcode == ida_hexrays.m_ldx:
                print("XOR insn detected(type:1)")
                ins.opcode = ida_hexrays.m_xor
                ins.l = ida_hexrays.mop_t(b)
                ins.r = ida_hexrays.mop_t(d)
                self.cnt += 1
            elif a.t == ida_hexrays.mop_d \
               and b.t == ida_hexrays.mop_n \
               and c.t == ida_hexrays.mop_d \
               and d.t == ida_hexrays.mop_n \
               and c.d.opcode == ida_hexrays.m_bnot \
               and b.nnn.value == (~d.nnn.value)%0x100000000:
                print("XOR insn detected(type:2)")
                ins.opcode = ida_hexrays.m_xor
                ins.l = ida_hexrays.mop_t(a)
                ins.r = ida_hexrays.mop_t(d)
                self.cnt += 1
            elif a.t == ida_hexrays.mop_d \
               and a.d.opcode == ida_hexrays.m_bnot \
               and b.t == ida_hexrays.mop_d \
               and b.d.opcode == ida_hexrays.m_ldx \
               and c.t == ida_hexrays.mop_d \
               and c.d.opcode == ida_hexrays.m_ldx \
               and d.t == ida_hexrays.mop_d \
               and d.d.opcode == ida_hexrays.m_bnot:
                print("XOR insn detected(type:3)")
                ins.opcode = ida_hexrays.m_xor
                ins.l = ida_hexrays.mop_t(b)
                ins.r = ida_hexrays.mop_t(c)
                self.cnt += 1
        return 0
        

    # def visit_minsn(self):
    #     ins = self.curins
    #     if ins.opcode == ida_hexrays.m_xor and ins.d.t != 0:
    #         print("xor insn detected")
    #         print("    l:{}".format(ins.l))
    #         print("      l.t:{}".format(ins.l.t))
    #         if ins.l.is_insn():
    #             print("        l.d.l.t:{}",ins.l.d.l.t)
    #             print("        l.d.r.t:{}",ins.l.d.r.t)
    #             print("        l.d.d.t:{}",ins.l.d.d.t)
    #         print("    r:{}".format(ins.r))
    #         print("      r.t:{}".format(ins.r.t))
    #         if ins.r.is_insn():
    #             print("        r.d.l.t:{}",ins.r.d.l.t)
    #             print("        r.d.r.t:{}",ins.r.d.r.t)
    #             print("        r.d.d.t:{}",ins.r.d.d.t)
    #         print("    d:{}".format(ins.d))
    #         print("      d.t:{}".format(ins.d.t))
    #     return 0

# a custom instruction optimizer, boilerplate code
class sample_optimizer_t(ida_hexrays.optinsn_t):
    def func(self, blk, ins, optflags):
        opt = subinsn_optimizer_t()
        ins.for_all_insns(opt)
        if opt.cnt != 0:                # if we modified microcode,
            blk.mba.verify(True)        # run the verifier
        return opt.cnt                  # report the number of changes

# a plugin interface, boilerplate code
class my_plugin_t(ida_idaapi.plugin_t):
    flags = ida_idaapi.PLUGIN_HIDE
    wanted_name = "optimize x|~x"
    wanted_hotkey = ""
    comment = ""
    help = ""
    def init(self):
        if ida_hexrays.init_hexrays_plugin():
            self.optimizer = sample_optimizer_t()
            self.optimizer.install()
            print("Installed sample optimizer for 'x | ~x'")
            return ida_idaapi.PLUGIN_KEEP # keep us in the memory
    def term(self):
        self.optimizer.remove()
    def run(self, arg):
        if arg == 1:
            return self.optimizer.remove()
        elif arg == 2:
            return self.optimizer.install()

def PLUGIN_ENTRY():
    return my_plugin_t()
