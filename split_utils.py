import re
from spellchecker import SpellChecker
import string
import wordninja

corrections ={r"won\'t": "will not",
              r"can\'t": "can not",
              r"n\'t": " not",
              r"\'re": " are",
              r"\'s": " is",
              r"\'d": " would",
              r"\'ll": " will",
              r"\'t": " not",
              r"\'ve": " have",
              r"\'m": " am"}

spellcheck = SpellChecker()

def decontracted(phrase):  

    for k,v in corrections.items():
        phrase = re.sub(k, v, phrase)
    return phrase

def split_word(compound_word):
    '''
    Takes in compound word
    Splits it into individual words
    Returns string with spaced words
    '''
    sep_words = wordninja.split(compound_word)
    return sep_words

def decide_split(word):
    if not spellcheck[word]:
        nearest = spellcheck.correction(word)
        #When there is no valid word, the nearest word
        #is the same as the original
        if word == nearest:
            print('The compound word is {}'.format(word))
            return split_word(word)
        else:
            return nearest
    else:
        return word

def split_incorrect(text):
    '''
    Takes in a long string
    The punctuation parameter checks if punctuation marks are to
    be preserved
    Splits into component words, checks for incorrect spellings
    For incorrect spellings, checks if is possibly compound
    If not, then looks for the closest one word in the dictionary
    Returns the entire text with all words corrected
    '''
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    fixed_words =[decide_split(decontracted(word)) for word in words]
    final = " ".join(fixed_words)
    return final
