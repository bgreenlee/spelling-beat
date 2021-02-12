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

Two files, [include-words](include-words) and [exclude-words](exclude-words), are used to add and remove words from this dictionary.

To update the word list, just run:

```
make update-words
```

This will filter the dictionary, removing proper nouns, words shorter than 4 characters, and words having more than 7 distinct letters, and update the word list in application.js in-place.

## Legalese

This code (c) 2021 by Brad Greenlee. Released under the [MIT license](LICENSE).
