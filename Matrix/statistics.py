s = input()
counts = dict()
for ch in s:
    counts[ch] = counts[ch] + 1 if ch in counts else 1
print(counts)