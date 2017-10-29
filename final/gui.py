from Tkinter import *
import tkMessageBox
import math
from scipy import spatial
import pickle,numpy

top = Tk()
f1=open("saved_users","r")
top.geometry("400x300")
top.title("Input")
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
val1=0
val2=0
val3=0
val4=0
val5=0
val6=0
val7=0
li=[0,0,0,0,0,0,0]
temp=0
tkMessageBox.showinfo( "Recomendation System for Projects", "Collection of Student Interest on Projects. Student Should give response as 1,-1 or 0 based on if they like, dislike or can't decide based on provided information.")
def sel1():
	val1 = var1.get()
	if val1==1:
		li[0]=1
	if val1 == -1:
		li[0]=-1
	
def sel2():
	val2 = var2.get()
	if val2==1:
		li[1] = 1
	if val2 == -1:
		li[1]=-1

def sel3():
	val3 = var3.get()
	if val3==1:
		li[2]=1
	if val3 == -1:
		li[2]=-1
	
def sel4():
	val4 = var4.get()
	if val4==1:
		li[3]=1
	if val4 == -1:
		li[3]=-1

def sel5():
	val5 = var5.get()
	if val5==1:
		li[4]=1
	if val5 == -1:
		li[4]=-1

def sel6():
	val6 = var6.get()
	if val6 == 1:
		li[5]=1
	if val6 == -1:
		li[5]=-1

def sel7():
	val7 = var7.get()
	if val7 == 1:
		li[6]=1
	if val7 == -1:
		li[6]=-1

def sub1():
	if li[0]==1:
		root = Tk()
		root.title("Machine Learning")
		text1 = Text(root)
		for i in gui[0][1]:
			text1.insert(INSERT, i)
			text1.insert(INSERT, "\n")
		text1.grid(row=0, column=0)

		'''text2 = Text(root)
		text2.insert(INSERT, "USERS\n")
		text2.insert(INSERT, "Hello.....\n")
		text2.insert(END, li)
		text2.grid(row=0, column=1)'''
	
		B2 = Button(root, text ="Next", command = sub2).grid(row=2, column=0, rowspan=10)
		root.mainloop()

	else:
		sub2()

def sub2():
	if li[1]==1:
		root1 = Tk()
		root1.title("Image Processing")
		text3 = Text(root1)
		for i in gui[1][1]:
			text3.insert(INSERT, i)
			text3.insert(INSERT, "\n")
		text3.grid(row=0, column=0)
	
		B3 = Button(root1, text ="Next", command = sub3).grid(row=2, column=0, rowspan=10)
	
		root1.mainloop()
	else:
		sub3()
		
def sub3():
	if li[2]==1:
		root2=Tk()
		root2.title("Internet of Things")
		text5 = Text(root2)
		for i in gui[2][1]:
			text5.insert(INSERT, i)
			text5.insert(INSERT, "\n")
		text5.grid(row=0, column=0)
	
		B4 = Button(root2, text ="Next", command = sub4).grid(row=2, column=0, rowspan=10)

		root2.mainloop()
	else:
		sub4()

def sub4():
	if li[3]==1:
		root3= Tk()
		root3.title("Security")
		text7 = Text(root3)
		for i in gui[3][1]:
			text7.insert(INSERT, i)
			text7.insert(INSERT, "\n")
		text7.grid(row=0, column=0)

		B5 = Button(root3, text ="Next", command = sub5).grid(row=2, column=0, rowspan=10)
	
		root3.mainloop()
	else:
		sub5()

def sub5():
	if li[4]==1:
		root4 = Tk()
		root4.title("Big Data")
		text9 = Text(root4)
		for i in gui[4][1]:
			text9.insert(INSERT, i)
			text9.insert(INSERT, "\n")
		text9.grid(row=0, column=0)
	
		B6 = Button(root4 , text ="Next", command = sub6).grid(row=2, column=0, rowspan=10)

		root4.mainloop()
	else:
		sub6()

def sub6():
	if li[5]==1:
		root5 = Tk()
		root5.title("Android Development")
		text11 = Text(root5)
		for i in gui[5][1]:
			text11.insert(INSERT, i)
			text11.insert(INSERT, "\n")
		text11.grid(row=0, column=0)

		B7 = Button(root5, text ="Next", command = sub7).grid(row=2, column=0, rowspan=10)

		root5.mainloop()
	else:
		sub7()

def sub7():
	if li[6]==1:
		root6 = Tk()
		root6.title("Cloud Computing")
		text13 = Text(root6)
		for i in gui[6][1]:
			text13.insert(INSERT, i)
			text13.insert(INSERT, "\n")
		text13.grid(row=0, column=0)
	
		B8 = Button(root6, text ="Next", command=sub8).grid(row=2, column=0, rowspan=10)
		root6.mainloop()
	else:
		sub8()

def sub8():
	root7=Tk()
	root7.title("Users")
	text15 = Text(root7)
	for i in user_res:
		if i==name:
			continue
		text15.insert(INSERT, i)
		text15.insert(INSERT,"\n")
	text15.grid(row=0, column=1)

def sub():
	top.destroy()
def user_list():
	return li
def user_name():
	return v1.get()

v1 = StringVar()

L9 = Label(top, text="Please tick your interests").grid(row=2, column=0, rowspan=4)

L8 = Label(top, text="Name: ").grid(row=6, column=0)
E1 = Entry(top, textvariable = v1).grid(row=6, column=1, columnspan=4)

