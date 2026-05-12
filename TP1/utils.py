import numpy as np
import networkx as nx
import pickle

#Funciones para cargar grafos en archivos .txt
def read_graph(filename):
    G = nx.Graph()
    array = np.loadtxt(filename, dtype=int)
    G.add_edges_from(array)
    return G

def read_graph_weighted(filename):
    G = nx.Graph()
    array = np.loadtxt(filename, dtype=int)
    G.add_weighted_edges_from(array)
    return G

def read_dir_graph(filename):
    G = nx.DiGraph()
    array = np.loadtxt(filename, dtype=int)
    G.add_edges_from(array)
    return G

def read_dir_graph_weighted(filename):
    G = nx.DiGraph()
    array = np.loadtxt(filename, dtype=int)
    G.add_weighted_edges_from(array)
    return G

#Función para cargar información posicional de un archivo pickle
def get_graph_pos(filename):
  with open(filename, 'rb') as f:
    posData = pickle.load(f)
  return posData

#Función para graficar un grafo con pesos
def plotWeightedGraph(G, pos, magnification):
  edge_weights = nx.get_edge_attributes(G, "weight")
  edgeWidths = np.array(list(edge_weights.values()))
  edgeWidths = magnification * edgeWidths / np.max(edgeWidths)
  edgeWidths[edgeWidths > 0] = edgeWidths[edgeWidths > 0] - np.min(edgeWidths[edgeWidths > 0]) + .5
  nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=edgeWidths, edge_color='gray', alpha=0.3)

#Función para graficar un grafo con pesos en los nodos
def plotNodeAttribute(G, pos, attribute, exaggeration):
  values = [attribute[n] for n in G.nodes()]
  nsize = np.array (values)
  nsize = exaggeration*( nsize - min(nsize))/(max(nsize) - min(nsize))
  nx.draw(G, pos=pos, node_size = nsize, alpha=0.4,node_color = values, edge_color='gray')