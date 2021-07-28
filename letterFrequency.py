

def letterFreq(s):
    letters = set(s)
    freq = {}
    for lett in letters:
        freq[lett] = s.count(lett)
    k = sum(freq.values())
    print("total {}".format(k))
    sortedFreq = sorted(freq.items(), key = lambda kv: kv[1])

    return sortedFreq

# path = "/Users/asya/GitHub/hello-world/text.txt"

s = "abracodabra boo"
f2 = open("text2.txt", 'w')
f2.write(s)
f2.close()
f = open('text.txt')
st = f.read()

# s = input("Введите строку\n")
# s = "abracodabra boo"

res = letterFreq(st)
resStr = str(res)
f3 = open("text3.txt", 'a')
f3.write(resStr)
f3.close()
print("res = {}".format(res))