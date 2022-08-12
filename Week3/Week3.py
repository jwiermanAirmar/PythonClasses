# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 14:15:33 2022

@author: jwierman
"""

import subprocess

ip_addr = "8.8.8.8"

def ping(address):
    
    try:
        #decode makes it much more readable
        response = subprocess.check_output("ping " + address, 
                   shell = True, 
                   stderr = subprocess.STDOUT).strip().decode() 
            
        lines = response.split("\r\n")
        
        response_lines = lines[1:5]
        
        response_parsed = []
        
        for line in response_lines:
            
            time_str_start = line.split("Reply from " + address + ": bytes=32 time=")[1]
            
            time_str = time_str_start.split(" ")[0]
            
            response_parsed.append(time_str)
        print (response_parsed)
            
    except:
        
        print(" ")
        
        
if __name__ == "__main__":
    
    ping(ip_addr)