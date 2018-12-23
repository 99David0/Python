# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 17:38:47 2018

@author: david
"""

def Caesar_Cipher(message,key):
    """Takes two inputs, a string and an integer, and rotates the string by "key" values in the alphabet and returns the encryption. """
    
    message=message.upper()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper() 
    ls_indices=[]   
    encrypt=''
    
    for ch in message:
        if ch not in alphabet:
            pass
        else:
            ch_indices=alphabet.find(ch)  
            ls_indices+=[ch_indices] 
            shift=(ch_indices+key)%26
            encrypt+=alphabet[shift]
        
    return encrypt.upper()
    return ls_indices   
    
        
  



    
    
    
    
