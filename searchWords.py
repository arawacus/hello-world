def listFiles():
    listFiles = 'f1.txt', 'f2.txt', 'f3.txt'
    return listFiles

def getWordsSet(fileName):
    f = open(fileName)
    s = f.read()
    procS = s.replace(',', '')
    words = procS.split()
    sWords = set(words)
    return sWords

def dictWordsUpdate(dictWords, sWords, fileName):
    
    for word in sWords:
        if word in dictWords:
            dictWords[word].append(fileName)
        else:
            dictWords[word] = [fileName]
    return 

def dictWordsToFile(dictWords, indexFileName, lF):
    listFileToFile = ' '.join(str(x) for x in lF)
    f = open('temp.txt', "w")
    f.write(listFileToFile)

    print("file:")
    for word in dictWords:
        ind = ' '.join(str(x) for x in dictWords[word])
        print("{} {}".format(word, ind))
        
        f.write("\n{} {}".format(word, ind))
    return

def main():
    lF = listFiles()
    print("lF= {}".format(lF))
    dictWords = {}
    for fileID, fileName in enumerate(lF):
        print("fileName = {}".format(fileName))
        wordSet = getWordsSet(fileName)
        print("wordSet = {}".format(wordSet))
        dictWordsUpdate(dictWords, wordSet, fileID)
        print("dictWords = {}".format(dictWords))
    dictWordsToFile(dictWords,'temp.txt', lF)

main()
