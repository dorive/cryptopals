#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cryptopal: Challenge 5 from Set 1

@author: David Orive Miguel
"""

from lib_byteoperator import encode_repeating_xor


str_to_encode   = """Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"""
key             = r'ICE'
solution        = r'0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'

# XOR encode using the key
hex_encoded = encode_repeating_xor(str_to_encode, key)

# Check the solution is correct
if hex_encoded == solution:
    print('Solution is correct.')
else:
    raise ValueError('The solution is not correct.')




