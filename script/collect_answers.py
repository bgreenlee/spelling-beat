#!/usr/bin/env python3

import re
from datetime import date
import sys
import urllib.request
from datetime import datetime
import logging

logging.basicConfig(format='[%(asctime)s] [%(levelname)s] %(message)s')

def main():
    headers = {
        'User-Agent': 'Spelling Beat/1.0 (https://spellingbeat.com)'
    }
    req = urllib.request.Request("https://www.nytimes.com/puzzles/spelling-bee", headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            page = response.read().decode('utf-8')
            pattern = re.compile('"today":.*?"validLetters":\[(.*?)\].*?"answers":\[(.*?)\]')
            match = pattern.search(page)
            if match != None:
                letters = match[1].replace('"', '').replace(',', '')
                answers = match[2].replace('"', '')
                print(date.today(), letters, answers)
            else:
                logging.error("could not find answers")
    except urllib.error.URLError as e:
        logging.error(e.reason)

if __name__ == "__main__":
    main()