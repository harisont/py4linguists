import langid
import spacy_udpipe as udpipe

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
    udpipe.download(lang)
    parse = udpipe.load(lang)
    tokens = parse(sent)
    return [(token.text, token.lemma_) for token in tokens]

def pos_tags(sent,lang="en"):
    """Given a sentence, return a list of (word,part-of-speech tag) pairs
    
    sent -- the sentence as a string of text
    lang -- the two-letter ISO code of the language the text is written in
            (default: en)"""
    udpipe.download(lang)
    parse = udpipe.load(lang)
    tokens = parse(sent)
    return [(token.text, token.pos_) for token in tokens]