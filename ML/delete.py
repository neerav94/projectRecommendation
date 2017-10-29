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

for i in range(100):
	for j in range(len(finalList)-1):
		for k in range((j+1),len(finalList)):
			v1, v2 = build_vector(finalList[j], finalList[k])
			var = (cosine(v1, v2))
			if var>0.5:
				temp=[]
				for m in finalList[j]:
					temp.append(m)
				for m in finalList[k]:
					temp.append(m)
				temp = Counter(temp)
				temp = sorted(temp.items(), key=operator.itemgetter(1))
				temp = temp[-8:]
				temp1 = []
				for m in range(len(temp)):
					for n in range(temp[m][1]):
						temp1.append(temp[m][0])
				finalList[k] = temp1[:]
				#temp=[]
				'''for m in range(len(finalList)):
					if m==j:
						continue
					temp.append(finalList[m])
				finalList=temp[:]'''
				finalList.remove(finalList[j])
				temp=[]
				for m in title[k]:
					temp.append(m)
				temp.append(title[j])
				title[j]=temp[:]
				#temp=[]
				for m in range(len(title)):
					if m==k:
						continue
					temp.append(title[m])
				title=temp[:]
				#title.remove(title[k])
				break
		if var>0.5:		
			break	
	print len(finalList)
count=0
for i in range(len(title)):		
	count+= len(title[i])
print "done"
print count
