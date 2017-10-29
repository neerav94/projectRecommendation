import pickle
import math
import json
from collections import Counter
import operator

def build_vector(iterable1, iterable2):
    counter1 = Counter(iterable1)
    counter2 = Counter(iterable2)
    all_items = set(counter1.keys()).union(set(counter2.keys()))
    vector1 = [counter1[k] for k in all_items]
    vector2 = [counter2[k] for k in all_items]
    return vector1, vector2

def cosine(v1, v2):
    dot_product = sum(n1 * n2 for n1, n2 in zip(v1, v2) )
    magnitude1 = math.sqrt(sum(n ** 2 for n in v1))
    magnitude2 = math.sqrt(sum(n ** 2 for n in v2))
    if magnitude1==0 or magnitude2==0:
	return 0
    return dot_product / (magnitude1 * magnitude2)

f1=open("data","r")
f2=open("title","r")
finalList=pickle.load(f1)
title=pickle.load(f2)
f1.close()
f2.close()

for i in range(200):
	for j in range(len(finalList)-1):
		for k in range((j+1),len(finalList)):
			flag=False
			if k<=j:
				continue
			v1, v2 = build_vector(finalList[j], finalList[k])
			var = (cosine(v1, v2))
			if var>0.5:
				temp=[]
				for m in finalList[j]:
					temp.append(m)
				for m in finalList[k]:
					temp.append(m)

				wordFrequency = Counter(temp)
				wordList = sorted(wordFrequency.items(), key=operator.itemgetter(1))
				length = len(wordList)
				wordList=wordList[(length-8):]
				temp1=[]
				for q in range(len(wordList)):
					for n in range(wordList[q][1]):
						temp1.append(wordList[q][0])

				finalList[j]=temp1[:]
				del finalList[k]

				if len(title[k])==1:
					title[j].append(title[k][0])
				else:
					for m in title[k]:
						title[j].append(m)
				del title[k]
				flag=True
				break
		if(flag):
			break
	print len(finalList)
count=0
for i in range(len(title)):
	count += len(title[i])
	#final = Counter(finalList[i])
	#print final
	#print title[i]
print count
