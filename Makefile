.SILENT: words
SHELL=/bin/bash
DICT?=/usr/share/dict/words

words:
	# remove proper nouns and words shorter than 4 letters,
	# remove any words with an 's'
	# remove words with more than 7 different letters,
	# resort it,
	# remove the exclude words,
	# put it all on one line,
	# and output it to words-filtered
	grep -E '^[a-z]{4,}$$' $(DICT) | \
	    grep -v s | \
		awk '{ split($$0, a, ""); delete h; for (i=1;i<=length(a);i++) h[a[i]]=1; if (length(h) < 8) print }' | \
		sort | \
		comm -23 - data/exclude-words | \
		tr -s '\n' ' ' > data/words-filtered
