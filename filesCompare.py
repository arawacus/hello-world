def fileProc(file):
    f = open(file)
    s = f.read()
    procS = s.replace(',', '')
    words = procS.split()
    sWords = set(words)
    return sWords

words1 = fileProc("file1.txt") 
words2 = fileProc("file2.txt")   
print("words1 = {}".format(words1))    
print("words2 = {}".format(words2))    
# words2 = set(s2)
compare = words1 & words2
print("compare = {}".format(compare))    





