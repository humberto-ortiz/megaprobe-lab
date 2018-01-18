Title: Bianca I. Colón Rosado
Date: 2015-05-22
Slug: bianca
Category: People
Tags: Flows

# Biography:

Hello! :)

My name is Bianca I. Colón Rosado, I’m a Computer Science student at the University of Puerto Rico, Río Piedras Campus. I did research on Techniques for Anomaly Detection in IPv4 & IPv6 Network Flows with Dr. Humberto Ortiz-Zuazaga from September 2014 to May 2016.

I presented posters about my research in Women in CyberSecurity Conference (WiCyS) on March 2015, in Atlanta, GA. My poster was about the installation and adaptation of a new tool that supports the efficient collection, storage, and analysis of network flow data. This helps us to be able to capture more types of data for our research. Also in the Computing Alliance of Hispanic-Serving Institutions Conference (CAHSI) on September 2015 and in Women in CyberSecurity Conference (WiCyS) in March 2016, Dallas, TX. These posters were about the implementation of the Benford’s law in Network Flows. This law helps us to detect any type of anomalies affecting Transmission Control Protocol (TCP)  flows, including intentional intrusions or unintended faults and network failures in general. Those anomalies can be detected by investigating the first-digit distributions of the inter-arrival times of TCP synchronise (SYN) packets.

My career short-term goals are to finish my degree in Computer Science, in May 2018. Furthermore, my long-term goals are to pursue graduate studies in Cybersecurity.

