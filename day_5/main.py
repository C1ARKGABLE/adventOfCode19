import sys
import math

# [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
op_list = []

for line in open("opList.csv"):
    op_list.append(line.strip().split(","))

master = {}
for pos, x in enumerate(op_list[0]):
    master[pos] = int(x)

op_lens = {1: 3,
           2: 3,
           3: 1,
           4: 1,
           5: 3,
           6: 3,
           7: 3,
           8: 3,
           99: 0}


def compute(op_dict, i=0):

    while i != -1:
        # print("=" * 20)
        try:
            op_dict, i = retrieve(op_dict, i)
        except Exception as e:
            # print(i)
            print([(op_dict[x], x) for x in range(i - 4, i + 4)])
            sys.exit()

    return -1


def retrieve(op_dict, current, instr_len=6, op_code_len=2):
    op_str = f"{op_dict[current]:0{instr_len}d}"
    op_code = int(op_str[-op_code_len:])
    modes = op_str[:-op_code_len][::-1]

    op_len = op_lens[int(op_code)]

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

    vals = [
        op_dict[current + i] if int(modes[i]
                                    ) == 1 else op_dict[op_dict[current + i]]
        for i in range(0, op_len - 1)
    ]

    out_reg = op_dict[current + op_len - 1]

    if op_code == 1:
        # print(f"adding {vals = } to {out_reg = }")
        out = sum(vals)
    elif op_code == 2:
        # print(f"multiplying {vals = } to {out_reg = }")
        out = math.prod(vals)
    elif op_code == 3:
        out = int(input("Enter an int:\n"))
        # print(f"storing {out = } to {out_reg = }")
    elif op_code == 4:
        print("*" * 20)
        print("OUTPUT BLOCK:")
        if int(modes[0]) == 1:
            print(out_reg)
        else:
            print(op_dict[out_reg])
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


compute(master.copy(), 0)
