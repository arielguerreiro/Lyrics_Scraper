#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 23:46:29 2020

@author: ariel
"""

import artist_search as ar
import os

def main():
    cont = True
    while cont == True:
        print("Welcome to the lyric finder.",
              "\nWe will find the lyrics for the top 20 songs of a given artist.",
              "\nPlease, insert an artist:")
        to_search = str(input('>'))
        
        ar.artist_link_search(to_search)
                
        os.system("scrapy runspider musicspider.py -s LOG_ENABLED=0")
        cont = False

main()
