import sys
import readchar

program = ""
if len(sys.argv) <= 1:
    filename = "examples/hello_world.bf"
else:
    filename = sys.argv[1]

file = open(filename, "r")
program = file.read()

# Jump table creation to improve loop performance
jumpTable = {}
openingBrackets = []
cursor = 0
while cursor < len(program):
    instruction = program[cursor]
    if instruction == '[':
        openingBrackets.append(cursor)
    elif instruction == ']':
        loopStart = openingBrackets.pop()
        jumpTable[loopStart] = cursor
        jumpTable[cursor] = loopStart
    cursor += 1

tape = [0] * 640000  # ought to be enough for anybody
pointer = 0
cursor = 0
while cursor < len(program):
    instruction = program[cursor]
    if instruction == '+':
        tape[pointer] += 1
    elif instruction == '-':
        tape[pointer] -= 1
    elif instruction == '>':
        pointer += 1
    elif instruction == '<':
        pointer -= 1
    elif instruction == '[' and tape[pointer] == 0:
            cursor = jumpTable[cursor]
    elif instruction == ']':
        cursor = jumpTable[cursor] - 1
    elif instruction == '.':
        c = chr(tape[pointer])
        print(c, end='', flush=True)
    elif instruction == ',':
        c = readchar.readchar()
        tape[pointer] = ord(c)
    cursor += 1
