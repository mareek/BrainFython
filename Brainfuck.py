import sys
import readchar

program = ""
cursor = 0
tape = [0] * 640000  # ought to be enough for anybody
pointer = 0
loopStarts = []


def findMatchingBracket(startingPoint):
    global program
    innerLoopCount = 0
    searchCursor = startingPoint
    while searchCursor < len(program):
        searchCursor += 1
        instruction = program[searchCursor]
        if instruction == '[':
            innerLoopCount += 1
        elif instruction == ']' and innerLoopCount > 0:
            innerLoopCount -= 1
        elif instruction == ']':
            return searchCursor
    return searchCursor


if len(sys.argv) <= 1:
    filename = "examples/hello_world.bf"
else:
    filename = sys.argv[1]

file = open(filename, "r")
program = file.read()

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
    elif instruction == '[':
        if tape[pointer] == 0:
            cursor = findMatchingBracket(cursor)
        else:
            loopStarts.append(cursor)
    elif instruction == ']':
        cursor = loopStarts.pop() - 1
    elif instruction == '.':
        c = chr(tape[pointer])
        print(c, end='', flush=True)
    elif instruction == ',':
        c = readchar.readchar()
        tape[pointer] = ord(c)
    cursor += 1
