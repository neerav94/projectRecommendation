from scipy import spatial
import pickle,numpy
f2=open("user_vectors","r")

projects = ['Machine Learning','Image Processing','IOT','Computer Security','Big-Data','Android-Development','Cloud Computing']
no_of_papers=[248,67,57,92,97,69,99]

pickle_names=[["ml_weights","ml_paper_weights"],["IP_weights","IP_paper_weights"],["IOT_weights","IOT_paper_weights"],["CS_weights","CS_paper_weights"],["BD_weights","BD_paper_weights"],["AD_weights","AD_paper_weights"],["CC_weights","CC_paper_weights"]]
	

'''for i in range(10):                                                user-user
	if user_vec[i]!=0:
		f=open(pickle_names[i][0],"r")
		f1=open(pickle_names[i][1],"r")
		users[i].append(all_vectors[0])'''
c=0
dic={}

for i in range(1):
	gui=[[],[],[],[],[],[],[]]
	val=0
	domains=[]	
	all_vectors=pickle.load(f2)
	user_vec=all_vectors[1]
	indices=[]
	flag=True
	for i in range(7):
		if(user_vec)!=[]:

			if user_vec[i]!=float(0):
				domains.append(projects[i])
				indices.append(i)
			c+=1
	if dic.keys()!=[]:
		if all_vectors[0] in dic.keys():
			dic[all_vectors[0]]=domains
		else:
			dic[all_vectors[0]]=domains
	elif dic.keys()==[]:
		dic[all_vectors[0]]=domains


	for i in indices:
		res=[]
		f=open(pickle_names[i][0],"r")
		f1=open(pickle_names[i][1],"r")
		domain_weights=pickle.load(f)
		domain_user_vec=[a*b for a,b in zip(domain_weights,user_vec)]

		for i in range(50):
			vec=pickle.load(f1)
			paper_vec=vec[1]
			#print vec
			if paper_vec==[]:
				continue
			a=numpy.array(paper_vec[:7])
			b=numpy.transpose(a).tolist()
			#print domain_user_vec,b
			if len(b)!=7:
				continue
			result = 1 - spatial.distance.cosine(domain_user_vec,b)
			res.append([result,vec[0]])
		f.close()
		f1.close()
		res.sort()
		#print domains[val]
		ll=[]	
		for i in res[::-1][:10]: 
			ll.append(i[1])
		final_res= list(set(ll))
		#for i in range(len(final_res)):
			#print final_res[i]
		domain_projects=[]
		gui[val].append(domains[val])
		gui[val].append(final_res)
		#gui[val].append(domain_projects)
		#print val
		c=0
		match=[]
		val+=1
		
		if flag==True:
			if dic.keys()!=[]:
				for i in dic.keys():
					#print dic
					c+=len(set(domains)&set(dic[i]))
					cent=(float(c)/float(7))*100
					match.append([cent,i])
					#print match
					c=0
			match.sort()
			user_res=[]		
			for i in match[::-1][:10]: 
				user_res.append(i[1])
			flag==False
	print gui	
	print user_res
		
