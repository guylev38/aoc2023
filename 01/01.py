import regex as re

def read_file():
    data = []
    with open("data.txt", "r") as d:
        for line in d.readlines():
            data.append(line.strip())
    return data

def get_value(num):
    if num == "one" or num == "1":
        return 1
    elif num == "two" or num == "2":
        return 2
    elif num == "three" or num == "3":
        return 3
    elif num == "four" or num == "4":
        return 4
    elif num == "five" or num == "5":
        return 5
    elif num == "six" or num == "6":
        return 6
    elif num == "seven" or num == "7":
        return 7
    elif num == "eight" or num == "8":
        return 8
    elif num == "nine" or num == "9":
        return 9 
    else:
        return 0


def part_one(data):
    digits = [] 
    sum = 0
    for line in data: 
        row = []
        for c in line:
            if c.isdigit() == True:
                row.append(int(c))
        digits.append(row)

    for d in digits:
        num = int(d[0]) * 10 + d[-1]
        sum += num

    print(f"Sum: {sum}") 


                


def part_two(data):
    # Use external regex to find the numbers and convert them to int using get_value
    PATTERN = r'one|two|three|four|five|six|seven|eight|nine|[1-9]'
    matches = []
    sum = 0
    for line in data:
        matches.append(re.findall(PATTERN, line, overlapped=True))
    
    for m in matches:
        number = get_value(m[0]) * 10 + get_value(m[-1])
        sum += number 

    print(f"Sum: {sum}")



def main():
    data = read_file()
    print("PART ONE:")
    part_one(data)
    print("PART TWO:")
    part_two(data)

main()