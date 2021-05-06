# -*- coding: utf-8 -*-
"""
Created on Mon May  3 19:48:56 2021

@author: אביב
"""
import json

file = open('happy_birthday.txt' , 'r' , encoding = 'utf8')
hendler= file.readlines()



def set_id(hendler):
    lst = list()
    for line in hendler:
        line = line.strip()
        if line.count(':') >= 2:
            name_start = line.find('-')
            name_end = line[name_start:].find(':')
            if not line[(name_start+2):(name_start+name_end)] in lst:
                lst.append(line[(name_start+2):(name_start+name_end)])  
                
    return (lst)   

def get_id(hendler):
    lst = list()
    for line in hendler:
        line = line.strip()
        if line.count(':') >= 2:
            start_id = line.find('-')
            end_id = line[start_id:].find(':')
            lst.append(line[(start_id+2):(start_id+end_id)])
            
    return (lst)

def get_date(hendler):
    lst = list()
    for line in hendler:
        line = line.strip()
        if line.count(':') >= 2:
            start_date = line.find('-')
            lst.append(line[:(start_date-1)])
            
    return (lst)
                
def get_txt(hendler):
    lst = list()
    for line in hendler:
        line = line.strip()
        if line.count(':') >= 2:
            start_txt = line.find('-')
            end_txt = line[start_txt:].find(':')
            lst.append(line[(end_txt+start_txt+2):])
            
    return (lst)   

def set_list(hendler):
     lst=list()
     counter=0
     for line in hendler:
        line = line.strip()
        if line.count(':') >= 2:
            dct = dict()
            dct["datetime"] = get_date(hendler)[counter]
            dct["id"] = set_id(hendler).index(get_id(hendler)[counter])+1
            dct["text"] = get_txt(hendler)[counter]
            lst.append(dct)
            counter=counter+1  
            
     return (lst)
       
def get_metadata(hendler):
    dct = dict()
    second_line = hendler[1]
    second_line = second_line.strip()
    
    
    group_start = second_line.find('"')
    group_end = second_line[(group_start+1):].find('"')
    dct["group name"] = second_line[(group_start+1):(group_start+group_end+1)]
    
    start_date = second_line.find('-')
    dct["creation date"] = second_line[:(start_date-1)]
    
    dct["number of participants:"] = len(set_id(hendler))
    
    creator_start = second_line.find("על ידי")
    dct["creator"] =1+set_id(hendler).index(second_line[(creator_start+len( "על ידי")+1):])
    
    return (dct)


def get_metadata_dictionary(hendler):   
    dct = {"metadata" : get_metadata(hendler) , "messages" : set_list(hendler)} 
    
    return (dct)
  
    
def json_convertor():    
    file_json=get_metadata(hendler)["group name"]+".txt" 
    with open(file_json, 'w', encoding='utf8') as file_json:
        json.dump(get_metadata_dictionary(hendler),file_json,ensure_ascii=False, indent = 4,)

json_convertor()


