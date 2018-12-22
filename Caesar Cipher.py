# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 21:54:57 2018

@author: david
"""

def Caesar_Cipher(message,key):
    """Caesar Cipher. Caesar used a key of 3. Takes a string and an integer as the inputs."""
    alphabet='abcdefghijklmnopqrstuvwxyz'.upper()
    alpha=list(alphabet)
    encrypt=''
    message=message.upper()
    
    for letter in message:
        if letter not in alpha:
            pass
        else:
            message_indices=alpha.index(letter) 
            encrypt_index=message_indices+key
            shift=alpha[encrypt_index]
            encrypt+=shift
    
    return encrypt