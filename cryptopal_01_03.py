#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cryptopal: Challenge 3 from Set 1

@author: David Orive Miguel
"""

from lib_text_scoring import score_english_text


str_encoded = r'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

# Convert hexadecimal to bytes
bytes_encoded = bytes.fromhex(str_encoded)

# XOR the encoded bytes with all possible characters (256 different bytes)
candidates = [''.join(chr(byte_key ^ byte_i) for byte_i in bytes_encoded) for byte_key in range(255)]

# Score candidates
str_decoded = min(candidates, key=score_english_text)

print(str_decoded)