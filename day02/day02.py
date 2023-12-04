from collections import defaultdict

def process_game(game_str):
    color_counts = defaultdict(int)

    # Split the game string by semicolon to get individual counts
    counts_list = game_str.split(';')

    # Iterate through each count and update color_counts
    for count in counts_list:
        colors = count.split(',')
        for color_count in colors:
            num, color= color_count.strip().split()
            color_counts[color] = max(color_counts[color], int(num))

    return color_counts

def main():
    with open('data.txt', 'r') as f:
        lines = f.readlines()

    sum=0
    power=0
    for line in lines:
        if line:
            game_name, counts_str = line.split(':')
            color_counts = process_game(counts_str)
            if color_counts['red'] <= 12 and color_counts['blue'] <= 14 and color_counts['green'] <= 13:
                sum += int(game_name.split()[1])
            power += color_counts['red'] * color_counts['blue'] * color_counts['green']

    print("Part 1: "+ str(sum))
    print("Part 2: "+ str(power))

if __name__ == "__main__":
    main()
