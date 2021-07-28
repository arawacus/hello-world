

def letterFreq(s):
    letters = set(s)
    freq = {}
    for lett in letters:
        freq[lett] = s.count(lett)

    print(letters)

    return freq



# s = input("Введите строку\n")
s = "abracodabra boo"

res = letterFreq(s)
print("res = {}".format(res))