import os

def parse(puzzle_input):
    # Convert each line to integers (keep empty lines to separate different elves)
    input = [line.split() for line in puzzle_input.splitlines()] 
    return input

def part1(data):
    player_guide = {
        'X': 'A', # rock
        'Y': 'B', # paper
        'Z': 'C'  # scissors
    }

    score_guide = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    total = 0

    for game in data:
        player1 = game[0]
        player2 = game[1]

        # draw
        if player1 == player_guide[player2]: 
            total += score_guide[player2] + 3
        # player 2 wins
        elif (player_guide[player2] == 'A' and player1 == 'C') or (player_guide[player2] == 'B' and player1 == 'A') or (player_guide[player2] == 'C' and player1 == 'B'):
            total += score_guide[player2] + 6
        # player 2 lose
        else:
            total += score_guide[player2]

    return total

def part2(data):
    lose_guide = {
        'A': 'C',
        'B': 'A',
        'C': 'B'
    }

    win_guide = {
        'C': 'A',
        'A': 'B',
        'B': 'C'
    }

    score_guide = {
        'A': 1,
        'B': 2,
        'C': 3
    }

    total = 0

    for game in data:
        player1 = game[0]
        scenario = game[1]

        if scenario == 'X': # need to lose
            total += score_guide[lose_guide[player1]]
        elif scenario == 'Z': # need to win
            total += score_guide[win_guide[player1]] + 6
        else: # need to draw
            total += score_guide[player1] + 3

    return total

def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "day2_input.txt")) as file:
        _input = file.read()
    
    print(solve(_input))