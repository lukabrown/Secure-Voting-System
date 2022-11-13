import networkx as nx
import matplotlib.pyplot as plt


class Vote:
    # is this the array of vote options/candidates?
    # do we need to set a var for # of options
    votes = []
    INITIAL_TRUST = 1

    def __init__(self, voterName, voterDLnum, voterTimeCast, voterParty, voterIPaddress, voterMACaddress, voterVerifNum, INITIAL_TRUST):
        self.name = voterName
        self.DLnum = voterDLnum
        self.timeCast = voterTimeCast
        self.party = voterParty
        self.IPaddress = voterIPaddress
        self.MACaddress = voterMACaddress
        self.verifNum = voterVerifNum
        self.trust = INITIAL_TRUST


# node types
#validVote = Vote()
#corruptedVote = Vote()
#corruptedVoteFromVote = Vote()

# functions


def runSim():
    pass


def printReport():
    pass


def init():
    pass


G = nx.DiGraph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('C', 'B')])
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
nx.draw_networkx_labels(G, pos)
plt.show()
