import os
import copy

instructions = open(os.path.expanduser("~/Downloads/input.txt")).read()
instructions = instructions.split(",")
instructions = [int(l) for l in instructions]

for _ in range(500):
    instructions.append(None)

ADD  = 1
MUL  = 2
INP  = 3
OUP  = 4
JT   = 5
JF   = 6
JLT  = 7
JE   = 8
HALT = 99

num_params = {
    ADD: 4,
    MUL: 4,
    INP: 2,
    OUP: 2,
    JT: 3,
    JF: 3,
    JLT: 4,
    JE: 4,
}

def get_digit(n, i):
    try: 
        return int(str(n)[-(i + 1)])
    except:
        return 0

pos = 0
while instructions[pos] != HALT:
    inst = instructions[pos]
    opcode = 10 * get_digit(inst, 1) + get_digit(inst, 0)
    set_ir = False

    if opcode == ADD or opcode == MUL:
        a = get_digit(inst, 2)
        b = get_digit(inst, 3)
        
        a_val = instructions[pos + 1]
        b_val = instructions[pos + 2]
        c_val = instructions[pos + 3]

        # 0 -> parameter mode, 1 -> immediate
        if a == 0:
            a_val = instructions[a_val]
        if b == 0:
            b_val = instructions[b_val]
        
        if opcode == ADD:
            instructions[c_val] = a_val + b_val
        elif opcode == MUL:
            instructions[c_val] = a_val * b_val
    elif opcode == INP:
        val = int(input("Enter input: "))
        a_val = instructions[pos + 1]
        instructions[a_val] = val
    elif opcode == OUP:
        a = get_digit(inst, 2)
        
        a_val = instructions[pos + 1]
        if a == 0:
            a_val = instructions[a_val]
        print("PROGRAM OUT: {}".format(a_val))
    elif opcode == JT or opcode == JF:
        a = get_digit(inst, 2)
        b = get_digit(inst, 3)
        
        a_val = instructions[pos + 1]
        b_val = instructions[pos + 2]

        if a == 0:
            a_val = instructions[a_val]
        if b == 0:
            b_val = instructions[b_val]

        if opcode == JT:
            if a_val != 0:
                pos = b_val
                set_ir = True

        elif opcode == JF:
            if a_val == 0:
                pos = b_val
                set_ir = True
    elif opcode == JLT or opcode == JE:
        a = get_digit(inst, 2)
        b = get_digit(inst, 3)
        
        a_val = instructions[pos + 1]
        b_val = instructions[pos + 2]
        c_val = instructions[pos + 3]

        if a == 0:
            a_val = instructions[a_val]
        if b == 0:
            b_val = instructions[b_val]

        if opcode == JLT:
            if a_val < b_val:
                instructions[c_val] = 1
            else:
                instructions[c_val] = 0
        
        elif opcode == JE:
            if a_val == b_val:
                instructions[c_val] = 1
            else:
                instructions[c_val] = 0

    else:
        print(f"Unknown opcode: {opcode} for {inst}!")
        exit()
    if not set_ir:
        pos += num_params[opcode]