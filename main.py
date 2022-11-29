import random
import string

party_options = ["democrat", "republican", "libertarian", "undecided"]
electees = {
    "Democrats": "Johnnie Fortier",
    "Republicans": "Steven Griffith",
    "Libertarians": "Patricia Cooke",
    "Undecided": "Sean Thomas",
}

#creates trivial names to replace the names module creating a realistic full name
names = ["" for x in range(100)]
for i in range(100):
  names[i] = names[i] + random.choice(string.ascii_uppercase)
  names[i] = names[i] + random.choice(string.ascii_lowercase)
  names[i] = names[i] + random.choice(string.ascii_lowercase)
  names[i] = names[i] + random.choice(string.ascii_lowercase)
  names[i] = names[i] + random.choice(string.ascii_lowercase)
  names[i] = names[i] + random.choice(string.ascii_lowercase)

def get_vote_data():
  voterInfo = {
    "name": names.get_full_name(),
    "party": random.choice(party_options),
    "prop_vote": "Prop " + str(random.randint(1, 8)),
    "vote_time": str(random.randint(7, 18)) + ":" + str(random.randint(0, 5)) + 
    str(random.randint(0, 9)), #7am to 7pm
    "default_weight": 1,
  }
  return voterInfo


class Vertex:

  def __init__(self, nodeID, veriNum, cumulativeWeight, weight=1):
    self.id = nodeID
    self.veriNum = veriNum
    self.weight = weight
    self.cumulativeWeight = cumulativeWeight
    self.adjacent = {}
    self.voteData = get_vote_data()

  def __str__(self):
    return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

  def add_neighbor(self, neighbor, weight=0):
    self.adjacent[neighbor] = weight

  def set_veriNum(self, num):
    self.veriNum = num
  
  def get_connections(self):
    return self.adjacent.keys()

  def get_id(self):
    return self.id

  def get_veriNum(self):
    return self.veriNum

  def get_weight(self, neighbor):
    return self.adjacent[neighbor]

  def get_voteData(self):
    return self.voteData

  def set_cumulativeWeight(self, num):
    self.cumulativeWeight = num

  def get_cumulativeWeight(self):
    return self.cumulativeWeight

  def encrypt(self):
    sum1 = sum2 = sum3 = 0
    str1 = self.voteData["vote_time"]
    str2 = self.voteData["name"]
    str3 = self.voteData["party"]
    
    for s in str1:
      sum1 += ord(s)
    for s in str2:
      sum2 += ord(s)
    for s in str3:
      sum3 += ord(s)
      
    return sum1 * sum2 * sum3
    

class Graph:

  #initiallizing the graph
  def __init__(self):
    self.vert_dict = {}
    self.num_vertices = 0
    self.veriNumSet = {}

  def __iter__(self):
    return iter(self.vert_dict.values())

  # adding vertex to the tangleCV graph
  def add_vertex(self, nodeID):
    self.num_vertices = self.num_vertices + 1
    cumulativeWeight = veriNum = 0

    new_vertex = Vertex(nodeID, veriNum, cumulativeWeight)
    self.vert_dict[nodeID] = new_vertex
    
    # 3% chance to be invalid veriNum
    chance = random.randint(1,33)
    if chance == 1:
      veriNum = random.randint(-100000,2147483647)
    else:
      veriNum = self.vert_dict[nodeID].encrypt()
    self.vert_dict[nodeID].set_veriNum(veriNum)

    if veriNum in self.veriNumSet:
      self.veriNumSet[veriNum] += 1
    else:
      self.veriNumSet[veriNum] = 0

    return new_vertex

  def get_vertex(self, n):
    if n in self.vert_dict:
      return self.vert_dict[n]
    else:
      return None

  def add_edge(self, frm, to, cost=0):
    if frm not in self.vert_dict:
      self.add_vertex(frm)
    if to not in self.vert_dict:
      self.add_vertex(to)

    self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)

  def get_vertices(self):
    return self.vert_dict.keys()

  # check if there is any duplicate voterIDs in graph
  def verify_node(self, veriNum):
    if veriNum not in self.veriNumSet or self.veriNumSet[veriNum] != 0:
      return False
    else:
      return True


