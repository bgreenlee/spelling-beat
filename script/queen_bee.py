#!/usr/bin/env python3

import re
import urllib.request
from functools import reduce

def is_pangram(word):
    return len(set(word)) == 7

def score(word):
    if len(word) < 4:
        return 0
    if len(word) == 4:
        return 1
    return len(word) + (7 if is_pangram(word) else 0)

def main():
    req = urllib.request.Request("https://www.nytimes.com/puzzles/spelling-bee",
        headers={
            'User-Agent': 'Spelling Beat/1.0 (https://spellingbeat.com)'
        })
    try:
        with urllib.request.urlopen(req) as response:
            page = response.read().decode('utf-8')
            pattern = re.compile('"today":.*?"validLetters":\[(.*?)\].*?"answers":\[(.*?)\]')
            match = pattern.search(page)
            if match != None:
                answers = match[2].replace('"', '').split(",")
                total = reduce(lambda acc, word: acc + score(word), answers, 0)
                print(f'{len(answers)} words, {total} points')
            else:
                print("Error: could not find answers")
    except urllib.error.URLError as e:
        print("Error:", e.reason)

if __name__ == "__main__":
    main()