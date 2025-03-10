import binascii

def lst_addr_to_val(str_addr):
    data = binascii.unhexlify(str_addr)
    val = 0
    for b in data:
        val = val*256 + b
    return val

class LstDebuggerCa65:
    def __init__(self, lstfile):
        self.inst_map = {}
        with open(lstfile, "r") as f:
            
            for l in f.readlines():
                if l[0] != '0':
                    continue
                addr = lst_addr_to_val(l[0:6])
                inst = l[11:].rstrip("\n").rstrip().lstrip()
                if len(inst) == 0:
                    continue
                self.inst_map[addr] = inst

    def get_inst(self, addr):
        prgm_addr = addr - 0x8000
        if prgm_addr not in self.inst_map:
            return "NOP"
        return self.inst_map[prgm_addr]


class LstDebuggerAsm6:
    def __init__(self, lstfile):
        self.inst_map = {}
        with open(lstfile, "r") as f:
            
            for l in f.readlines():
                if l[0] != '0':
                    continue
                addr = lst_addr_to_val(l[1:5])
                inst = l[6:].rstrip("\n").rstrip().lstrip()
                if len(inst) == 0:
                    continue
                self.inst_map[addr] = inst

    def get_inst(self, addr):
        prgm_addr = addr
        if prgm_addr not in self.inst_map:
            return "NOP"
        return self.inst_map[prgm_addr]
    