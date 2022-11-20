#!/usr/bin/env python3
import os
from collections import defaultdict

def main(words):
    # most pangrams
    pangram_count = defaultdict(int)
    max_count = 0
    for word in words:
        letters = ''.join(sorted(list(set(word))))
        if len(letters) != 7:
            continue
        pangram_count[letters] += 1
        max_count = max(pangram_count[letters], max_count)
            
    ordered_letters = sorted(pangram_count, key=pangram_count.get, reverse=True)
    top_n = 5
    print("Most pangrams:")
    for ordered_letter in ordered_letters:
        print(f'  {ordered_letter}, {pangram_count[ordered_letter]}')
        top_n -= 1
        if top_n == 0:
            break


    # top score


if __name__ == "__main__":
    rootdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
    datadir = os.path.join(rootdir, "data")
    with open(os.path.join(datadir, "words-filtered")) as f:
        words = f.read().strip().split(" ")

    main(words)
