#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 23:46:29 2020

@author: arielguerreiro
"""

import artist_search as ar
import os

def main():
    '''
    This function is responsible for recieving the artist name,
    calling the google search to find the correct link and then
    calling the crawler
    '''
    
    repeat = True
    while repeat == True:
        print("Welcome to the lyric finder.",
              "\nWe will find the lyrics for the top 20 songs of a given artist.",
              "\nPlease, insert an artist:")
        to_search = str(input('>'))
        
        artist_links = ar.artist_link_search(to_search)
                
        if len(artist_links ) == 1:
            repeat = False
        else:
            print("\nSorry, couldn't find the artist. Please, try again.\n\n")
    os.system("scrapy runspider musicspider.py -s LOG_ENABLED=0")

main()
