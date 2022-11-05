#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Conding and enconding library.

@author: David Orive Miguel
"""

from base64 import b64encode, b64decode


def hex_to_b64(str_hex):
    """
    Converts an string in hex to base64.

    INPUTS:
        * string, hexadecimal
    OUTPUTS:
        * string, base64
        * bytes, raw bytes
    """    
    
    raw_bytes = bytes.fromhex(str_hex)
    str_b64 = b64encode(raw_bytes).decode()
    
    return str_b64, raw_bytes
    

def xor_operator(str1, str2):
    """
    Performs a XOR to two equal-length hex strings.
    
    INPUTS:
        * str1: hex string
        * str2: hex string
    OUTPUTS:
        * hex string after XOR.
        * raw bytes after XOR.
    """
    
    # Check that they have equal length
    if len(str1) != len(str2):
        raise ValueError('Buffers have not the same length!')
    
    # Convert strings to bytes
    raw_bytes1 = bytes.fromhex(str1)
    raw_bytes2 = bytes.fromhex(str2)
    
    # Perform XOR operation
    byte_end    = bytes([a^b for a, b in zip(raw_bytes1, raw_bytes2)])
    str_end     = byte_end.hex()
    
    return str_end, byte_end
    
    
    
    