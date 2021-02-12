.SILENT: update-words
SHELL=/bin/bash
DICT=/usr/share/dict/words

update-words:
	# remove proper nouns and words shorter than 4 letters,
	# remove words with more than 7 different letters,
	# add in the include words,
	# remove the exclude words,
	# put it all on one line,
	# and finally update application.js
	grep -E '^[a-z]{4,}$$' $(DICT) | \
		awk '{ split($$0, a, ""); delete h; for (i=1;i<=length(a);i++) h[a[i]]=1; if (length(h) < 8) print }' | \
		cat include-words - | \
		sed -e "$$(sed 's:.*:s/&//ig:' exclude-words)" | \
		tr -s '\n' ' ' | \
		perl -0pe "s/const words = \`.*?\`/const words = \`\n`cat`\n\`/sg" -i js/application.js
