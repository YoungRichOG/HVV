#! /usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author:YoungRichOG
Hacking Everything :-)
Date: 2020-02-07
'''

def main():
	with open('1.txt','r') as f:
		for strs in f:
			c_strs = CaseConversion(strs.rstrip())
			c_strs = DelSpecialStrs(c_strs)
			c_strs = HandleJoin(c_strs)
			c_strs = HandleLength(c_strs)
			c_strs = TotalLength(c_strs)

			if c_strs is not None:
				print(c_strs)


def CaseConversion(strs):
	strs = strs.lower()
	return strs

def DelSpecialStrs(strs):
	whitelist = [
		'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
		'v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','.','-']
	if all(ch in whitelist for ch in strs):
		return strs

def HandleJoin(strs):
	if strs is not None:
		if not strs.startswith('-') and not strs.endswith('-') and not strs.startswith('.') and not strs.endswith('.'):
			return strs

def HandleLength(strs):
	s_length = 0
	flag = 0
	if strs is not None:
		_length = len(strs.split('.'))
		if _length >1:
			for i in range(0,_length):
				s_length = len(strs.split('.')[i])
				if s_length >63:
					flag +=1
			if flag == 0:
				return strs
		else:
			_length = len(strs)
			if _length <=63:
				return strs

def TotalLength(strs):
	if strs is not None:
		_length = len(strs)
		if _length < 253:
			return strs


if __name__ == "__main__":
	main()
