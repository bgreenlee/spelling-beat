.SILENT: words
SHELL=/bin/bash
DICT=/usr/local/share/dict

words:
	# remove proper nouns and words shorter than 4 letters,
	# remove words with more than 7 different letters,
	# remove the exclude words,
	# resort it,
	# put it all on one line,
	# and output it to words-filtered
	grep -E '^[a-z]{4,}$$' $(DICT) | \
		awk '{ split($$0, a, ""); delete h; for (i=1;i<=length(a);i++) h[a[i]]=1; if (length(h) < 8) print }' | \
		diff -w -y --suppress-common-lines - exclude-words | cut -f 1 | \
		sort | \
		tr -s '\n' ' ' > words-filtered
