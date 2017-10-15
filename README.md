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
$ git clone git@github.com:<yougithubuser>/lltk.git
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
