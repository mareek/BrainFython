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
        elif instruction == ']':
            if innerLoopCount == 0:
                return searchCursor
            else:
                innerLoopCount += 1
    return searchCursor


def execute_instruction(instruction):
    global pointer
    global tape
    global cursor
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
        print(chr(tape[pointer]))


filename = "hello_world.bf"
file = open(filename, "r")
program = file.read()

while cursor < len(program):
    execute_instruction(program[cursor])
    cursor += 1
