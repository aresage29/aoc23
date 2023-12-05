def getWinningNumbers(numbers, seperator):
    # seperator is the index of the seperator between the winning numbers and the ticket numbers
    # function returns a list of the winning numbers
    winningNumbers = []
    for i in range(2, seperator):
        winningNumbers.append(int(numbers[i]))

    return winningNumbers

def getTicketNumbers(numbers, seperator):
    # seperator is the index of the seperator between the winning numbers and the ticket numbers
    # function returns a list of the ticket numbers
    ticketNumbers = []
    for i in range(seperator+1, len(numbers)):
        ticketNumbers.append(int(numbers[i]))

    return ticketNumbers

def getTicketPoints(line):
    # function returns the amount of points a ticket is worth
    points = 0
    winningCards = getNumberOfWinningTickets(line)
    if winningCards == 0:
        points = 0
    else:
        points = 2**(winningCards-1)

    return points


def getNumberOfWinningTickets(line):
    # function returns the amount of winning tickets
    numbers = line.split()
    seperator = numbers.index('|')
    winningNumbers = getWinningNumbers(numbers, seperator)
    ticketNumbers = getTicketNumbers(numbers, seperator)
    winningTickets = 0
    for number in ticketNumbers:
        if number in winningNumbers:
            winningTickets += 1

    return winningTickets

def part1():
    # function prints the amount of points the tickets are worth
    file = open("data.txt", "r")
    lines = file.readlines()
    file.close()

    totalPoints = 0
    for line in lines:
        totalPoints += getTicketPoints(line)
    print("Part1: " + str(totalPoints))


def part2():
    # function prints the number of tickets won
    file = open("data.txt", "r")
    lines = file.readlines()
    file.close()

    AmountOfTickets = [ 1 for i in range(0, len(lines))]
    for i in range(0, len(lines)):
        winningTickets = getNumberOfWinningTickets(lines[i])
        if winningTickets != 0:
            for j in range(winningTickets):
                if i+j+1<len(AmountOfTickets):
                    AmountOfTickets[i+j+1] += AmountOfTickets[i]

    totalPoints = 0
    for i in range(0, len(lines)):
        totalPoints += AmountOfTickets[i]

    print("Part2: " + str(totalPoints))


if __name__ == "__main__":
    part1()
    part2()

