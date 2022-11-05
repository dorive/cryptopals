#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Library with functions to score texts.

@author: David Orive Miguel
"""

def score_english_text(str_to_score):
    """
    Scores the text using chi^2 method. It computes the summatory of
    (text_freq_char - theoretical_freq_char)^2/text_freq_char for the
    following characters: space, e, t, a, o and n. The assumed theoretical
    values are:
                Freq(%)
        space   18.3
        e       10.3
        t       7.5
        a       6.5
        o       6.2
        n       5.7
        
    The lower the score the more likely it will be a text written in English.
    
    INPUTS:
        * str_to_score: string
    OUTPUTS:
        * Score of the string: double
    """
    
    score = 0.0
    
    char_freqs = [18.3, 10.3, 7.5, 6.5, 6.2, 5.7]
                  
    for idx, char_test in enumerate([' ', 'e', 't', 'a', 'o', 'n']):
        score += (char_freqs[idx] - 100*str_to_score.count(char_test)/len(str_to_score))**2 / char_freqs[idx]
    
    return score

