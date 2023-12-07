def getSeedsPart1(fileText):
    # Returns a list of seeds
    seeds = []
    line = fileText.strip().split("\n")[0]
    elements = line.split()
    for element in elements[1:]:
        seeds.append(int(element))
    return seeds


def getSeedsPart2(fileText):
    # Returns a list of seeds as list with [first element, last element]
    seeds = []
    line = fileText.strip().split("\n")[0]
    elements = line.split()
    for i in range(1, len(elements), 2):
        seeds.append([int(elements[i]), int(elements[i + 1]) + int(elements[i]) - 1])
    return seeds


def getTransformationBlocks(fileText):
    # Returns a list of transformation blocks
    transformationBlocks = []
    text = fileText.strip().split("\n\n")
    for block in text[1:]:
        transformationBlocks.append(block.split("\n")[1:])
    for i in range(len(transformationBlocks)):
        for j in range(len(transformationBlocks[i])):
            block = transformationBlocks[i][j].split()
            block[0] = int(block[0])
            block[1] = int(block[1])
            block[2] = int(block[2])
            transformationBlocks[i][j] = block

    return transformationBlocks


def transform(seed, transformationBlock):
    # Returns a list of transformed seeds
    transformationMatrix = {}
    # Create a dictionary that maps the range of the seed to the first new value
    for item in transformationBlock:
        transformationMatrix[(item[1], item[1] + item[2] - 1)] = item[0]
    transformedSeed = []
    # check if the seed is in the range of the transformation matrix
    for item in seed:
        transformed = False
        for key in transformationMatrix.keys():
            # if the seed is in the range, the seed is transformed and the loop is broken
            if int(key[0]) <= item < int(key[1]):
                transformedSeed.append(transformationMatrix[key] + item - key[0])
                transformed = True
                break
        # if the seed is not in the range, the seed is added to the list of transformed seeds
        if not transformed:
            transformedSeed.append(item)

    return transformedSeed


def transform2(seed, transformationBlock):
    # Returns a list of transformed seeds
    transformationMatrix = {}
    for item in transformationBlock:
        # Create a dictionary that maps the range of the seed to the first new value
        transformationMatrix[(item[1], item[1] + item[2] - 1)] = item[0]
    transformedSeed = []
    newSeeds = seed.copy()
    changed = True
    # Reformat the seeds so that they don't overlap
    while changed:
        changed = False
        seed = newSeeds.copy()
        newSeeds = []
        for item in seed:
            transformed = False
            # check for every seed if it overlaps with a range in the transformation matrix and split it if it does
            for key in transformationMatrix.keys():
                if key[0] <= item[0] <= key[1] < item[1]:
                    newSeeds.append([item[0], key[1]])
                    newSeeds.append([key[1] + 1, item[1]])
                    transformed = True
                    changed = True
                    break
                elif item[0] < key[0] <= item[1] <= key[1]:
                    newSeeds.append([item[0], key[0] - 1])
                    newSeeds.append([key[0], item[1]])
                    transformed = True
                    changed = True
                    break
            # if the seed doesn't overlap with a range in the transformation matrix, it is added to the list of seeds
            if not transformed:
                newSeeds.append(item)
    # change the seeds to the new values
    for item in newSeeds:
        transformed = False
        for key in transformationMatrix.keys():
            # if the seed is in the range, the seed is transformed and the loop is broken
            if int(key[0]) <= item[0] <= int(key[1]):
                transformedSeed.append(
                    [transformationMatrix[key] + item[0] - key[0], transformationMatrix[key] + item[1] - key[0]])
                transformed = True
                break
        # if the seed is not in the range, the seed is added to the list of transformed seeds
        if not transformed:
            transformedSeed.append(item)

    return transformedSeed


def part1():
    # return the lowest seed for task one
    file = open("data.txt", "r")
    fileText = file.read()
    file.close()
    # get the seeds and transformation blocks
    seeds = getSeedsPart1(fileText)
    print("Seeds generated")
    transformationBlocks = getTransformationBlocks(fileText)
    newSeeds = seeds.copy()
    # transform the seeds
    for transformationBlock in transformationBlocks:
        newSeeds = transform(newSeeds, transformationBlock)
    newSeeds.sort()
    print("Part 1: " + str(newSeeds[0]))


def part2():
    # return the lowest seed for task two
    file = open("data.txt", "r")
    fileText = file.read()
    file.close()
    # get the seeds and transformation blocks
    seeds = getSeedsPart2(fileText)
    print("Seeds generated")
    transformationBlocks = getTransformationBlocks(fileText)
    newSeeds = seeds.copy()
    # transform the seeds
    for transformationBlock in transformationBlocks:
        newSeeds = transform2(newSeeds, transformationBlock)
    # find the lowest seed
    lowestSeed = newSeeds[0][0]
    for seed in newSeeds:
        if seed[0] < lowestSeed:
            lowestSeed = seed[0]
    print("Part 2: " + str(lowestSeed))


if __name__ == "__main__":
    part1()
    part2()
