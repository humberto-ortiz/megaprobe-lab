Title: Matias Rosner Ortiz
Date: 3/28/2018
Category: People
Tags: megaprobelab

# Bio: 
   - My name is Matias Rosner Ortiz. I'm studying Computer Sciences in the University of Puerto Rico Rio Piedras campus. My goals are to complete my Bachellors in Computer Science and achieve a PhD in Cybersecurity or Networking.
    
# Contact info:

   - e-mail - <matiasrosner@gmail.com>
   - Github - <https://github.com/RosnerM>
  
# Reasearch goals:

   - Spring 2018: Analyze IPv6 traffic on hulk.ccom.uprrp.edu to determine normal data transfer and protocols versus suspicious activity.
  

  
  
# Weekly Update:

### Week 1: (12-16/March)
- Read Grace’s Technical Report.

### Week 2: (19-23/March)
- Gained access to megaprobe lab
- Started to research on IPv6 networks.
- Did a wireshark scan of hulk.ccom.uprrp.edu and saved the log   
- Observed traffic from fca4:5cd6:1637:308:e167:7a08:3563:3745 (hozpi) to fcc7:e680:8435:51a2:a5bd:ac68:880e:660d (hulk.ccom.uprrp.edu). The traffic was pings every 10 seconds.

### Week 4: (2-6/April)
- Updated wireshark to version 2.4.4-1 that includes the cjdns/fc00 module to analyze hyperboria packets

- To set up this module I went to wireshark went to Analyze ->Decode As...-> 
added a new protocol with '+' button and added the following paremeters:
Field	Value	Current
'UDP		5158	Fc00'

### Week 9-12/April
-Was able to capture traffic on the two interfaces: "tun0" and "enp3s0" by control clicking both interfaces when wireshark is sudo started and then hitting on the top menu "Capture" -> "Start"
I used the following wireshark display filter:
"frame.interface_name == tun0 or udp.port ==5158"
to only see traffic in the network interface tun0 or see udp packets that go to the port 5158 (these are encrypted packets that are going to hulk through the physical enp3s0 interface through hyperboria). 

- My next goal is to try to obtain clues about the source/destination and/or content of the hyperboria packets which are encrypted and sent inside over UDP packets, as to relate encrypted hyperboria packets to their un-encrypted version after passing through the cjdns module.

### Week 23-26/April
-Read the cjdns whitepaper (https://docs.meshwith.me/Whitepaper.html) and discovered that there are five different type of packets used by the cjdns module specialle by the "The CryptoAuth" mechanism. The five different type of packets are identified on the first 4 bytes of the packet's header: 
1) Connect To Me - Used to start a session without knowing the other node's key | First 4 byte is bitwise complement of 0.
2) Hello Packet - The first message in beginning a session | If it is 0, 1 or 2 bytes.
3) Key Packet - The second message in a session | If it is 3 or 4.
4) Data Packet - A normal traffic packet. Bigger than 4 bytes is a Data Packet if it is past the handshake phase. 
5) Authenticated - A traffic packet with Poly1305 authentication. Bigger than 4 bytes if before the handshake phase.

- Wireshark does not identify these packet bytes sequences into the five different packet types above, so my goal now is to create a program/Wireshark-extension that would be able to do so.

### Week 14-17/May
- I designed the following Tshark terminal code:

sudo tshark -r /home/matias/tshark/cjdnsdown.pcapng -T fields -e frame.number -e ip.src -e ip.dst -e eth.src -e eth.dst -e frame.time -e fc00.session_state -E header=y -E separator=, -E quote=d -E occurrence=f > /home/matias/tshark/megaprobe.csv

