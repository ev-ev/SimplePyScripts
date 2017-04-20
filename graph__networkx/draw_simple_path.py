#!/usr/bin/env python

# SOURCE: https://networkx.readthedocs.io/en/stable/examples/drawing/simple_path.html

"""
Draw a graph with matplotlib.
You must have matplotlib for this to work.

"""

import matplotlib.pyplot as plt
import networkx as nx

G = nx.path_graph(8)
nx.draw(G)
plt.savefig("simple_path.png")  # save as png
plt.show()  # display
