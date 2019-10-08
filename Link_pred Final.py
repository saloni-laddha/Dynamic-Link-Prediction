
import matplotlib.pyplot as plt
import networkx as nx


G=nx.Graph()
init_links=[]


def initiate():
    #converting text to list of edges
    edge_list=[]
    f=open("example.txt","r")
    for line in f:
        spl=line.split()
        spl = [int(i) for i in spl]
        edge_list.append(spl)
    for i in range(len(edge_list)):
	G.add_edge(edge_list[i][0],edge_list[i][1])

initiate()

nx.draw(G,with_labels=True)
plt.show()


betCent=nx.betweenness_centrality(G,normalized=True,endpoints=True)
sorted(betCent, key=betCent.get, reverse=True)[:5]


eigenCent=nx.eigenvector_centrality(G,max_iter=1000)
sorted(eigenCent,key=eigenCent.get,reverse=True)[:5]


degCent=nx.degree_centrality(G)
sorted(degCent,key=degCent.get,reverse=True)[:5]

