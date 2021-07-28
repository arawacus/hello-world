

def letterFreq(s):
    letters = set(s)
    freq = {}
    for lett in letters:
        freq[lett] = s.count(lett)

    print(freq)
    sorted_freq = sorted(freq.items(), key = lambda kv: kv[1])

    return sorted_freq

# path = "/Users/asya/GitHub/hello-world/text.txt"

s = "abracodabra boo"
f2 = open("text2.txt", 'w')
f2.write(s)
f2.close()
f = open('text2.txt')
st = f.read()

# s = input("Введите строку\n")
# s = "abracodabra boo"

res = letterFreq(st)
print("res = {}".format(res))