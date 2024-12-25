from pathlib import Path

import networkx as nx


with ((Path(__file__).parent.parent.parent) / "data" / "23.in").open() as f:
    edges = [line.split("-") for line in f.read().strip().splitlines()]

G = nx.Graph(edges)
cliques: list[list[str]] = list(nx.enumerate_all_cliques(G))

p1 = (
    sum(
        len(clique) == 3 and any(member.startswith("t") for member in clique)
        for clique in cliques
    )
)
print(p1)

key = max(cliques, key=list.__len__)
p2 = ",".join(sorted(key))
print(p2)
