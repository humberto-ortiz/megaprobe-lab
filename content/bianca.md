Title: Bianca I. Colón Rosado
Date: 2015-05-22
Slug: bianca
Category: People
Tags: Flows

Hello! :)


My name is Bianca I. Colón Rosado, I’m an 20 year old junior Computer Science student at the University of Puerto Rico, Río Piedras Campus. I'm doing a research on Techniques for Anomaly Detection in IPv4 & IPv6 Network Flows with Dr. Humberto Ortiz-Zuazaga since September 2014. 

I presented posters about my research in Women in CyberSecurity Conference  (WiCyS) on March 2015, in Atlanta, GA and in the Computing Alliance of Hispanic-Serving Institutions Conference (CAHSI) on September 2015. Also participate in Malcon CTF 2015 with three partners and win first place.

My career short term goals are to finish my degree in Computer Science and still doing undergraduate research. Furthermore, my long-term goals are to pursue graduate studies in computer science.

My work is supported by the scholarship [Academics and Training for the Advancement of Cybersecurity Knowledge in Puerto Rico (ATACK-PR)](http://atackpr.ccom.uprrp.edu/) supported by the National Science Foundation under Grant No. DUE-1438838.

#Project Goals
This semester, we want to implement [NAB](http://arxiv.org/pdf/1510.03336v4.pdf), so we can compare and evaluate different algorithms for detecting anomalies in streaming data. Also we want use NAB with our SiLK flows, and run our Bendford's Algorithms with their flows.

#Weekly Update
## January 19, 2016 - January 22, 2016
Read and understand the paper Evaluating Real-time Anomaly Detection Algorithms – the Numenta Anomaly Benchmark.
## January 25, 2016 - January 29, 2016
When we start installing in Hulk the initial requirements, using the anaconda module get an error of the version `GLIBCXX_3.4.18' when we try to install nupic. After several attemps, we got an SystemError: Cannot compile 'Python.h'. 
## February 1, 2016 - February 5, 2016
We install [Vagrant + CoreOS + Docker](https://github.com/numenta/nupic/tree/master/coreos-vagrant) in my computer, to check if nupic work, and work. The next step was to install [NAB](https://github.com/numenta/NAB).
- We installed succesfully and then start running the full NAB. It would take many many hours to run.

## February 8, 2016 - February 12, 2016
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
## February 15, 2016 - February 19, 2016
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

