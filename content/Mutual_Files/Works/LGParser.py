##########################################################################################
#                                                                                        #
# Copyright 2016 Megaprobe-Lab                                                           #
#                                                                                        #
# This is software created by the megaprobe lab under the GPL license.                   #
#                                                                                        #
##########################################################################################

# Load Modules
import fileinput
import networkx as nx

# Arrays to store Forward and reverse complement, Read Count and Orientation
seq = []
rev = []
RC = []
O = []

# Deterministic Finite State Automata:
# (0, Reading From File searching for "NODE", "ARC" or "NR")
# (1, Found )
# (2, Read forward)
# (3, Read Reverse)
state = 0

# Networkx graph constructor
G = nx.Graph()

############################################
#                                          #
# Reading LastGraph format input file      #
#                                          #
############################################


# Initiate file processing
with open('output_file', 'w+') as graph:
    # Open file & iterate over it's lines.
    for (line) in fileinput.input():
        #Save line split into and array fields separating input by whitespace.
        fields = line.split()
        # Store K-mer size from header
        if (fields and fileinput.lineno() == 1):
            CIGAR = (int(fields[2])-1)
        # First state check line for NODE
        if (state == 0 and fields and fields[0] == "NODE"):
            # Set state to Read forward
            G.add_node(fields[1])
            state = 2
        # If NODE append next line to forward array
        elif (state == 2):
            seq.append(line)
            # Set state to Read reverse
            state = 3
        # Append next line to reverse array
        elif (state == 3):
            rev.append(line)
            # Go back to searching NODE or ARC
            state = 0
        # First state check line for ARC
        elif (state == 0 and fields and fields[0] == "ARC"):
                # Check if ARC connects two forwards
                if  (int(fields[1]) > 0 and int(fields[2]) > 0):
                    graph.write("Use forward " + str(fields[1]) + " and forward " + str(fields[2])+ "\n")
                    # Use fields-1 as index for forward array to retrieve corresponding node
                    graph.write(seq[int(fields[1])-1] + seq[int(fields[2])-1])
                    graph.write("Arc Multiplicity: " + fields[3]+ "\n")
                    # Add an edge to graph
                    G.add_edge(str(fields[1]), str(fields[2]))
               # Check if ARC connects a forward to a reverse
                elif (int(fields[1]) > 0 and int(fields[2]) < 0):
                    graph.write("Use forward " + str(fields[1]) + " and reverse " + str(fields[2]))
                    graph.write(seq[int(fields[1])-1] + rev[(int(fields[2])*-1)-1])
                    G.add_edge(str(fields[1]),str(fields[2]))
                # Check if ARC connects a reverse to a forward
                elif (int(fields[1]) < 0 and int(fields[2]) > 0):
                    graph.write("Use rev " + str(fields[1]) + " and forward " + str(fields[2]))
                    graph.write(rev[(int(fields[1])*-1)-1] + seq[int(fields[2])-1])
                    G.add_edge(str(fields[1]),str(fields[2]))
                # Check if ARC connects two reverses
                elif (int(fields[1]) < 0 and int(fields[2]) < 0):
                    graph.write("Use rev " + str(fields[1]) + " and rev " + str(fields[2]))
                    graph.write(rev[(int(fields[1])*-1)-1] + rev[(int(fields[2])*-1)-1])
                    G.add_edge(str(fields[1]),str(fields[2]))
        # First state check line for NR
        elif (state == 0 and fields and fields[0] == "NR" and (int(fields[1]) > 0)):
            RC.append(fields[2])
graph.closed

# Store all connected components in a list called CC
CC = list(nx.connected_components(G))

############################################
#                                          #
# Start writing output to GFA file Format  #
#                                          #
############################################

# For each connected component in CC write a new file with it's nodes.
for i in range(0,len(CC)):
    # Store subgraph of connected component in list called Component
    Component = nx.subgraph(G,CC[i])
    # Write current component to file
    with open('Connected_Component'+str(i)+'.gfa', 'w+') as compo:
        # Write GFA File Header
        compo.write("H\tVN:Z:1.0\n")
        # Write each node in connected component to file
        for segName in Component.nodes():
            if (int(segName) < 0):
                Node  = int(segName)*-1
            else:
                Node = int(segName)
            compo.write("S\t" + str(Node) + "\t" + (str(seq[int(Node)-1]).replace('\n', '').replace('\r', ''))  + "\tLN:i:" + str(len(seq[int(Node)-1])-1) + "\tRC:i:" + str(RC[int(Node)-1]) + "\n")
        # Write each link to file
        for segName1, segName2 in Component.edges():
            if (int(segName1) < 0 ):
                segOri1 = "-"
                Node1 = int(segName1)*-1
            elif (int(segName2) < 0):
                segOri2 = "-"
                Node2 = int(segName2)*-1
            else:
                segOri1 = "+"
                segOri2 = "+"
                Node1 = int(segName1)
                Node2 = int(segName2)
            # MUST FIX! ADD REVERSE OR FORWARD
            compo.write("L\t"+ str(Node1) + "\t" + segOri1 +"\t" + str(Node2) + "\t" + segOri2 + "\t"+ str(CIGAR) +"M\n")
        compo.close

# S    segName,segSeq                               Segment
# L    segName1,segOri1,segName2,segOri2,CIGAR      Link

# Stubs and drivers (uncomment to test)

# print "Here's K-1: " + str(K)
# print map(len, CC)
# print "How many connected components: " + str(len(CC))
# print list(nx.connected_components_subgraphs(G, False))
# print "Edges: " + str(G.edges())
# print "s: " + str(G.nodes())
