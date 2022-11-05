#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cryptopal: Challenge 2 from Set 1

@author: David Orive Miguel
"""

from lib_byteoperator import xor_operator

str1 = r'1c0111001f010100061a024b53535009181c'
str2 = r'686974207468652062756c6c277320657965'
str3 = r'746865206b696420646f6e277420706c6179'

str_result, byte_result = xor_operator(str1, str2)

if str3 == str_result:
    print('XOR operator works correctly!')
else:
    print('XOR operator is not working!')