L1 = Label(top, text="Machine Learning").grid(row=10, column=0, rowspan=4)
R1 = Radiobutton(top, text="-1", variable=var1, value=-1, command=sel1).grid(row=10, column=1, rowspan=4, columnspan=2)
R2 = Radiobutton(top, text="0", variable=var1, value=0, command=sel1).grid(row=10, column=3, rowspan=4, columnspan=2)
R3 = Radiobutton(top, text="1", variable=var1, value=1, command=sel1).grid(row=10, column=5, rowspan=4, columnspan=2)

L2 = Label(top, text="Image Processing").grid(row=15, column=0, rowspan=4)
R4 = Radiobutton(top, text="-1", variable=var2, value=-1, command=sel2).grid(row=15, column=1, rowspan=4, columnspan=2)
R5 = Radiobutton(top, text="0", variable=var2, value=0, command=sel2).grid(row=15, column=3, rowspan=4, columnspan=2)
R6 = Radiobutton(top, text="1", variable=var2, value=1, command=sel2).grid(row=15, column=5, rowspan=4, columnspan=2)

L3 = Label(top, text="IoT").grid(row=20, column=0, rowspan=4)
R7 = Radiobutton(top, text="-1", variable=var3, value=-1, command=sel3).grid(row=20, column=1, rowspan=4, columnspan=2)
R8 = Radiobutton(top, text="0", variable=var3, value=0, command=sel3).grid(row=20, column=3, rowspan=4, columnspan=2)
R9 = Radiobutton(top, text="1", variable=var3, value=1, command=sel3).grid(row=20, column=5, rowspan=4, columnspan=2)

L4 = Label(top, text="Security").grid(row=25, column=0, rowspan=4)
R10 = Radiobutton(top, text="-1", variable=var4, value=-1, command=sel4).grid(row=25, column=1, rowspan=4, columnspan=2)
R11 = Radiobutton(top, text="0", variable=var4, value=0, command=sel4).grid(row=25, column=3, rowspan=4, columnspan=2)
R12 = Radiobutton(top, text="1", variable=var4, value=1, command=sel4).grid(row=25, column=5, rowspan=4, columnspan=2)

L5 = Label(top, text="Big Data").grid(row=30, column=0, rowspan=4)
R13 = Radiobutton(top, text="-1", variable=var5, value=-1, command=sel5).grid(row=30, column=1, rowspan=4, columnspan=2)
R14 = Radiobutton(top, text="0", variable=var5, value=0, command=sel5).grid(row=30, column=3, rowspan=4, columnspan=2)
R15 = Radiobutton(top, text="1", variable=var5, value=1, command=sel5).grid(row=30, column=5, rowspan=4, columnspan=2)

L6 = Label(top, text="Android Development").grid(row=35, column=0, rowspan=4)
R16 = Radiobutton(top, text="-1", variable=var6, value=-1, command=sel6).grid(row=35, column=1, rowspan=4, columnspan=2)
R17 = Radiobutton(top, text="0", variable=var6, value=0, command=sel6).grid(row=35, column=3, rowspan=4, columnspan=2)
R18 = Radiobutton(top, text="1", variable=var6, value=1, command=sel6).grid(row=35, column=5, rowspan=4, columnspan=2)

L7 = Label(top, text="Cloud Computing").grid(row=40, column=0, rowspan=4)
R19 = Radiobutton(top, text="-1", variable=var7, value=-1, command=sel7).grid(row=40, column=1, rowspan=4, columnspan=2)
R20 = Radiobutton(top, text="0", variable=var7, value=0, command=sel7).grid(row=40, column=3, rowspan=4, columnspan=2)
R21 = Radiobutton(top, text="1", variable=var7, value=1, command=sel7).grid(row=40, column=5, rowspan=4, columnspan=2)

B1 = Button(top, text ="Submit", command = sub).grid(row=50, column=5, rowspan=10)
top.mainloop()


def user_profile_vectors(user_data,user_name):
    projects = ['Machine Learning','Image Processing','IOT','Security','Big data','Android-Development','Cloud Computing']
    count = 0
    temp_val = 0
    vector = []
    normalized_attribute = 0
    for i in range(len(user_data)):
        if user_data[i] == 1:
            count+=1

                
    normalized_attribute = count
    
    for j in range(len(projects)):
        if user_data[j] in [1,0,-1]:
            if normalized_attribute!=0:
                temp_val = user_data[j]/math.sqrt(normalized_attribute)
                vector.append(temp_val)
            else:
                vector.append(user_data[j])  

    for i in range(len(vector)):
           f = open("C:\Python34\user-profiles.txt","a")
           f.write("\n")
           f.write(str(vector[i])+",")
           f.flush();      
    f.write(user_name)
    f.flush() 
    f.write("\n")   

    return vector 


vec = user_list()
name = user_name()
vectors = user_profile_vectors(vec,name)
#print('Name of the student : ',name)
#print(vectors)
#print type(vectors)

user_vector = [0,0]
user_vector[0]=name
user_vector[1]=vectors
#project=["nee","asfd","asdfc"]
#print user_vector


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
dic=pickle.load(f1)

for i in range(1):
	gui=[[],[],[],[],[],[],[]]
	val=0
	domains=[]
	all_vectors = user_vector	
	#all_vectors=pickle.load(f2)
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


	for values in indices:
		res=[]
		f=open(pickle_names[values][0],"r")
		f1=open(pickle_names[values][1],"r")
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
		gui[values].append(domains[val])
		gui[values].append(final_res)
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
	#print gui	
	#print user_res

sub1()

