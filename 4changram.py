#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import os

TOKEN=""

tb = telebot.TeleBot(TOKEN)

def sendMsg(chatId,text):
	root=tb.send_message(chatId,text)
	print root.message_id
	#another=tb.send_photo(chatId,open("a.png","rb"),reply_to_message_id=root.message_id)
	#img=open("a.png","rb")
	#tb.reply_to(root,img)
	
def sendImg(chatId,image):
	tb.send_photo(chatId,image,)

def listener(messages):
	for message in messages:
		print message.text
		print message
		sendMsg(message.chat.id,message.text)

def main(args):
	tb.set_update_listener(listener)
	tb.polling()
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
	archivoToken = open("token.txt","r")
	TOKEN = archivoToken.readline()
	print(TOKEN)
	
