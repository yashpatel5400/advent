import os
import copy

base_instructions = open(os.path.expanduser("~/Downloads/input.txt")).read().split(",")
base_instructions = [int(l) for l in base_instructions]

ADD  = 1
MUL  = 2
HALT = 99

for noun in range(1, 100):
    for verb in range(1, 100):
        instructions = copy.deepcopy(base_instructions)

        pos = 0
        instructions[1] = noun
        instructions[2] = verb

        while instructions[pos] != HALT:
            opcode = instructions[pos]
            a = instructions[instructions[pos + 1]]
            b = instructions[instructions[pos + 2]]
            dest = instructions[pos + 3]
            
            if opcode == ADD:
                instructions[dest] = a + b
            elif opcode == MUL:
                instructions[dest] = a * b
            else:
                print(f"Unknown opcode: {opcode}!")
                exit()
            pos += 4
        output = instructions[0]

        if output == 19690720:
            print(100 * noun + verb)
            exit()