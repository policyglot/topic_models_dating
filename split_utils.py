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

def decontract(phrase): 
 
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
    return " ".join(sep_words)

def replace_nearest(word):
    """
    Replaces incorrect words with the closest correct one
    If no such word is found, commence splitting in split_word
    """    
    nearest = spellcheck.correction(word)
    #When there is no valid word, the nearest word
    #is the same as the original
    if word == nearest:
        #This implies we need to try splitting it
        return split_word(word)
    return nearest
    
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
    #Remove all punctuation
    decontracted = decontract(text)
    no_punct = decontracted.translate(str.maketrans('', '', string.punctuation))
    words = no_punct.split()
    # replace contractions
    fixed_words =[replace_nearest(word) if not spellcheck[word] else word for word in words]
    final = " ".join(fixed_words)
    return final
