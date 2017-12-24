#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import get

class Post:
	def __init__(self,id,text,image=None,main=True):
		self.id=id
		self.text=text
		self.image=image
		if(main):
			self.subs=[]

class Page:
	def __init__(self,board,number):
		
	
