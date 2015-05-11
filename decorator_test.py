#!/usr/bin/env python
# -*- coding: utf-8 -*-

print " test the decorator function in python environment"

def log(func):
	def wrapper(*args, **kw):
		print "call %s(): " % func.__name__
		return func(*args, **kw)
	return wrapper

@log
def now():
	print "2015-05-08"


print "and we are going to invoke the now() funtion with the log function append: "
now()

# the following are another way to test the advanced decorator abilities here
class WhatFor(object):
	def it(cls):
		print "work with %s " % cls
		it = classmethod(it)
		def uncommon():
			print "i could be one global functions here "
		uncommon = staticmethod(uncommon)

# and then, we could also test the map and reduce feature that provided in Python
init_word = ['TEST', 'guoshiCHAO', 'SHENdan']
# def process_word(*word):
# 	for w in word:
# 		w[1].upper()
# 		w[1:].lower()

# print "making the word that we input as formatted : "
# prio
# print process_word(init_word)














































