if __name__ == '__main__':
  random.seed()

  sample_size = 250
  print("Sample Size: ", sample_size)
  
  g = Graph()

  #hard coded and not counted in final vote
  g.add_vertex(0)
  g.add_vertex(1)

  # adds first edge so that every node added to graph after can
  # have 2 vertexes to link to
  g.add_edge(1, 0)

  for i in range(2, sample_size+2):
    g.add_vertex(i)
    # adding valid edges for each new node
    j = i - 1
    total_edges = 0
    while j >= 0:
      if g.verify_node(g.vert_dict[j].encrypt()) and j not in g.vert_dict[j].adjacent and total_edges < 2:
        g.add_edge(i, j)
        total_edges += 1
      j -= 1

    # assigns cumulative weight based on 3 layers of nodes going back verifying this node
    for v in g:
      sum = 1
      for w in v.get_connections():
        sum += 1
        for x in w.get_connections():
          sum += 1
          for z in x.get_connections():
            sum += 1
      v.set_cumulativeWeight(sum)

  # reports which party won
  dem = rep = lib = und = 0
  winner = "error"
  for v in g:
    if g.verify_node(v.encrypt()) and v.get_cumulativeWeight() > 2:

      voterData = v.get_voteData()
      party = str(voterData["party"])

      if (party == "democrat"):
        dem += 1
      elif (party == "republican"):
        rep += 1
      elif (party == "libertarian"):
        lib += 1
      elif (party == "undecided"):
        und += 1

  if (dem > rep and dem > lib and dem > und):
    winner = "Democrats"
    print("Winning Party: ", winner)
    print("Democrat Winning Candidate: ", electees["Democrats"])
  elif (rep > dem and rep > lib and rep > und):
    winner = "Republicans"
    print("Winning Party: ", winner)
    print("Republican Winning Candidate: ", electees["Republicans"])
  elif (lib > dem and lib > rep and lib > und):
    winner = "Libertarians"
    print("Winning Party: ", winner)
    print("Libertarian Winning Candidate: ", electees["Libertarians"])
  elif (und > dem and und > rep and und > lib):
    winner = "Undecided"
    print("Winning Party: ", winner)
    print("Undecided Winning Candidate: ", electees["Undecided"])
  elif (dem == rep):
    winner = "Tie between Democrats and Republicans"
    print("Winning Party: ", winner)
    print("Democrat Winning Candidate: ", electees["Democrats"])
    print("Republican Winning Candidate: ", electees["Republicans"])
  elif (dem == lib):
    winner = "Tie between Democrats and Libertarians"
    print("Winning Party: ", winner)
    print("Democrat Winning Candidate: ", electees["Democrats"])
    print("Libertarian Winning Candidate: ", electees["Libertarians"])
  elif (dem == und):
    winner = "Tie between Democrats and Undecided"
    print("Winning Party: ", winner)
    print("Democrat Winning Candidate: ", electees["Democrats"])
    print("Undecided Winning Candidate: ", electees["Undecided"])
  elif (rep == lib):
    winner = "Tie between Republicans and Libertarians"
    print("Winning Party: ", winner)
    print("Republican Winning Candidate: ", electees["Republicans"])
    print("Libertarian Winning Candidate: ", electees["Libertarians"])
  elif (rep == und):
    winner = "Tie between Republicans and Undecided"
    print("Winning Party: ", winner)
    print("Republican Winning Candidate: ", electees["Republicans"])
    print("Undecided Winning Candidate: ", electees["Undecided"])
  elif (lib == und):
    winner = "Tie between Libertarians and Undecided"
    print("Winning Party: ", winner)
    print("Libertarian Winning Candidate: ", electees["Libertarians"])
    print("Undecided Winning Candidate: ", electees["Undecided"])

  print("\nDemocrat votes:     ", dem)
  print("Republicans votes:  ", rep)
  print("Libertarians votes: ", lib)
  print("Undecided votes:    ", und)
  
  #adjacency list output (shows edges of each node)
  #for v in g:
    #print('g.vert_dict[%s]=%s' % (v.get_id(), g.vert_dict[v.get_id()]))

  # malicious node output
  first = True
  for v in g:
    if not g.verify_node(v.encrypt()):
      if first:
        print("\nMalicious Nodes Detected: ")
        first = False
      print("ID: ", v.get_id(), "False Data: ", v.get_veriNum(), "Expected: ", v.encrypt())
      
  if first:
    print("\nNo malicious nodes deteced.")
  