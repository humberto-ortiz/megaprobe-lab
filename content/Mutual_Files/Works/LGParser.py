##########################################################################################
#                                                                                        #
# Copyright 2016 Megaprobe-Lab                                                           #
#                                                                                        #
# This is software created by the megaprobe lab under the GPL license.                   #
#                                                                                        #
##########################################################################################

# Load Modules
import fileinput
# import networkx as nx


fow = []
rev = []


state = 0 # (0, Reading From File) ( 1, Found Node) (2, Read forward) (3, Read Reverse) (4, Found ARC)
with open('output_file', 'w+') as graph:
   # Open file & iterate over it's lines.
    for (line) in fileinput.input():
        #Save line split into and array fields separating input by whitespace.
        fields = line.split()
        # First state check line for NODE
        if (state == 0 and fields and fields[0] == "NODE"):
            # Set state to Read forward
            state = 2
        # If NODE append next line to forward array
        elif (state == 2):
            fow.append(line)
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
                if   (int(fields[1]) > 0 and int(fields[2]) > 0):
                    graph.write("Use forward " + str(fields[1]) + " and forward " + str(fields[2]))
                    # Use fields-1 as index for forward array to retrieve corresponding node
                    graph.write(fow[int(fields[1])-1] + fow[int(fields[2])-1] + "Arc Multiplicity: " + fields[3])
                # Check if ARC connects a forward to a reverse
                elif (int(fields[1]) > 0 and int(fields[2]) < 0):
                    print "Use forward " + str(fields[1]) + " and reverse " + str(fields[2])
                    print fow[int(fields[1])-1] + rev[(int(fields[2])*-1)-1]
                # Check if ARC connects a reverse to a forward
                elif (int(fields[1]) < 0 and int(fields[2]) > 0):
                    print "Use rev " + str(fields[1]) + " and forward " + str(fields[2])
                    print rev[(int(fields[1])*-1)-1] + fow[int(fields[2])-1]
                # Check if ARC connects two reverses
                elif (int(fields[1]) < 0 and int(fields[2]) < 0):
                    print "Use rev " + str(fields[1]) + " and rev " + str(fields[2])
                    print rev[(int(fields[1])*-1)-1] + rev[(int(fields[2])*-1)-1]
graph.closed
