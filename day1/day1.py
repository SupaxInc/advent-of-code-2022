import os

def parse(puzzle_input):
    # Convert each line to integers (keep empty lines to separate different elves)
    input = [int(line) if line.isdecimal() else line for line in puzzle_input.splitlines()] 
    return input

def calculateEachElfCalories(data):
    output = []
    totalCalories = 0

    for num in data:
        if num == '':
            output.append(totalCalories)
            totalCalories = 0
            continue
        
        totalCalories += num
    
    return output

# Return max calories amongst all elves
# O(n)
def part1(data):
    return max(calculateEachElfCalories(data))

# Return total of top three most calories amongst all elves
# O(nlogn)
def part2(data):
    sortedCalories = calculateEachElfCalories(data)
    sortedCalories.sort()
    return sum(sortedCalories[-3:])

def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "day1_input.txt")) as file:
        _input = file.read()
    
    print(solve(_input))