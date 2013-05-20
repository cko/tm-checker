#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mechanize
import logging
import sys
import codecs
from time import sleep

#TODO: check encoding

def read_special_word_file(filename):
	f = codecs.open(filename, 'r')
	wordlist = []
	for line in f:
		if not line==''  and not line.startswith('#'):
			wordlist.append(line.strip())
	return wordlist

def request_dpma_database (special_word):
	browser = mechanize.Browser() 
	browser.set_handle_robots(False)
	browser.open('https://register.dpma.de/DPMAregister/marke/einsteiger')
	browser.select_form(name='form')
	browser['wm'] = special_word
	response = browser.submit()
	return response.read()

def check_response(response):
	phrase1 = "Die Datenbankabfrage lieferte keine Treffer."
	phrase2 = "Anmeldung gilt als zur"
	if phrase1 in response or phrase2 in response:
		return "not registered"
	else:
		return "Please check manually"



list_of_words = read_special_word_file('words.txt')
for word in list_of_words:
	response = request_dpma_database(word)
	print word + ' \t' + check_response(response)
	sleep(5)
