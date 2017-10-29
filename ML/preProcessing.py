#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator
from pattern.en import pluralize
import re
from collections import Counter
import glob, os
import math
import json
import pickle

l=[]
words=[]
temp=[]
finalList=[]
#For stopwords
f2 = open("/home/neerav/recommender/stopwords.txt","r")

stopwords=[]
for i in f2:
	i = re.sub("\r\n","",i)
	stopwords.append(i)

titles=[]
f = open("/home/neerav/recommender/ML/ml_title","r")
for line in f:
	temp=[]
	line = re.sub("\n","",line)
	temp.append(line)
	titles.append(temp)

#for the text file
#os.chdir("/home/neerav/recommender/CS229_2015/paper")
#for file in glob.glob("*.txt"):
for i in range(1,531):
    	#if file.endswith(".txt"):
	i=str(i)
	j="/home/neerav/recommender/ML/ML/"+i+".txt"
        f = open(j,"r")
	doc = f.read()
	doc = doc.lower()
	l=doc.split(" ")
	l = map(lambda s: s.strip(), l)
	words=[]
	temp=[]
	temp1=[]
	for i in l:
		i = re.sub("\n","",i)
		i = re.sub("[,.<>!@$%^&*|()_+-/=?/;:/#'{}~`\]\[]''","",i)
		j = re.match("[a-zA-Z]*",i)
		if j:
			temp.append(j.group(0))

	for i in temp:
		if i not in stopwords:
			if len(i)>3:
				words.append(i)

	plural_words_list=[]
	for word in words:
		plural_words_list.append(pluralize(word))

	text1 = ' '.join([word for word in words if word not in plural_words_list])
	wordFrequency = Counter(text1.split())

	wordList = sorted(wordFrequency.items(), key=operator.itemgetter(1))
	#print wordList
	#----------------------------------------------------------------------------------------------------------------------------
	#pre_processing over
	#----------------------------------------------------------------------------------------------------------------------------
	length = len(wordList)
	wordList=wordList[(length-8):]
	#print wordList[0]
	#finalList.append(wordList)
	for i in range(len(wordList)):
		for j in range(wordList[i][1]):
			temp1.append(wordList[i][0])
	#temp1.append(titles[count])
	finalList.append(temp1)

f1 = open('data', 'w')
pickle.dump(finalList, f1)
f1.close()

f2 = open('title','w')
pickle.dump(titles,f2)
f2.close()

print "Preprocessing done!!"
print len(finalList)
print len(titles)
