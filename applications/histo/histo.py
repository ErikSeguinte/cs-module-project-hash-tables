# Your code here
from pathlib import Path
import re

path = "applications/histo/robin.txt"

with open(path, "r") as f:
    words = re.findall(r"[\w']+", f.read())

counts = dict()

longest_length = 0
for word in words:
    word = word.lower()

    longest_length = max(longest_length, len(word))

    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

sorted_counts = {
    k: v for k, v in sorted(counts.items(), key=lambda item: (-item[1], item[0]), reverse=False)
}

spacing = longest_length + 2

for k, v in sorted_counts.items():
    hashtags = ['#'] * v
    print(f"{k}{' ':{spacing - len(k)}}{''.join(hashtags)}")
