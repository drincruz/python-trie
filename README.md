python-trie
===========

A simple trie implementation in Python

This implementation utilizes a dictionary as its backing
data structure. Essentially, it is creating nested dictionaries.


Example
----------
    >>> from trie import Trie
    >>> t = Trie()
    >>> t.add_word("dog")
    >>> t.add_word("doggy")
    >>> t.add_word("dogs")
    >>> t.contains_word("dog")
    True
    >>> t.contains_word("dogg")
    False
    >>> t.root
    {'d': {'o': {'g': {'!THIS_IS_THE_END!': {'word': 'dog'}, 's': {'!THIS_IS_THE_END!': {'word': 'dogs'}}, 'g': {'y': {'!THIS_IS_THE_END!': {'word': 'doggy'}}}}}}}


Unit Testing
----------
nose is used for unit testing and simple unit tests
can be run with the following in the source trie directory:
    `nosetests`
