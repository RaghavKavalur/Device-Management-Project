#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


def read(d):   
   for i in d:    
       print(i,d[i])


# In[3]:


def add(d):   
    id1=input("Enter id")   
    name=input("Enter device name")    
    d[name]=id1   
    f = open("devices.txt", "w")    
    c=0   
    for i in d:   
        if c!=0:        
            s="\n"+i + " " +d[i]      
            f.write(s)   
        else:         
            s=i + " " +d[i]   
            f.write(s)       
            c+=1  
    f.close()
    return d


# In[4]:


def update(d):   
    name=input("Enter device name")   
    id1=input("Enter id") 
    f = open("devices.txt", "w")   
    c=0  
    d[name]=id1   
    print(d)   
    for i in d:     
        if c!=0:      
            s="\n"+i + " " +d[i]    
            f.write(s)     
        else:      
            s=i + " " +d[i]    
            f.write(s)       
            c+=1   
    f.close()


# In[5]:


def delete(d):    
    d1={}  
    name=input("Enter device name")  
    f = open("devices.txt", "w")   
    c=0   
    for i in d:     
        if i!=name:      
            d1[i]=d[i]   
    for i in d1:    
        if c!=0:       
            s="\n"+i + " " +d1[i]         
            f.write(s)     
        else:     
            s=i + " " +d1[i]     
            f.write(s)        
            c+=1       
    f.close()


# In[7]:


c=0 
while(c<2):
    f = open("devices.txt", "r")   
    s=f.read()   
    f.close()    
    s=s.split()  
    d={}   
    for i in range(len(s)):    
        if i%2==0:      
            s1=s[i]       
            s2=s[i+1]       
            d[s1]=s2   
            print("Press 1 for read")   
            print("Press 2 for add")  
            print("Press 3 for update")   
            print("Press 4 for Delete")  
            print("Press 5 for Exit")  
            try:         
                n=int(input("Enter your choice"))   
            except:    
                print("Wrong Input")   
            if(n==1):     
                read(d)  
            elif(n==2):      
                d=add(d) 
            elif(n==3): 
                update(d)
            elif(n==4):  
                delete(d)
            elif(n==5):    
                break;    
            else:      
                print("Wrong Input,Plz try Again")    
            c+=1


# In[ ]:




