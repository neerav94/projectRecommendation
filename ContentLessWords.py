#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import os
import re
from nltk.stem.porter import *
from collections import Counter

stemmer = PorterStemmer()
stopwords=[]
words_list=[]

path="/home/neerav/try"

f=open("stopwords.txt","rb")
patt="\r\n"
s=""
for line in f:
	s=(''.join(re.sub(patt,"",line)))
	stopwords.append(s)
def preprocessing(filename):
	patt="[A-Za-z]+"	
	f=open(filename,"r")
	temp0=[]
	temp=[]
	temp1=[]
	temp2=[]
	string=f.read()
	print string
	first="".join(re.sub("[,.<>!@$%^&*|()_+-=?/;:/#'{}~`]","",string))
	text = ' '.join([word for word in first.split() if word not in stopwords])
	temp=text.split()
	for word in temp:
		if re.match(patt,word):
			temp1.append(word.lower())
	#print len(temp1)ss
	#temp2 = [stemmer.stem(word) for word in temp1]
	#print len(temp2)	
	words_list.extend(temp1)

for filename in glob.glob(os.path.join(path, '*.txt')):
	preprocessing(filename)

wordFrequency = Counter(words_list)
print wordFrequency
print "TOTAL WORDS",len(words_list)
