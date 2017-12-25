#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import get


def getBoardList():
    page = get('https://a.4cdn.org/boards.json')
    boards = page.json()
    boardsListReturn = []
    for board in boards['boards']:
        boardsListReturn.append("/" + board['board'] + " - " + board['title'])
    return boardsListReturn
