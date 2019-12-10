import sys
import math


op_list = []

for line in open("opList.csv"):
    op_list.append(line.strip().split(","))

master = {}
for pos, x in enumerate(op_list[0]):
    master[pos] = int(x)


class IntCode:
    def __init__(self, op_dict, start_ptr=0, instr_len=6, op_code_len=2):
        self.op_dict = op_dict
        self.ptr = start_ptr
        self.op_code_len = op_code_len
        self.instr_len = instr_len
        self.op_regs_count = {1: 3, 2: 3, 3: 1, 4: 1, 5: 3, 6: 3, 7: 3, 8: 3, 99: 0}

    def inputQueue(self, inp):
        self.inputQueue = inp
    def get_op_modes(self):
        op_str = f"{self.op_dict[self.ptr]:0{self.instr_len}d}"
        op_code = int(op_str[-self.op_code_len:])
        modes = op_str[:-self.op_code_len][::-1]

        return op_code, op_regs, modes

    def run(self):
        op_code = 0

        while op_code < 99:

            op_code, op_regs, modes = get_op_modes()
            
            
            
            op_regs = self.op_regs_count[int(op_code)]
            vals = [
                self.op_dict[self.ptr + i]
                if int(modes[i]) == 1
                else op_dict[op_dict[self.ptr + i]]
                for i in range(0, op_regs - 1)
            ]
            out_reg = op_dict[current + op_len - 1]


def compute(op_dict, i=0, print_out=True, inputs=False):

    while i != -1:
        # print("=" * 20)
        try:
            op_dict, i = retrieve(op_dict, i, print_out=print_out, inputs=inputs)
            if not type(op_dict) == dict:
                return op_dict
        except Exception as e:
            # print(i)
            print([(op_dict[x], x) for x in range(i - 4, i + 4)])
            sys.exit()

    return op_dict


def retrieve(op_dict, current, print_out=True, inputs=False):

    current += 1
    # print(modes)

    # vals = []

    # for i in range(0, op_len - 1):
    #     if int(modes[i]) == 1:
    #         print(f"Getting imed val {current+i}")
    #         vals.append(op_dict[current + i])
    #     else:
    #         print(f"Getting ref val at {op_dict[current+i]}")
    #         vals.append(op_dict[op_dict[current + i]])

    

    if op_code == 1:
        # print(f"adding {vals = } to {out_reg = }")
        out = sum(vals)
    elif op_code == 2:
        # print(f"multiplying {vals = } to {out_reg = }")
        out = math.prod(vals)
    elif op_code == 3:
        if not inputs:
            out = int(input("Enter an int:\n"))
            # print(f"storing {out = } to {out_reg = }")
        else:
            out = inputs.pop(0)
            # print(f"accepting input {out}")
    elif op_code == 4:

        if int(modes[0]) == 1:
            to_print = out_reg
        else:
            to_print = op_dict[out_reg]
        if print_out:
            print("*" * 20)
            print("OUTPUT BLOCK:")
            print(to_print)
        else:
            return to_print, -1

        return op_dict, current + op_len
    elif op_code == 5:
        if bool(vals[0]):

            return op_dict, vals[1]
        else:
            return op_dict, current + op_len - 1
    elif op_code == 6:

        if not bool(vals[0]):
            return op_dict, vals[1]
        else:
            return op_dict, current + op_len - 1
    elif op_code == 7:
        out = int(vals[0] < vals[1])
    elif op_code == 8:
        out = int(vals[0] == vals[1])
    elif op_code == 99:
        return op_dict, -1
    else:
        raise Exception(f"Invalid {op_code = }")

    op_dict[out_reg] = out

    return op_dict, current + op_len


def amp(user_phase=[4, 3, 2, 1, 0], signal=0):
    for i in user_phase:
        signal = compute(master.copy(), print_out=False, inputs=[i, signal])
    return signal


values_dict = {}

for i in range(0, 5):
    for j in range(0, 5):
        for k in range(0, 5):
            for l in range(0, 5):
                for m in range(0, 5):
                    values_dict[amp(user_phase=[i, j, k, l, m])] = [i, j, k, l, m]


print(max(values_dict.keys()))
# print(compute(master.copy(), print_out=False, inputs=[0, 3]))

