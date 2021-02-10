# Spelling Beat

Serverless Solver for [everyone's favorite spelling puzzle](https://www.nytimes.com/puzzles/spelling-bee).

<https://spellingbeat.com>

## Development

No setup required. Just open [index.html](index.html) in your browser. If you want to run it from a server, one easy way is with python:

```
python3 -m http.server # or SimpleHTTPServer for python2
```

### The Word List

The word list is derived from `/usr/share/dict/words`, which ships on most *nix-based machines, including macOS. It's Webster's Second International from 1934, so it is somewhat dated, but good enough. Since Spelling Bee uses a dictionary that removes a lot of uncommon words, it will actually return a good number of words not accepted by Spelling Bee.

This is what I use to pare the list down for the app:

```
grep -E '^[a-z]{4,}$' /usr/share/dict/words \ 
  | awk '{ split($0, a, ""); delete h; for (i=1;i<=length(a);i++) h[a[i]]=1; if (length(h) < 8) print }' \
  | tr '\n' ' ' > words-filtered
```

The first line filters out proper nouns and words less than four characters. The second removes any words that have more than 7 unique letters. And the last just puts them all on one line, space-separated. This can then be pasted directly in to [application.js](js/application.js).

## Legalese

This code (c) 2021 by Brad Greenlee. Released under the [MIT license](LICENSE).