This code generates a file called megaprobe.csv (Comma Separated Value table), in which the expressions (they are indicated by the -e flag) are frame.number (the packets unique frame identifier), ip.src (source ip), ip.dst (destination ip), eth.src (source Network Card Mac Address), eth.dst (destination Network Card Mac Address), frame.time (time log), fc00.session_state (number which represents one the five Hyperboria packet types [described above], also referred to as a nuance. We ran the previous Tshark code on May 15, 2018 at 1pm AST, while we were resetting the Cjdns virtual network card "Tun0" in order to see a connection being established from scratch to hulk.ccom.uprrp.edu and represented by 'Hello Packets'. 
This are the results we got, which was sorted by the column 'fc00.session_state':

| frame.number | ip.src         | ip.dst         | frame.time                          | fc00.session_state |
|--------------|----------------|----------------|-------------------------------------|--------------------|
| 5239         | 136.145.231.10 | 44.131.22.48   | May 15, 2018 13:02:48.322843648 AST | 0                  |
| 5240         | 136.145.231.10 | 198.58.100.240 | May 15, 2018 13:02:48.323943443 AST | 0                  |
| 5438         | 198.58.100.240 | 136.145.231.10 | May 15, 2018 13:02:48.433078232 AST | 2                  |
| 5454         | 44.131.22.48   | 136.145.231.10 | May 15, 2018 13:02:48.529487742 AST | 2                  |
| 5469         | 44.131.22.48   | 136.145.231.10 | May 15, 2018 13:02:48.717727841 AST | 3                  |
| 1            | 198.58.100.240 | 136.145.231.10 | May 15, 2018 13:02:39.757444072 AST |                    |
| 2            | 136.145.181.62 | 136.145.231.10 | May 15, 2018 13:02:39.757828051 AST |                    |
| 3            | 136.145.231.10 | 136.145.181.62 | May 15, 2018 13:02:39.757861850 AST |                    |
| 4            | 136.145.181.62 | 136.145.231.10 | May 15, 2018 13:02:39.757904373 AST |                    |
| 5            |                |                | May 15, 2018 13:02:39.760154001 AST |                    |
| 6            | 136.145.181.62 | 136.145.231.10 | May 15, 2018 13:02:39.772274059 AST |                    |
| 7            | 136.145.231.10 | 136.145.181.62 | May 15, 2018 13:02:39.772306587 AST |                    |
| 8            | 136.145.181.62 | 136.145.231.10 | May 15, 2018 13:02:39.772315015 AST |                    |
| 9            | 136.145.231.10 | 136.145.181.62 | May 15, 2018 13:02:39.772332489 AST |                    |
| 10           | 136.145.231.10 | 136.145.181.62 | May 15, 2018 13:02:39.772365424 AST |                    |
| 11           | 136.145.181.62 | 136.145.231.10 | May 15, 2018 13:02:39.772377093 AST |                    |
| 12           | 136.145.231.10 | 136.145.181.62 | May 15, 2018 13:02:39.772386619 AST |                    |
| 13           | 136.145.181.62 | 136.145.231.10 | May 15, 2018 13:02:39.772418334 AST |                    |
| 14           | 136.145.181.62 | 136.145.231.10 | May 15, 2018 13:02:39.772423995 AST |                    |
| 15           | 136.145.181.62 | 136.145.231.10 | May 15, 2018 13:02:39.772441420 AST |                    |

We can see that we got two '0' packets which are Hello Packets; two '2' packets which are "Repeated Hello Packets"; and a Key Packet represented by the by the byte '3'. We noted that the cjdns/fc00 Wireshark module was not identifying: Data Packets, Authenticated Packets, and Connect to Me Packets with the filter fc00.session_state, but it did identify them with another separate filter called fc00.session_nonce after we questioned where the rest of the unidentified packets where.



Week 21-24/May
- Discusssed with Dr. Humberto Ortiz new future ideas for the lab research. Since the cjdns/fc00 module identified all the Hyperboria packets with a nuance and only some with their name, we thought about modifying my previous Tshark script which uses the given Wireshark-field called "fc00.session_state" to generate the .csv files -- to not use this and rather use the byte locations of the nuance in a packet which is always in a fixed offset (from the Hyperboria Whitepaper and observed on the previous results). To do this I would utilize Python (probably with the 'Scapy' packet manipulation module) to check these given offsets at each given packet, in order to identify the nuance bytes in an automated way and being able to further customize what we can do with these results (Wireshark does no support this); e.g. pass it to another Python program or HTML webserver, in which we could do further operations on the data. Additionally, this Python program would work on any version of Wireshark as it would read the packets directly from the pcapng file as RAW data.
