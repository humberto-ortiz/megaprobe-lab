#!/bin/bash

export PATH=$PATH:~/Mutual_Files/velvet
export PATH=$PATH:~/Mutual_Files/oases

velveth ~/Mutual_Files/velvetA 27 -short -fmtAuto ~/Mutual_Files/velvetA/0Hour_ATCACG_L002_R1_001.fastq.gz 
velvetg ~/Mutual_Files/velvetA -read_trkg yes
oases ~/Mutual_Files/velvetA -cov_cutoff 3  

velveth ~/Mutual_Files/velvetB 27 -short -fmtAuto ~/Mutual_Files/velvetB/0Hour_ATCACG_L002_R1_002.fastq.gz
velvetg ~/Mutual_Files/velvetB -read_trkg yes
oases ~/Mutual_Files/velvetB -cov_cutoff 3 
