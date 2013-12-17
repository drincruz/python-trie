"""
Testing for trie
"""

from nose.tools import eq_
from trie import Trie

def test_abc_add_word():
    """
    Test creating a simple trie with pattern "abc"
    """
    my_test =  {"a": 
                    {"b": 
                        {"c": 
                            {"!THIS_IS_THE_END!":
                                {"word": "abc"}
                            }
                        }
                    }
                }
    trie_test = Trie()
    trie_test.add_word("abc")
    eq_(my_test, trie_test.root)

def test_asterisk_add_word():
    """
    Test creating a simple trie with pattern "*,x,*,z"
    """
    my_test =  {"*": 
                    {"x": 
                        {"*":
                            { "z":
                                {"!THIS_IS_THE_END!":
                                    {"word": "*x*z"}
                                }
                            }
                        }
                    }
                }
    trie_test = Trie()
    trie_test.add_word("*x*z")
    eq_(my_test, trie_test.root)

def test_contains_true():
    """
    Test if trie contains path
    """
    trie = Trie()
    trie.add_word("x,y,z")
    eq_(True, trie.contains_word("x,y,z"))

def test_contains_false():
    """
    Test if trie contains path
    """
    trie = Trie()
    trie.add_word("x,y,z")
    eq_(False, trie.contains_word("a,y,z"))
    eq_(False, trie.contains_word("x,y,z,more"))
