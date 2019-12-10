# This is an interpreter for the BF language, but simplified for
import sys

op_list = []

for line in open("opList.csv"):
    op_list.append(line.strip().split(","))

master = {}
for pos, x in enumerate(op_list[0]):
    master[pos] = int(x)

def compute(op_dict, n, v, idx=0,word_size=4):
    op_dict[1] = n
    op_dict[2] = v

    for i in range(0, len(op_dict), word_size):
        op = op_dict[i]
        a_reg = op_dict[i + 1]
        b_reg = op_dict[i + 2]
        c_reg = op_dict[i + 3]
        if op == 1:
            out = op_dict[a_reg] + op_dict[b_reg]
        elif op == 2:
            out = op_dict[a_reg] * op_dict[b_reg]
        elif op == 99:
            return op_dict[idx]
        else:
            raise Exception(f"Invalid {op = }")
            break
        op_dict[c_reg] = out

    return -1


for n in range(0, 100):
    for v in range(0, 100):
    
        final = compute(master.copy(),n,v)
        if final == 19690720:
            print(100 * n + v)
            sys.exit()
            
