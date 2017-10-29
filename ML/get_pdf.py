import urllib2
#import slate
f1 = open("/home/neerav/recommender/link1.txt","r")
j=58
for i in f1:
	f = urllib2.urlopen(i)
	k = str(j)+".pdf"
	output = open(k,'wb')
	j+=1
	output.write(f.read())
	output.close()

print "done"
