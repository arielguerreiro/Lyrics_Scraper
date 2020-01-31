#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 23:37:03 2020

@author: arielguerreiro
"""

from googlesearch import search

def artist_link_search(to_search):
    '''
    This function searches google for the link to be used
    by the 'music spider' crawler
    '''
    # artist search
    query = '{} site:letras.mus.br'.format(str(to_search))
    artist_links = []
    for i in search(query,        # The query you want to run
                    tld = 'com',  # The top level domain
                    lang = 'pt',  # The language
                    num = 10,     # Number of results per page
                    start = 0,    # First result to retrieve
                    stop = 1,  # Last result to retrieve
                    pause = 0,  # Lapse between HTTP requests
                    ):
        artist_links.append(i)
        
    filepath = 'start_url.txt'
    f = open(filepath, 'w')
    if len(artist_links) > 0:
        f.write(artist_links[0])
    f.close()
    
    return artist_links