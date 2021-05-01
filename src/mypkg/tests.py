from main import Graph
import math, random,scipy,sys,os,time
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
time1=time.perf_counter()

#future stuff
import subprocess
subprocess.call('', shell=True)
from termcolor import colored
import colorama
colorama.init()
os.system('color')


#inititialise a model connection
pop = 10000
prev=[]
g={}
temp=""
pos=[0]*pop
def init(social_distancing):
	global g, pop, temp, pos, prev
	pos=[0]*pop
	prev=[0]*pop
	for i in range(0,pop):
		temp=str(i)
		g[temp]=[]
	if social_distancing==True:
		x1,x2=5,10
	else:
		x1,x2=10,20
	for i in range(0,random.randint(x1,x2)):
		for i in g.values():
			i.append(str(random.randint(0,pop-1)))
	for i in range(0,40):
		pos[random.randint(0,pop-1)]=1
	for i in range(0,60):
		pos[random.randint(0,pop-1)]=2

"""
start the covid pandemic
0 for negative
1 for positive, asymptomatic
2 for positive and symptomatic
"""




x2=2

#print(len(pos))
#print(len(g))	
def drawnext():
	global color_map
	color_map=[]
	global pos,x2
	#print(pos)
	for x in pos:
		if x==0:
			color_map.append("b")
		elif x==1:
			color_map.append("g")
		elif x==2:
			color_map.append("r")
		elif x==3:
			color_map.append("black")
		elif x==4:
			color_map.append('pink')
	plt.subplot(2,3,x2)
	plt.title("At %i months" %(4*(x2-2)))
	x2+=1
	nx.draw(G, node_color=color_map,with_labels=False,font_weight='bold')

"""
every 12 days, infect a new person
if a person is infected, all people connected to them will get infected with probability COVID, whether they are symptomatic or not
people die with probability probd
dead people cannot transmit disease (set as 3)
0: uninfected
1: infected asymptomatic
2: infected symptomatic
3: dead
4: recovered and immune
#https://coronavirus.jhu.edu/data/mortality
"""
count1=[0]*50 #number of cases in a masked society
count2=[0]*50 #number of cases in a maskless society
count3=[0]*50 #deaths in a masked society
count4=[0]*50 #deaths in a maskless society
def infect(masking):
	global count1,count2,count3,count4
	count=0
	probd=25
	if masking==True:
		probinf=45731
	else:
		probinf=76218
	for i in range(0,50): #counter
		indices=[j for j,x in enumerate(pos) if (x==1 or x==2)] #gives the source people who are positive
		for j in indices: #for all these people,
			for k in list(g.values())[j]: #for every list of connected people to the source person(j), take individually (k),
				if(random.randint(0,1000000)<probinf and (pos[int(k)]!=2 and pos[int(k)]!=3 and pos[int(k)]!=4)): #probability of getting infected asymp
					#g[str(j)][k]=1
					pos[int(k)]=1
				elif(random.randint(0,1000000)<probinf and (pos[int(k)]!=1 and pos[int(k)]!=3 and pos[int(k)]!=4)): #probability of getting infected symp
					#g[str(j)][k]=2
					pos[int(k)]=2
			#trial 
			if((prev[j]==1 or prev[j]==2)): #if the source person was infected previously
				if(random.randint(0,1000)<probd): #they may die
					pos[j]=3
				else: #or they may recover
					pos[j]=4
			elif(prev[j]==0): #or prev[j]==3 or prev[j]==4): #if they were healthy, dead or recovered
				if(pos[j]==1 or pos[j]==2): #if they are currently infected
					prev[j]=pos[j]
			elif(prev[j]==3):
				pos[j]=3
			elif(prev[j]==4):
				pos[j]=4
					
				#if(prev[i]==1 or prev[i]==2):
				#	pos[
		for x in pos:
			if (x==1 or x==2 or x==3 or x==4):
				if masking==True:
					count1[i]+=1
				else:
					count2[i]+=1
			if x==3:
				count+=1				
			if masking==True:
				count3[i]=count
			else:
				count4[i]=count
		count=0
		if(i%10==0):
			drawnext()

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
text3='Red: Infected and Symptomatic\n'#colored('Red: Infected and Symptomatic','red')
text4='Black: Deaths\nPink: Recovered'

init(False)
fig2=plt.figure()
fig2.suptitle("Network with no social distancing or masking")
fig2.text(0.02,0.02,("Population of %i \nLegend: \n" %pop +text1 +text2 +text3+text4))
fig()
infect(False)
print("Total number of infected cases after no social distancing or masking: %i" %count2[-1])
print("Total number of deaths after no social distancing or masking: %i"  %count4[-1])
print("Infection rate with no social distancing or masking: %.02f" %((count2[-1]/pop)*100)+"%")
print("Mortality rate with no social distancing or masking: %.02f" %((count4[-1]/pop)*100)+"%")


init(True)
fig2=plt.figure()
fig2.suptitle("Network with social distancing and masking")
fig2.text(0.02,0.02,("Population of %i \nLegend: \n" %pop +text1 +text2 +text3+text4))
fig()
x2=2
infect(True)

print("Total number of infected cases after social distancing and masking: %i"  %count1[-1])
print("Total number of deaths after social distancing and masking: %i" %count3[-1])
print("Infection rate with social distancing and masking: %.02f" %((count1[-1]/pop)*100)+"%")
print("Mortality rate with social distancing and masking: %.02f" %((count3[-1]/pop)*100)+"%")


fig3=plt.figure()
fig3.suptitle("Total number of cases and deaths")
labels=['0 months','4 months', '8 months','12 months','16 months']
plt.plot(list(range(40)),count1[:40])
plt.plot(list(range(40)),count2[:40])
plt.plot(list(range(40)),count3[:40])
plt.plot(list(range(40)),count4[:40])
plt.xticks([0,10,20,30,40],labels)
#plt.yticks([0,20,40,60,80,100],[0,int(0.2*pop),int(0.4*pop),int(0.6*pop),int(0.8*pop),pop])
plt.legend(['Cases after good social distancing and masking','Cases after no social distancing or masking','Deaths after social distancing and masking','Deaths with no social distancing or masking'])

fig4=plt.figure()
fig4.suptitle("Increase in cases and deaths")
count11,count21,count31,count41=[0]*40,[0]*40,[0]*40,[0]*40
for i in range(1,40):
	count11[i]=count1[i]-count1[i-1]
	count21[i]=count2[i]-count2[i-1]
	count31[i]=count3[i]-count3[i-1]
	count41[i]=count4[i]-count4[i-1]
plt.plot(list(range(40)),count11[:40])
plt.plot(list(range(40)),count21[:40])
plt.plot(list(range(40)),count31[:40])
plt.plot(list(range(40)),count41[:40])
plt.xticks([0,10,20,30,40],labels)
#plt.yticks([0,20,40,60,80,100],[0,int(0.2*pop),int(0.4*pop),int(0.6*pop),int(0.8*pop),pop])
plt.legend(['Cases after good social distancing and masking','Cases after no social distancing or masking','Deaths after social distancing and masking','Deaths with no social distancing or masking'])
time2=time.perf_counter()
print("Time taken for simulating %i population: " %pop +str(time2-time1)+" seconds")
#print(count3)
#print(count4)
plt.show()

