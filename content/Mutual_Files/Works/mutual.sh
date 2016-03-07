#!/bin/bash

export PATH=$PATH:~/Mutual_Files/mutual
export PATH=$PATH:~/Mutual_Files/mutual/bin
export PATH=$PATH:~/Mutual_Files/velvet
export PATH=$PATH:~/Mutual_Files/oases
export PATH=$PATH:~/Mutual_Files/blast-2.2.26

mutual prefixa=/home/israel/Mutual_Files/velvetA prefixb=/home/israel/Mutual_Files/velvetB kmera=27 kmerb=27 blast_path=/home/israel/Mutual_Files/blast-2.2.26 threads=8 work_path=/home/israel/Mutual_Files saveintermediate=1
