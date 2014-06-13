"""
Testing for trie

"""

from nose.tools import eq_
from trie import TriePy

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
    trie_test = TriePy()
    trie_test.addWord("abc")
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
    trie_test = TriePy()
    trie_test.addWord("*x*z")
    eq_(my_test, trie_test.root)

def test_contains_true():
    """
    Test if trie contains path
    """
    trie = TriePy()
    trie.addWord("x,y,z")
    eq_(True, trie.containsWord("x,y,z"))

def test_contains_false():
    """
    Test if trie contains path
    """
    trie = TriePy()
    trie.addWord("x,y,z")
    eq_(False, trie.containsWord("a,y,z"))
    eq_(False, trie.containsWord("x,y,z,more"))
