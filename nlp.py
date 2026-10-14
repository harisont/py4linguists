import langid
import stanza

def language(txt):
    """Guess the language of the given text, returning the two-letter ISO
    language code.
    
    txt -- a string of text in an unknown language"""
    return langid.classify(txt)[0]

def sentences(txt):
    """Segment a text into a list of sentences.
    
    txt  -- a string of text"""
    for boundary in [".", "?", "!"]:
        txt = txt.replace(boundary,boundary + "<b>")
    isempty = lambda s: s or s.isspace() 
    return [sent.strip() for sent in txt.split("<b>") if isempty(sent)]

def lemmas(sent,lang="en"):
    """Given a sentence, return a list of (word,lemma) pairs

    sent -- the sentence as a string of text
    lang -- the two-letter ISO code of the language the text is written in
            (default: en)"""
    parse = stanza.Pipeline(lang=lang, processors='tokenize,lemma')
    tokens = parse(sent).sentences[0].words
    return [(token.text, token.lemma) for token in tokens]

def pos_tags(sent,lang="en"):
    """Given a sentence, return a list of (word,part-of-speech tag) pairs
    
    sent -- the sentence as a string of text
    lang -- the two-letter ISO code of the language the text is written in
            (default: en)"""
    parse = stanza.Pipeline(lang=lang, processors='tokenize,pos')
    tokens = parse(sent).sentences[0].words
    return [(token.text, token.upos) for token in tokens]
