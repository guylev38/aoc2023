import regex as re

def read_data():
    data = []
    with open("02.txt", "r") as d:
        for line in d.readlines():
            data.append(re.split("; |, |:", line.strip()))
    return data
    

def part_one(data):
    possible_games = []
    for x in data:
        is_possible = True
        for i in range(1, len(x)):
            reveal = re.split("\s", x[i].strip())
            if reveal[1] == "red" and int(reveal[0]) > 12:
                is_possible = False
                break
            elif reveal[1] == "green" and int(reveal[0]) > 13:
                is_possible = False
                break
            elif reveal[1] == "blue" and int(reveal[0]) > 14:
                is_possible = False
                break
        if is_possible == True:
            possible_games.append(int(x[0].split(" ")[1]))
    print(sum(possible_games))

def part_two(data):
    powers = []
    for x in data:
        red = 0
        green = 0
        blue = 0
        for i in range(1, len(x)):
            reveal = re.split("\s", x[i].strip())
            if reveal[1] == "red" and int(reveal[0]) > red:
                red = int(reveal[0])
            elif reveal[1] == "green" and int(reveal[0]) > green:
                green = int(reveal[0])
            elif reveal[1] == "blue" and int(reveal[0]) > blue:
                blue = int(reveal[0])
            
        powers.append(red * green * blue)

    print(sum(powers))


def main():
    data = read_data()
    print("PART ONE:")
    part_one(data)
    print("PART TWO: ")
    part_two(data)

main()
