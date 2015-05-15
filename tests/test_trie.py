"""
Testing for trie

"""

from nose.tools import eq_
from trie import TriePy


def test_abc_add_word():
    """
    Test creating a simple trie with pattern "abc"

    """
    my_test = {"a":
                    {"b": 
                        {"c": 
                            {"\0":
                                {"word": "abc"}
                            }
                        }
                    }
                }
    trie_test = TriePy()
    trie_test.add_word("abc")
    eq_(my_test, trie_test.root)


def test_asterisk_add_word():
    """
    Test creating a simple trie with pattern "*,x,*,z"

    """
    my_test = {"*":
                {"x":
                    {"*":
                        {"z":
                            {"\0":
                                {"word": "*x*z"}
                            }
                        }
                    }
                }
            }
    trie_test = TriePy()
    trie_test.add_word("*x*z")
    eq_(my_test, trie_test.root)


def test_contains_true():
    """
    Test if trie contains path

    """
    trie = TriePy()
    trie.add_word("x,y,z")
    eq_(True, trie.contains_word("x,y,z"))


def test_contains_false():
    """
    Test if trie contains path

    """
    trie = TriePy()
    trie.add_word("x,y,z")
    eq_(False, trie.contains_word("a,y,z"))
    eq_(False, trie.contains_word("x,y,z,more"))
