import spacy
import textacy
nlp = spacy.load('en_core_web_sm')
en = textacy.load_spacy_lang("en_core_web_sm")
from textacy import TextStats


def get_flesch(text):    
    doc = textacy.make_spacy_doc(text, lang=en)
    ts = TextStats(doc)
    try:
        return ts.flesch_kincaid_grade_level
    except ZeroDivisionError:
        return (11.8 * ts.n_syllables) + (0.39 * ts.n_words) - 15.59

def get_npoly(text):
    doc = textacy.make_spacy_doc(text, lang=en)
    ts = TextStats(doc)
    return ts.n_polysyllable_words