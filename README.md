# Mysterion-128

Functions needed for encryption like s-box, l-box, shift-columns are in directory encryption_base_function.
Functions needed for decryption like rev-s-box, rev-l-box, rev-shift-columns are in directory decryption_base_function.

Mysterion encryption funciton on n rounds is defined is implimentetion/enc mysterion128.py
Mysterion decryption funciton on n rounds is defined is implimentetion/dec Invmysterion128.py
Those directories has also file enc.py and dec.py , which use these functions with proper data format ,which is follows:

message is given as string of length 32 where each charcter belongs to {0,1,...,e,f}
key format and ciphertex format is also same
varibale 'state' used in between is 4*4 matrix where state[i][j] is hex number <256.


Mysterion128_application is an oracle application that encrypts and decrypts a given file
