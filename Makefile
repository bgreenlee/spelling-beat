.SILENT: words
SHELL=/bin/bash
DICT?=/usr/share/dict/words

words:
	script/generate_wordlist.py