My work is supported by the scholarship [Academics and Training for the Advancement of Cybersecurity Knowledge in Puerto Rico (ATACK-PR)](http://atackpr.ccom.uprrp.edu/) supported by the National Science Foundation under Grant No. DUE-1438838.

## Contact Info:
e-mail: bianca.colon1@upr.edu

Github: [github.com/BnkColon](https://github.com/BnkColon)

Twitter: [@BiancaIvelisse1](https://twitter.com/BiancaIvelisse1)

# Project Goals
## First Semester 2014-2015
Read and understand papers about anomaly detection. We installed a set of flow tools on a computer in the UPR ScienceDMZ, including [SiLK](https://tools.netsa.cert.org/silk/docs.html) and [PMACCT](http://www.pmacct.net/). We configure this machine to capture flows from the ScienceDMZ. The ScienceDMZ is a high-performance network for data science. But had problems with the version 9 flows and IPv6 support.

## Second Semester 2014-2015: [Technical Report](https://figshare.com/articles/Techniques_for_Anomaly_Detection_in_Network_Flows/1424475)
Learn how to use SiLK [(Book)](http://tools.netsa.cert.org/silk/analysis-handbook.pdf). With SiLK we collected IPv4 and IPv6 flows. The other tool is [FlowBAT](http://www.flowbat.com/) is a graphical flow-based analysis tool.

In this research, we are classifying as flow anomalies those packets with an inexplicable amount of bytes. We collected flow data using SiLK from the UPR’s Science DMZ. We analized the flows with FlowBAT. No real anomaly was detected because we need to collect more flow data to establish patterns and find anomalies.

Also we can identifies first 10 IP-numbers that generated the most traffic in a network. The program start by reading a file which contains IP numbers with its respective octets. Then, it sums the octets for repeated IP-numbers. Finally, it orders the list of IP numbers, placing those with more octets at the final and we obtain the first 10 IP numbers with the most octets.

## First Semester 2015-2016
We implement the **Benford's Law**. According to Benford’s law of anomalous numbers the frequency of the digit d, appearing as the first significant digit in a collection of numbers, is no uniform as expected intuitively, rather it follows closely the logarithmic relation: Pd = log 10 { 1 + (1/d)}, where d = 1,2,3,4,5,6,7,8,9 and {ZP(d)=1}.

Sets which obey the law the number 1 would appear as the most significant digit about 30% of the time while larger digits would occur in that position less frequently: 9 would appear less than 5% of the time. If all digits were distributed uniformly, they would each occur about 11.1% of the time.

It took one hour to analyze one week of flows. This has billions of coordinates from the inter-arrival time. If we compare Benford’s law with the distribution of leading digits in the inter-arrival time of the flows, then we can identify an anomaly as significant discrepancies between them. We can see that there are anomalies but can’t identify what type of anomalies, or with what computer. These anomalies are the peaks that deviate from the baseline. To get details of what type of anomalies is, we need to consult other techniques.

Another way to analyze our flows using the Benford’s law is comparing the same day each week. If we take for example Monday, March 23,2015 and Monday, March 30, 2015 we will expect that the results be almost the same, and if not they could be anomalies.

The Benford’s Law was effective with our flows. An important advantage of this method is that malware cannot easily adapt their communication pattern to conform to the logarithmic distribution of first digits. We need to validate the method with labeled or simulated data, and build an alerting system to notify of anomalies as soon as they are detected. Finding a general method for detecting anomalies in flows is hard. But with these techniques we can identify when we have real anomalies.

## Second Semester 2015-2016 [Technical Report](https://ccom.uprrp.edu/~humberto/megaprobe/images/technicalReportBianca2sem2016.pdf)

This semester, we want to implement [NAB](http://arxiv.org/pdf/1510.03336v4.pdf), so we can compare and evaluate different algorithms for detecting anomalies in streaming data. Also we want use NAB with our SiLK flows, and run our Bendford's Algorithms with their flows, that are already labeled with real anomalies.

### Weekly Update
#### Week 1: January 19, 2016 - January 22, 2016
Read and understand the paper Evaluating Real-time Anomaly Detection Algorithms – the Numenta Anomaly Benchmark.
#### Week 2: January 25, 2016 - January 29, 2016
When we start installing in Hulk the initial requirements, using the anaconda module get an error of the version `GLIBCXX_3.4.18' when we try to install nupic. After several attemps, we got an SystemError: Cannot compile 'Python.h'.
#### Week 3: February 1, 2016 - February 5, 2016
We install [Vagrant + CoreOS + Docker](https://github.com/numenta/nupic/tree/master/coreos-vagrant) in my computer, to check if nupic work, and work. The next step was to install [NAB](https://github.com/numenta/NAB).
- We installed succesfully and then start running the full NAB. It would take many many hours to run.

#### Week 4: February 8, 2016 - February 12, 2016
Results of NAB:
```
Optimizer found a max score of -33.2060596464 with anomaly threshold 0.803125.

Running scoring step
null detector benchmark scores written to /usr/local/src/NAB/results/null/null_reward_low_FP_rate_scores.csv
null detector benchmark scores written to /usr/local/src/NAB/results/null/null_reward_low_FN_rate_scores.csv
null detector benchmark scores written to /usr/local/src/NAB/results/null/null_standard_scores.csv
numenta detector benchmark scores written to /usr/local/src/NAB/results/numenta/numenta_reward_low_FP_rate_scores.csv
numenta detector benchmark scores written to /usr/local/src/NAB/results/numenta/numenta_reward_low_FN_rate_scores.csv
numenta detector benchmark scores written to /usr/local/src/NAB/results/numenta/numenta_standard_scores.csv
random detector benchmark scores written to /usr/local/src/NAB/results/random/random_reward_low_FP_rate_scores.csv
random detector benchmark scores written to /usr/local/src/NAB/results/random/random_reward_low_FN_rate_scores.csv
random detector benchmark scores written to /usr/local/src/NAB/results/random/random_standard_scores.csv
skyline detector benchmark scores written to /usr/local/src/NAB/results/skyline/skyline_reward_low_FP_rate_scores.csv
skyline detector benchmark scores written to /usr/local/src/NAB/results/skyline/skyline_reward_low_FN_rate_scores.csv
skyline detector benchmark scores written to /usr/local/src/NAB/results/skyline/skyline_standard_scores.csv

Running score normalization step
Final score for 'null' detector on 'reward_low_FP_rate' profile = 0.00
Final score for 'null' detector on 'reward_low_FN_rate' profile = 0.00
Final score for 'null' detector on 'standard' profile = 0.00
Final score for 'numenta' detector on 'reward_low_FP_rate' profile = 58.59
Final score for 'numenta' detector on 'reward_low_FN_rate' profile = 69.38
Final score for 'numenta' detector on 'standard' profile = 65.27
Final score for 'random' detector on 'reward_low_FP_rate' profile = 5.76
Final score for 'random' detector on 'reward_low_FN_rate' profile = 27.20
Final score for 'random' detector on 'standard' profile = 17.66
Final score for 'skyline' detector on 'reward_low_FP_rate' profile = 27.08
Final score for 'skyline' detector on 'reward_low_FN_rate' profile = 44.48
Final score for 'skyline' detector on 'standard' profile = 35.69
Final scores have been written to /usr/local/src/NAB/results/final_results.json.
```

We don't have the real time of this run because we stop the process a few times. We want to run it in Hulk to get that time. Our next step is to analize the way they use their Flows data in order to adapt our Benford's program to that data.
#### Week 5: February 15, 2016 - February 19, 2016
Analyzing the obtained results we found that
   - Their data is saved in .csv formatt containing the timestamp and value.
```
   timestamp,value
   2014-04-01 00:00:00,18.090486228499998
   2014-04-01 00:05:00,20.359842585899997
```
   - The majority of the results provide information about the Detector, Profile, File, Threshold, Score, TP, TN, FP, FN, and Total_Count
```
   Detector,Profile,File,Threshold,Score,TP,TN,FP,FN,Total_Count
   numenta,reward_low_FN_rate,artificialNoAnomaly/art_daily_small_noise.csv,0.5,-0.11,0,3427,1,0,4032
   numenta,reward_low_FN_rate,realAWSCloudwatch/ec2_disk_write_bytes_c0d644.csv,0.5,-0.338868818772,4,3022,1,401,4032
```
#### Week 6: February 22, 2016 - February 26, 2016
Start the installation of NAB in Hulk, but get an error building the docker.
Make an issue report [(#3026)](https://github.com/numenta/nupic/issues/3026)
#### Week 7: February 29, 2016 - March 4, 2016
They respond our issue report [(#3026)](https://github.com/numenta/nupic/issues/3026).

In they recomendations we found a [Dockerfile](https://hub.docker.com/r/numenta/nupic/builds/bvwatcsdwfbzijajcj3t3qa/) (in a similar error) that we can use in [Docker Machine](https://docs.docker.com/machine/). We install Docker Machine in my [computer](https://docs.docker.com/engine/installation/mac/) to try it, if it work we will use that Dockerfile in Hulk.  

Learning Docker Machine:
* [Hello world in a container](https://docs.docker.com/engine/userguide/containers/dockerizing/)
* [Run a simple application](https://docs.docker.com/engine/userguide/containers/usingdocker/)
* [Build your own images](https://docs.docker.com/engine/userguide/containers/dockerimages/)

**Dockerfile**
```
FROM ubuntu:14.04

MAINTAINER Allan Costa <allaninocencio@yahoo.com.br>

# Install dependencies
RUN apt-get update && \
    apt-get install -y \
    curl \
    wget \
    git-core \
    gcc \
    g++ \
    cmake \
    python \
    python2.7 \
    python2.7-dev \
    zlib1g-dev \
    bzip2 \
    libyaml-dev \
    libyaml-0-2
RUN wget https://bootstrap.pypa.io/get-pip.py -O - | python
RUN pip install --upgrade setuptools
RUN pip install wheel

# Use gcc to match nupic.core binary
ENV CC gcc
ENV CXX g++

# Set enviroment variables needed by NuPIC
ENV NUPIC /usr/local/src/nupic
ENV NTA_DATA_PATH /usr/local/src/nupic/prediction/data

# OPF needs this
ENV USER docker

# Copy context into container file system
ADD . $NUPIC

WORKDIR /usr/local/src

# Clone nupic.core
RUN git clone `head -n 2 $NUPIC/.nupic_modules | tail -n 1 | sed -r "s/NUPIC_CORE_REMOTE = '(.+)'/\\1/"` && \
    cd nupic.core && \
    git reset --hard `head -n 3 $NUPIC/.nupic_modules | tail -n 1 | sed -r "s/NUPIC_CORE_COMMITISH = '(.+)'/\\1/"`

WORKDIR /usr/local/src/nupic.core

# Build nupic.core
RUN pip install \
        --cache-dir /usr/local/src/nupic.core/pip-cache \
        --build /usr/local/src/nupic.core/pip-build \
        --no-clean \
        pycapnp==0.5.5 \
        -r bindings/py/requirements.txt && \
    python setup.py install

WORKDIR /usr/local/src/nupic

# Install NuPIC with using SetupTools
RUN python setup.py install

WORKDIR /home/docker
```
#### Week 8: March 7, 2016 - March 11, 2016
My poster, **Techniques for Anomaly Detection in Network Flows: Benford’s Law**, has been accepted to be presented in the [WiCyS 2016](https://www.csc.tntech.edu/wicys/) Poster session. I have been working on it.
#### Week 9: March 14, 2016 - March 18, 2016
The student assembly celebrated on March 15, 2016, decreed a strike of 72 hours, starting on Tuesday, March 15, 2016 until Friday, March 18, 2016.
#### Week 10: March 21, 2016 - March 25, 2016
Easter week.
#### Week 11: March 28, 2016 - April 1, 2016
Conference for Women in Cybersecurity 2016, Dallas, TX.
#### Week 12: April 4, 2016 - April 8, 2016
Try to run the docker in Hulk, but Hulk is broked. I start fixing the vagrant in my computer but get some errors.
Need a Lab Meetig!!
#### Week 13: April 11, 2016 - April 15, 2016
We had a Lab Meeting! Christopher is guilty of breaking Hulk.

I start running NAB in my computer again because we lost the last results when the docker broke. I will left the docker running and start the technical report.
#### Week 14: April 18, 2016 - April 22, 2016
The docker elegant_pasteur broke, again... and the docker machine of Hulk doesn't work. So for my mental peace I will continue with the technical report.

#### Week 15: April 25, 2016 - April 29, 2016
The step of executing our Benford's Law program at NAB is paused. We will work with the data provided by NAB in their github and adapt our program to receive those data.

#### Week 16: May 2, 2016 - May 6, 2016
In the process to adapt our Benford's Law program to receive the data provided by NAB, we need to change some functions. I started making some changes but talking to my adviser I realized that I was complicating my code more than necessary.

In order to mantein my coding skills updated, I decide make the code from scratch.

#### Week 17: May 9, 2016 - May 13, 2016
I'm working in the code.

### Results
We start comparing the expected curve provided by Benford’s Law with the results obtained from the data labeled as no anomalies. We notice some differences that should not be there assuming the data don’t have anomalies. To find more information about this differences we search the deviations from the Benford theoretical curve. In the graph of the Deviations from the Benford Theoretical Curve, there’s a gap between the days from September 5 and some hours of September 9 in the provided data. We didn’t notice that until we make this graph. Also, looking the graph we need to find information to define the real anomalies. We want to prognosticate how close or far the deviation need to be from zero to be counted as a TP, FP, FN, TN.

### Conclusion
In order to prove that the Benford’s Law can detect anomalies in Network Flows we need to continue validating the algorithm with labeled data. NAB provide a lot of files with data, but we don’t get enought time to inspect all the files. Also we need to define when we classify the results of the Deviations from the Benford theorical curve as a real anomaly. An important advantage of this method is that malware cannot easily adapt their communication pattern to conform to the logarithmic distribution of first digits.

### Future Work
We want to analyze more the utility of this law, we want to compare the results of the Deviations from the Benford theorical curve with the octets in the same flows. Also, we will explore new approaches to find new techniques. Implement these techniques for anomaly detection to our collection of flows from UPR’s network, and compare results with the results of current techniques. If those techniques are effective we can use it in real time flow collection and build an alerting system to notify the anomalies as soon as they are detected.
