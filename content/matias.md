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
