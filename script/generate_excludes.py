#!/usr/bin/env python3
import os
import re


def main(answers_file, exclude_words_file, word_list_file):
    with open(word_list_file) as f:
        words = f.read().strip() #.split(" ")

    with open(answers_file) as f:
        answers_log = f.readlines()
    
    all_excludes = set()
    for line in answers_log:
        date, letters, answers = line.strip().split(" ")
        answers = set(answers.split(","))
        matches = solve(letters, words)
        excluded = matches - answers
        all_excludes = all_excludes | excluded
        # print(letters, ':', excluded)

    print(all_excludes)


def solve(letters, words):
    pattern = '\\b[' + letters + ']*' + letters[0] + '[' + letters + ']*\\b'
    matches = re.findall(pattern, words)
    return set(matches)

if __name__ == "__main__":
    rootdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
    datadir = os.path.join(rootdir, "data")
    answers_file = os.path.join(datadir, "answers.log")
    exclude_words_file = os.path.join(datadir, "exclude-words")
    word_list_file = os.path.join(datadir, "words-filtered")
    main(answers_file=answers_file, exclude_words_file=exclude_words_file, word_list_file=word_list_file)
