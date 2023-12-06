def getSeeds(fileText):
    seeds = []
    line = fileText.strip().split("\n")[0]
    elements = line.split()
    for element in elements[1:]:
        seeds.append(int(element))
    return seeds

def getTransformationBlocks(fileText):
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
    transformationMatrix = {}
    for item in transformationBlock:
        transformationMatrix[(item[1], item[1]+item[2])] = item[0]
    transformedSeed = []
    for item in seed:
        transformed = False
        print(transformationMatrix.keys())
        for key in transformationMatrix.keys():
            print(str(key[0]) + " " + str(item) + " " + str(key[1]))
            if int(key[0]) <= item < int(key[1]):
                print("Transformed " + str(item) + " to " + str(transformationMatrix[key]+item-key[0]))
                transformedSeed.append(transformationMatrix[key]+item-key[0])
                transformed = True
                break
        if not transformed:
            transformedSeed.append(item)


    return transformedSeed


def part1():
    file = open("data.txt", "r")
    fileText = file.read()
    file.close()
    seeds = getSeeds(fileText)
    print(seeds)
    transformationBlocks = getTransformationBlocks(fileText)
    newSeeds = seeds.copy()
    for transformationBlock in transformationBlocks:
        print(transformationBlock)
        newSeeds = transform(newSeeds, transformationBlock)
        print(newSeeds)
    print(newSeeds)
    newSeeds.sort()
    print(newSeeds)

if __name__ == "__main__":
    part1()


