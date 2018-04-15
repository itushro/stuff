import networkx as nx
import numpy as np
import sys

from time import time
from random import random,randrange,choice

sys.setrecursionlimit(1000000)

def random_surfer(G,d,k):
    v = {node:0 for node in G.nodes()}
    n = nx.number_of_nodes(G)
    i = k*n
    node = str(randrange(n))
    v[node] += 1
    start = time()
    t = 0
    while i > 0:
        if (time() - start) > 1.618*t:
            print(" {:.2f} percent done.".format(100-100*i/(k*n)),end="\r")
            t += 1
        i -= 1
        neigh = [i for i in G.neighbors(node)]
        if neigh and d < random():
            node = str(choice(neigh))
            v[node] += 1
        else:
            node = str(randrange(n))
            v[node] += 1
    return v

def calc_a(G):
    A = np.transpose(nx.to_numpy_matrix(G))
    A /= np.sum(A,axis=0)
    A = np.nan_to_num(A)
    return A

def calc_d(A):
    D = np.zeros(A.shape)
    for i in range(len(A)):
        if A[:,i].sum() == 0:
            D[:,i] = 1/len(A)
    return D

def calc_s(D):
    S = np.zeros(np.shape(D))
    S.fill(1/nx.number_of_nodes(G))
    return S

def calc_x(x,k,m,G):
    A = calc_a(G)
    D = calc_d(A)
    S = calc_s(D)
    i = 0
    return _calc(x,k,m,A,D,S,i)

def _calc(x,k,m,A,D,S,i):
    if 0 < (i % 3.141) < 1:
        print(" {:.2f} percent done.".format(100*i/k),end="\r")
    if i == k:
        return x
    else:
        x = (1-m)*np.dot(A,x)+(1-m)*np.dot(D,x)+m*np.dot(S,x)
        i += 1
        return _calc(x,k,m,A,D,S,i)

# load graph
infile = open("data/gnutella.txt","rb")
G = nx.read_adjlist(infile,create_using=nx.DiGraph())
infile.close()

# define parameters
approx = 1000
damping = 0.15

# calculate eigenvector
x = np.transpose(np.matrix([1/nx.number_of_nodes(G)]*nx.number_of_nodes(G)))
x = calc_x(x,approx,damping,G)

# order by ranking
ranks = list()
for node in reversed(np.argsort(x,axis=0)):
    idx = node.item()
    ranks.append((list(G.nodes)[idx],x[idx].item()))
message = str()
message = message.join("Rank: {:.4f}\t Node: {}\n".format(rank[1],rank[0]) for rank in ranks[:10])
print("\nPageRank:\n" + message)

# random surfer simulation
visits = random_surfer(G,damping,approx)
visits = sorted(visits.items(),key=lambda x: x[1],reverse=True)
message = str()
message = message.join("Visits: {}\t Node: {}\n".format(visit[1],visit[0]) for visit in visits[:10])
print("Random surfer:\n" + message)



