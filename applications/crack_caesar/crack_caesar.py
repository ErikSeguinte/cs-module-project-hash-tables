# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

from pathlib import Path

path = "cs-module-project-hash-tables/applications/crack_caesar/ciphertext.txt"

with open(path, "r") as f:
    cypher = f.read()

letters = set("ABCDEFGHIJKLMNOPQRSTUVWXWZ")

counts = dict()
for char in cypher:

    if char not in letters:
        continue
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1

sorted_counts = {
    k: v for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)
}

order = list("ETAOHNRISDLWUGFBMYCPKVQJXZ")


key = dict()
for i, k in enumerate(sorted_counts.keys()):
    key[k] = order[i]


uncoded = ""

for char in cypher:
    if char in letters:
        uncoded += key[char]
    else:
        uncoded += char

print(uncoded)
