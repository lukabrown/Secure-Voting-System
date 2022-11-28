# Cybersecurity-Project



Group Members:
Victoria Jordan
Serhat Oncu
Harpaz Aviv
Luka Brown

About the program:
The project we made is a simulator to the use of directed acyclic graph in voting system. 
The program creates random votes which are added to the acyclic graph and are getting validates by 2 other nodes(votes) that already exist in the graph.
The program contains a class that holds the directed acyclic graph and all the nodes that are being added. The class contains a function that validates the votes, by checking whether the ID of the voter is already in the system of votes. Every new vote is added to the list of votes and its following appearances are counted. A vote with a voter ID that is already exists in the votes list, will be considered invalid and will not be considered in the cumulative weight (validation) of the other nodes. The votes are created randomly by the function get_vote_data() and are stores in the class Vertex, which defines each vertex with the vote info, weight and cumulative weight. 
Line 143 in the code determines the number of votes that are being generated. Currently the program is set to simulate 250 votes.
The program outputs the results of the elections from the generated votes: The winning party and winning candidate, as well as the valid voted counted to each party. 
The program then outputs the malicious nodes that were detected from the run, along with the malicious info that caused to its invalidation.


How to run:

to clone the code, in the git terminal execute the command:

git clone https://github.com/lukabrown/Cybersecurity-Project.git <targetDirectory>
  
then, cd into the target directory you input, compile and run the code. (.py file)

