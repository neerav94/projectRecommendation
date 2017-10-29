import math
import json
from collections import Counter
import operator

f=open("data.txt","r")
finalList=json.load(f)

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

title=[]
for i in range(len(finalList)):
	#length = len(finalList[i])
	#length=length-1
	temp_title=[]
	temp_title.append(finalList[i][-1])	
	title.append(temp_title)

temp3=[]
for i in range(len(finalList)):
	temp3.append(finalList[i][:-1])
	#finalList=finalList[i][:-1]
finalList=temp3[:]
t1=[]
t2=[]
temp4=title[:]
count1=0

for k in range(500):
	for i in range(len(finalList)-1):
		temp=[]
		for j in range((i+1),len(finalList)):
			if i==j:
				continue
			v1, v2 = build_vector(finalList[i], finalList[j])
			var = (cosine(v1, v2))
			if var>0.5:
				count1+=1
				temp1=[]
				#if count==1:
				for m in finalList[i]:
					temp.append(m)
				#count+=1
				#temp1=temp[:]
				for m in finalList[j]:
					temp.append(m)
				wordFrequency = Counter(temp)
				wordList = sorted(wordFrequency.items(), key=operator.itemgetter(1))
				wordList=wordList[-8:]
				temp1=[]
				for i in range(len(wordList)):
					for k in range(wordList[i][1]):
						temp1.append(wordList[i][0])

				finalList[j]=temp1[:]
				count=0			
				for m in title[j]:
					count+=1
					title[i].append(m)
					if count==15:
						break
				temp=[]
				for m in range(len(title)):
					if m==j:
						continue
					temp.append(title[m])
				title=temp[:]		
				#title.remove(title[i])
				temp=[]
				for m in range(len(finalList)):
					if m==i:
						continue
					temp.append(finalList[m])
				finalList=temp[:]
				break
		if var>0.5:
			break
	#finalList=finalList[:]
	#title=title[:]
	print len(finalList)
	#print len(title)
count11=0
for i in range(len(title)):
	count11 += len(title[i])
	final = Counter(finalList[i])
	print final
	#print title[i]
#print count11
#print count1
