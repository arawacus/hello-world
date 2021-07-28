

def letterFreq(s):
    letters = set(s)
    freq = {}
    for lett in letters:
        freq[lett] = s.count(lett)

    print(freq)
    sorted_freq = sorted(freq.items(), key = lambda kv: kv[1])

    return sorted_freq



# s = input("Введите строку\n")
s = "abracodabra boo"

res = letterFreq(s)
print("res = {}".format(res))