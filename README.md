# Spelling Beat

Serverless Solver for [everyone's favorite spelling puzzle](https://www.nytimes.com/puzzles/spelling-bee).

<https://spellingbeat.com>

## Development

No setup required. Just open [index.html](index.html) in your browser. If you want to run it from a server, one easy way is with python:

```
python3 -m http.server # or SimpleHTTPServer for python2
```

### The Word List

The word list is currently derived from the [North American Scrabble Players Association](http:/www.scrabbleplayers.org) official word list, used with permission. You can also use `/usr/share/dict/words`, which ships on most *nix-based machines, including macOS. It's Webster's Second International from 1934, so it is somewhat dated, but good enough.

Since the Spelling Bee editors manually remove obscure or offensive words from the answer set for each puzzle, some of the words returned by Spelling Beat aren't going to be considered valid. There are also words the NYT considers valid, but aren't in the NASPA word list. I've started collecting some all the Spelling Bee answers (answers.log) in order to figure out what words to exclude and add.

To update the word list, run:

```
make words
```

This will filter the dictionary, removing proper nouns, words shorter than 4 characters, words with an "s", and words having more than 7 distinct letters, and then iterate through answers.log, comparing it to the official word list to figure out what words to add and remove. It writes the final word list to `words-filtered`. You then copy the contents of `words-filtered` into [line 4 of application.js](js/application.js#L4).

## Legalese

This code © 2021 by Brad Greenlee. Released under the [MIT license](LICENSE).

[NASPA Word List 2020 Edition](http:/www.scrabbleplayers.org) © NASPA 2020. The copy included in this app is licensed for personal use. You may not use it for any commercial purposes.
