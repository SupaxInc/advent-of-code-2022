import os

def calculateAsciiCode(data):
    output = []
    for char in data:
        if char.islower():
            output.append(ord(char)-96) # a-z is from 1-26
        else:
            output.append(ord(char)-64+26) # A-Z is from 27-52
    
    return output

def parse(puzzle_input):
    input = []
    for line in puzzle_input.splitlines():
        newItem = []
        lineList = list(line)
        item1 = set(lineList[:len(lineList)//2])
        item2 = set(lineList[len(lineList)//2:])
        newItem.append(item1)
        newItem.append(item2)
        input.append(newItem)
    
    return input

def part1(data):
    output = []
    for items in data:
        item1 = items[0]
        item2 = items[1]
        output.append(item1.intersection(item2).pop())
    
    return sum(calculateAsciiCode(output))

def part2(data):
    return data

def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)

    return solution1

if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "day3_input.txt")) as file:
        _input = file.read()
    
    print(solve(_input))