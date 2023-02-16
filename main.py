import osmnx as ox  # https://osmnx.readthedocs.io/en/stable/
import networkx as nx  # https://networkx.org/

G = ox.load_graphml("./data/madison_wisconsin.graphml")

edge_centrality = nx.closeness_centrality(nx.line_graph(G))
nx.set_edge_attributes(G, edge_centrality, "edge_centrality")

ec = ox.plot.get_edge_colors_by_attr(G, "edge_centrality", cmap="inferno")
fig, ax = ox.plot_graph(G, edge_color=ec, edge_linewidth=2, node_size=0)

ox.plot_graph(G)
