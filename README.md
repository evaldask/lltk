[![Build Status](https://travis-ci.org/evalkaz/lltk.svg?branch=master)](https://travis-ci.org/evalkaz/lltk)
[![Coverage Status](https://coveralls.io/repos/github/evalkaz/lltk/badge.svg?branch=master)](https://coveralls.io/github/evalkaz/lltk?branch=master)

# LLTK
## Lithuanian Language ToolKit

This is Python3 library for Lithuanian language analysis. Currently these functions are supported:
* word [stemming](https://en.wikipedia.org/wiki/Stemming),
* paragraph splitting into sentences,
* text summarization based on [smmry](http://smmry.com/).

For summarization example please checkout example jupyter notebook.

Stemming and splitting is based on [TokenMill](https://github.com/tokenmill) work. So big thumbs up for these guys for opensourcing their tools.


## Installing for development
* Fork the project
* Clone your forked project:
```
$ git clone git@github.com:evalkaz/lltk.git
```
* Install development dependencies:
```
$ pip install -r requirements-dev.txt
```

## Running tests
After cloned and installed development dependencies run tests just typing the
following command:
```
$ pytest
```

#### Any contribution is welcome!
