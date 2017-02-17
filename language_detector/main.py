# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

def detect_language(text, languages):
    """Returns the detected language of given text."""
    counter = 0
    select_lang = None
    for language in languages:
        num_of_words = len([word for word in language['common_words'] if word in text])
        if num_of_words > counter:
            counter = num_of_words
            select_lang = language['name'] 
            
    return select_lang
