#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 13:08:55 2021

@author: ishitakheria
"""

import socket

def xor(a,b):
    result = []
    
    #if the bits are same then xor is 0 else 1
    for i in range(1,len(b)):
        if a[i]==b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(divident,divisor):
    
    pick = len(divisor)
    
    temp=divident[0:pick]#slicing upto required comparision size
    
    while pick<len(divident):
        if temp[0]=='1':
            temp = xor(divisor, temp) + divident[pick]
        else:
            temp = xor('0'*pick, temp) + divident[pick]
        pick += 1
        
    if temp[0] == '1':
        temp = xor(divisor,temp)
    else:
        temp = xor('0'*pick,temp)
    
    checkword = temp
    return checkword

def encode(data,key):
    
    len_key = len(key)
    
    new_data = data + '0'*(len_key-1)
    remainder = mod2div(new_data,key)
    codeword = data + remainder 
    return codeword

s = socket.socket()
port = 12345
s.connect(('127.0.0.1', port)) #connecting the server to the local port
## s.sendall('Hello World')
input_string = input("Enter data you want to send-> ")
data =(''.join(format(ord(x), 'b') for x in input_string)) 
print(data)
key = str(input("Enter Key:- "))
  
ans = encode(data,key) 
print(ans) 
s.send(ans.encode()) 
  
  
# receive data from the server 
print(s.recv(1024))
  
# close the connection 
s.close() 




    


        