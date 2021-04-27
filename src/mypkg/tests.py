from main import Graph
import math, random,scipy
import networkx as nx
import matplotlib.pyplot as plt
g = { "a" : ["d"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : []
    }

#inititialise a model connection
g={}
temp=""
for i in range(0,1000):
	temp=str(i)
	g[temp]=[]
for i in range(0,random.randint(3,5)):
	for i in g.values():
		i.append(str(random.randint(0,1000)))

"""
start the covid pandemic
0 for negative
1 for positive, asymptomatic
2 for positive and symptomatic
"""
pos=[0]*1000
for i in range(0,40):
	pos[random.randInt(0,1000)]=1
for i in range(0,60):
	pos[random.randInt(0,1000)]=2
	
	
"""
every 12 days, infect a new person
if a person is infected, all people connected to them will get infected with probability COVID, whether they are symptomatic or not
"""
def infect():
	pass
"""
every 12 days, deaths are updated
people die with probability death
dead people cannot transmit disease (set as -1 or remove from the graph?)
"""
def death():
	pass
graph = Graph(g)
print(graph)

for node in graph.vertices():
    print(graph.vertex_degree(node))

print("List of isolated vertices:")
print(graph.find_isolated_vertices())

print("""A path from "a" to "e":""")
print(graph.find_path("a", "e"))

print("""All pathes from "a" to "e":""")
print(graph.find_all_paths("a", "e"))

print("The maximum degree of the graph is:")
print(graph.Delta())

print("The minimum degree of the graph is:")
print(graph.delta())

print("Edges:")
print(graph.edges())

print("Degree Sequence: ")
ds = graph.degree_sequence()
print(ds)

fullfilling = [ [2, 2, 2, 2, 1, 1], 
                     [3, 3, 3, 3, 3, 3],
                     [3, 3, 2, 1, 1]
                   ] 
non_fullfilling = [ [4, 3, 2, 2, 2, 1, 1],
                    [6, 6, 5, 4, 4, 2, 1],
                    [3, 3, 3, 1] ]

for sequence in fullfilling + non_fullfilling :
    print(sequence, Graph.erdoes_gallai(sequence))

print("Add vertex 'z':")
graph.add_vertex("z")
print(graph)

print("Add edge ('x','y'): ")
graph.add_edge(('x', 'y'))
print(graph)

print("Add edge ('a','d'): ")
graph.add_edge(('a', 'd'))
print(graph)








#plot the initial network
trial=graph.edges()
trial2=[]
for i in range(0,len(trial)):
	trial2.append(tuple((trial[i])))
	if len(trial2[i])==1:
		trial2[i]=list(trial2[i])
		trial2[i]=tuple((trial2[i][0],trial2[i][0]))
print("/n/n/n/n\n\n\n")
print(trial2)
G=nx.Graph()
G.add_edges_from(trial2)
plt.subplot(121)
nx.draw(G,with_labels=True, font_weight='bold')
plt.show()

