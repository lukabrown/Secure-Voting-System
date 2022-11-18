import networkx as nx
import matplotlib.pyplot as plt
import csv


class Vote:
    # is this the array of vote options/candidates?
    # do we need to set a var for # of options
    votes = []
    INITIAL_TRUST = 1

    def __init__(self, voterNum, voterName,  voterTimeCast, voterParty, voterIPaddress, voterMACaddress, voterVerifNum, INITIAL_TRUST):
        self.DLnum = voterNum
        self.name = voterName
        self.timeCast = voterTimeCast
        self.party = voterParty
        self.IPaddress = voterIPaddress
        self.MACaddress = voterMACaddress
        self.verifNum = voterVerifNum
        self.trust = INITIAL_TRUST

# node types
# validVote = Vote(var_name[0])
#corruptedVote = Vote()
#corruptedVoteFromVote = Vote()

# functions


def runSim():
    pass


def printReport():
    pass


def initDirectedGraph():
    G = nx.DiGraph()
    # G.add_edges_from([('A', 'B'), ('A', 'C'), ('C', 'B'), ('D', 'A')])
    # pos = nx.spring_layout(G)
    # nx.draw_networkx_nodes(G, pos, node_size=500)
    # nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
    # nx.draw_networkx_labels(G, pos)
    # plt.show()
    voterPairs = []
    with open('Voter-Pairs.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1
                voter1 = row[0]
                voter2 = row[1]
                print(voter1, voter2)
                voterPairs.append((voter1, voter2))

    G.add_edges_from(voterPairs)
    # print(G.number_of_nodes())
    # pos = nx.planar_layouts(G)
    # nx.draw_networkx_nodes(G, pos)
    # nx.draw_networkx_edges(G, pos, edge_color='black')
    # nx.draw_networkx_labels(G, pos, font_color='white')
    # nx.draw_networkx_edge_labels(G, pos)
    nx.draw(G, with_labels=True)
    plt.show()


initDirectedGraph()
