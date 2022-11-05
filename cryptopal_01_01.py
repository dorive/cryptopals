#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cryptopal: Challenge 1 from Set 1

@author: David Orive Miguel
"""

from lib_byteoperator import hex_to_b64

str_hex = r'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
str_b64 = r'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

str_output, bytes_output = hex_to_b64(str_hex)

if str_output == str_b64:
    print('Hex to B64 converter works correctly!')
else:
    print('Hex to B64 converter is not working!')