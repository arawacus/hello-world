def readFile(fileName):
    f = open(fileName, "r")
    lines = f.readlines()
    # print("lines = {}".format(lines))
    return lines

def procData(lines):
    listFiles = lines[0]
    print("listFiles = {}".format(listFiles))
    dictWords = {}
    for currLineId in range (1, len(lines)):
        word = lines[currLineId].split()
        # print("word[0] = {}".format(word[0]))
        wordList = []
        for currWordId in range (1, len(word)):
            indFile = int(word[currWordId])
            wordList.append(indFile)

        dictWords[word[0]] = wordList
    print("dictWords = {}".format(dictWords))
    return



lines = readFile("temp.txt")
# print("lines[1] = {}".format(lines[1]))
procData(lines)
