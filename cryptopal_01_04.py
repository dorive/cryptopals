#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cryptopal: Challenge 4 from Set 1

@author: David Orive Miguel
"""

from lib_text_scoring import score_english_text


# Read file with encoded strings
with open('file_01_04.txt') as f:
    strings_encoded = f.readlines()
    

# Convert hexadecimal strings to bytes
bytes_encoded = [bytes.fromhex(str_encoded) for str_encoded in strings_encoded]

# XOR the encoded bytes with all possible characters (256 different bytes)
candidates = []
for bytes_temp in bytes_encoded:
    candidates.append([''.join(chr(byte_key ^ byte_i) for byte_i in bytes_temp) for byte_key in range(255)])

# Score candidates and get the one with lowest score
candidates_per_line = [min(list_candidates, key=score_english_text) for list_candidates in candidates]
candidate           = min(candidates_per_line, key=score_english_text)
idx_candidate       = min(range(len(candidates_per_line)), key=candidates_per_line.__getitem__)

# Print solution
print(candidate)
print('It was in line ' + str(idx_candidate+1))