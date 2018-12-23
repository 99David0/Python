# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 17:38:47 2018

@author: david
"""

def Caesar_Cipher(message,key):
    """Takes two inputs, a string and an integer, and rotates the string by "key" values in the alphabet and returns the encryption. """
    #string=string.upper()
    message=message.upper()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper() 
    ls_indices=[]   #Contains the index of each character in "message."
    encrypt=''
    
    for ch in message:
        if ch not in alphabet:
            pass
        else:
            ch_indices=alphabet.find(ch)  #The find method returns the index of that character in the string.
            ls_indices+=[ch_indices] 
            shift=(ch_indices+key)%26
            encrypt+=alphabet[shift]
        
    return encrypt.upper()
    return ls_indices
    
        
  



    
    
    
    