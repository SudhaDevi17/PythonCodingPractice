import collections
class FreqStack:

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        print("\n ####################### Push Operations #######################")
        f = self.freq[x] + 1
        print("f val is ", f)
        self.freq[x] = f
        print("After adding f : ", self.freq)
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x)
        print("pushed an item in the dictionary list group ", self.group, self.maxfreq)

    def pop(self):
        print("\n ####################### POP Operations #######################")
        x = self.group[self.maxfreq].pop()
        print("self group after pop  & Item popped is ", self.group, x)
        self.freq[x] -= 1
        print("Before reducing frequency", self.group[self.maxfreq])
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        print("After reducing frequency", self.group[self.maxfreq])
        return x

