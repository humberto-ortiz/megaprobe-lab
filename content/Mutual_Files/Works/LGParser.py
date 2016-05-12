##########################################################################################
#                                                                                        #
# Copyright 2016 Megaprobe-Lab                                                           #
#                                                                                        #
# This is software created by the megaprobe lab under the GPL3 license.                  #
#                                                                                        #
# This program parses the LastGraph file produced by Velvet/Oases. To run the program, #
# utilize the command: "Python2.7 LGParser.py LastGraph"                                 #
#                                                                                        #
##########################################################################################

# Load Modules
import os
import fileinput
import networkx as nx

# Make output directory
if not os.path.exists("Parser_Output"):
    os.mkdir("Parser_Output")

# Arrays to store Forward and reverse complement, Read Count and Orientation
RCOUNT = []

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
        cur_node = fields[1]
        state = 2
    # If NODE append next line to forward array
    elif (state == 2):
        G.node[cur_node]['seq']=line
        # Set state to Read reverse
        state = 3
    # Append next line to reverse array
    elif (state == 3):
        G.node[cur_node]['rev'] = line
        # Go back to searching NODE or ARC
        state = 0
    # First state check line for ARC
    elif (state == 0 and fields and fields[0] == "ARC"):
            src = "+"
            dst = "+"
            # Check if ARC connects two forwards
            if (int(fields[1]) < 0):
                src = "-"
            if (int(fields[2]) < 0):
                dst = "-"
            # Check if ARC connects a reverse to a forward
            G.add_edge(str(abs(int(fields[1]))), str(abs(int(fields[2]))), {'segOri1':src,'segOri2':dst})
    # First state check line for NR
    elif (state == 0 and fields and fields[0] == "NR" and (int(fields[1]) > 0)):
        RCOUNT.append(fields[2])


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
    with open('./Parser_output/Connected_Component'+str(i)+'.gfa', 'w+') as compo:
        # Write GFA File Header
        compo.write("H\tVN:Z:1.0\n")
        # Write each node in connected component to file
        for segName in Component.nodes():
            print segName
            print str(Component.node[segName]['seq'])
            compo.write("S\t" + str(segName) + "\t" + (str(Component.node[segName]['seq']).replace('\n', '').replace('\r', ''))  + "\tLN:i:" + str(len(Component.node[segName]['seq'])) + "\tRC:i:" + str(RCOUNT[int(segName)-1]) + "\n")
        # Write each link to file
        for segName1, segName2 in Component.edges_iter():
            # MUST FIX! ADD REVERSE OR FORWARD
            compo.write("L\t"+ segName1 + "\t" + Component.edge[segName1][segName2]['segOri1'] +"\t" + segName2 + "\t" + Component.edge[segName1][segName2]['segOri2'] + "\t"+ str(CIGAR) +"M\n")
    compo.close

# S    segName,segSeq                               Segment
# L    segName1,segOri1,segName2,segOri2,CIGAR      Link

# Stubs and drivers (uncomment to test)

# print "CIGAR value: " + str(CIGAR)
# print map(len, CC)
# print "How many connected components: " + str(len(CC))
# print list(nx.connected_components_subgraphs(G, False))
# print "All Edges: " + str(G.edges())
# print "All Nodes: " + str(G.nodes())
