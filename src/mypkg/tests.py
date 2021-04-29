from main import Graph
import math, random,scipy,sys,os
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import subprocess
subprocess.call('', shell=True)
from termcolor import colored
import colorama
colorama.init()
os.system('color')
#inititialise a model connection
pop = 100
g={}
temp=""
pos=[0]*pop
def init(social_distancing):
	global g, pop, temp, pos
	pos=[0]*pop
	for i in range(0,pop):
		temp=str(i)
		g[temp]=[]
	if social_distancing==True:
		x1,x2=0,2
	else:
		x1,x2=3,7
	for i in range(0,random.randint(x1,x2)):
		for i in g.values():
			i.append(str(random.randint(0,pop-1)))
	for i in range(0,4):
		pos[random.randint(0,pop-1)]=1
	for i in range(0,6):
		pos[random.randint(0,pop-1)]=2

"""
start the covid pandemic
0 for negative
1 for positive, asymptomatic
2 for positive and symptomatic
"""




x2=2

print(len(pos))
print(len(g))	
def drawnext():
	global color_map
	color_map=[]
	global pos,x2
	print(pos)
	for x in pos:
		if x==0:
			color_map.append("b")
		elif x==1:
			color_map.append("g")
		else:
			color_map.append("r")
	plt.subplot(2,3,x2)
	plt.title("At %i months" %(4*(x2-2)))
	x2+=1
	nx.draw(G, node_color=color_map,with_labels=False,font_weight='bold')

"""
every 12 days, infect a new person
if a person is infected, all people connected to them will get infected with probability COVID, whether they are symptomatic or not
"""
count1=[0]*50
count2=[0]*50
def infect(masking):
	global count1,count2
	if masking==True:
		prob=45731
	else:
		prob=76218
	for i in range(0,50):
		indices=[j for j,x in enumerate(pos) if (x==1 or x==2)]
		for j in indices:
			for k in list(g.values())[j]: #range(0,len(
				if(random.randint(0,1000000)<prob and pos[j]!=2):
					#g[str(j)][k]=1
					pos[int(k)]=1
				elif(random.randint(0,1000000)<prob and pos[j]!=1):
					#g[str(j)][k]=2
					pos[int(k)]=2
		for x in pos:
			if (x==1 or x==2):
				if masking==True:
					count1[i]+=1
				else:
					count2[i]+=1
	
		if(i%10==0):
			drawnext()
				
	
"""
every 12 days, deaths are updated
people die with probability death
dead people cannot transmit disease (set as -1 or remove from the graph?)
"""
def death():
	pass
	
	

#print(graph)



#plot the network
def fig():
	global g,G
	graph = Graph(g)
	trial=graph.edges()
	trial2=[]
	for i in range(0,len(trial)):
		trial2.append(tuple((trial[i])))
		if len(trial2[i])==1:
			trial2[i]=list(trial2[i])
			trial2[i]=tuple((trial2[i][0],trial2[i][0]))
	G=nx.Graph()
	G.add_edges_from(trial2)
	plt.subplot(2,3,1)
	plt.title("Control",loc='center')
	nx.draw(G,with_labels=False, font_weight='bold')


text1='Blue: Healthy\n'#colored('Blue: Healthy\n','blue')
text2='Green: Infected but Asymptomatic\n'#colored('Green: Infected but Asymptomatic\n','green')
text3='Red: Infected and Symptomatic'#colored('Red: Infected and Symptomatic','red')

init(False)
fig2=plt.figure()
fig2.suptitle("Network with no social distancing or masking")
fig2.text(0.02,0.02,("Population of %i \nLegend: \n" %pop +text1 +text2 +text3))
fig()
infect(False)



init(True)
fig2=plt.figure()
fig2.suptitle("Network with social distancing and masking")
fig2.text(0.02,0.02,("Population of %i \nLegend: \n" %pop +text1 +text2 +text3))
fig()
x2=2
infect(True)


fig3=plt.figure()
fig3.suptitle("Total number of infected people")
labels=['0 months','4 months', '8 months','12 months','16 months']
plt.plot(list(range(40)),count2[:40])
plt.plot(list(range(40)),count1[:40])
plt.xticks([0,10,20,30,40],labels)
plt.yticks([0,20,40,60,80,100],[0,int(0.2*pop),int(0.4*pop),int(0.6*pop),int(0.8*pop),pop])
plt.legend(['No social distancing or masking','Good social distancing and masking'])
plt.show()

