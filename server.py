#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 13:54:22 2021

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

def decode(data,key):
    len_key = len(str(key))
    
    new_data = data + '0'*(len_key-1)
    remainder = mod2div(new_data,key)
    return remainder

s = socket.socket()
print("Socket created successfully!")

port = 12345
s.bind(('', port)) 
print ("socket binded to %s" % (port)) 
# put the socket into listening mode 
s.listen(5) 
print ("socket is listening! ") 

while True:
    #establishing the connection with the client 
    c , add = s.accept()
    print('Got connection from : ', add)
    
    data = c.recv(1024)
    data.decode()
    print(data)
    if not data:
        break;
    key = str(input("Enter key:- "))
    ans = decode(data,key)
    print("Remainder after decoding is :", ans)
    temp = "0" * (len(key) - 1) 
    if ans == temp: 
        c.sendall("THANK you Data ->"+data + " Received No error FOUND") 
    else: 
        c.sendall("Error in data") 
  
    c.close() 


    
    