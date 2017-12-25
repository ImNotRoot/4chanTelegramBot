#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from requests import get

now = datetime.datetime.now()
URL_BASE = 'https://a.4cdn.org/'

def getBoardList():
    page = get(URL_BASE + 'boards.json')
    boards = page.json()

    cache = open('boards_cache.json',"a+")
    cacheData = [{"date":now, "boards":str(boards)}]
    cache.write(str(cacheData))
    cache.close()
    

    boardsListReturn = []
    for board in boards['boards']:
        boardsListReturn.append("/" + board['board'] + " - " + board['title'])
    return boardsListReturn

def getCatalogBoard(board):
    page = get(URL_BASE + board + '/catalog.json')
    boards = page.json()
    boardsListReturn = []