# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 21:02:18 2018

@author: david
"""

def Vigenere_Cipher(message,key):
    """Vigenere Cipher using list methods in the code.Takes two strings as input."""
    message=message.upper()
    key=key.upper()
    alphabet='abcdefghijklmnopqrstuvwxyz'.upper()
    alpha=list(alphabet)
    alpha=alpha+alpha
    encryption=''
    k_ls=[]
    m_ls=[]

    for letter in key:
        letter_index=alpha.index(letter)
        k_ls+=[letter_index+1]    
        
    for ch in message:
        if ch not in alpha:
            pass
        else:
            ch_index=alpha.index(ch)
            m_ls+=[ch_index]
            
    while len(k_ls)<len(m_ls):  
        k_ls+=k_ls
    
    while len(k_ls)>len(m_ls):
        k_ls.pop()
        
    e_ls=[m_ls[i]+k_ls[i] for i in range(len(m_ls))]
    
    encrypt=[alpha[i] for i in e_ls]
    
    for i in encrypt:
        encryption+=i
        
    return encryption
