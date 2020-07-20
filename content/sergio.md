Title: Sergio Emilio Mares
Date: 2020-06-15
Slug: sergio
Category: People
Tags: bioinformatics, REU, IQ-BIO

# Sergio Emilio Mares

## Contact info:
 - e-mail- <sergio.mares@okstate.edu>
 - LinkedIn-  <https://www.linkedin.com/in/sergio-mares>

## Bio:
Biochemistry student-researcher at Oklahoma State University. Now, as part of the IQ BIO REU in the Univesristy of Puerto Rico Rio Piedras,
I will explore the tools and insights of bioinformatics and data analysis.

## Research Goals

Introduce myself into the usage of the UNIX interface, the kmer tools and the usage of extensive genome files. 

## Research Abstract

The rhizosphere region is a thin layer around the plant root, which is composed of microbial communities, 
plant cells, and root secretions. Rhizosphere communities from similar niches and variants in geologies 
have shown to impact the composition and plant phenotype (1).  Methodologies conducted to process metagenomics 
begin by relying on pre-filtering steps of redundant, low quality sequences, and assembly of contigs (2).
In (2) the authors claim that metagenomic research is computationally constrained, and novel algorithms
and techniques must be developed to further the field. Recent advancements have introduced k-mer based
sequence analysis. k-mer analysis was developed to overcome time constraints of traditional assembly strategies (3).
The purpose of this study is to explore the changes in composition of microbiota from previously published
rhizosphere communities by k-mer based sequence analysis. It will consist of analyzing the metagenomic
data from the _Tabebuia heterophylla_ rhizosphere communities from different geological substrates.
This project hopes to find and provide further understanding of the key differences in the
_Tabebuia heterophylla_ rhizosphere communities.

1. Ortiz Y, Restrepo C, Vilanova-Cuevas B, Santiago-Valentin E, Tringe SG, Godoy-Vitorino F. 2020. Geology and climate influence rhizobiome composition of the phenotypically diverse tropical tree Tabebuia heterophylla. PLOS ONE 15:e0231083.
1. Scholz MB, Lo C-C, Chain PS. 2012. Next generation sequencing and bioinformatic bottlenecks: the current state of metagenomic data analysis. Current Opinion in Biotechnology 23:9–15.
1. Zhang Q, Pell J, Canino-Koning R, Howe AC, Brown CT. 2014. These Are Not the K-mers You Are Looking For: Efficient Online K-mer Counting Using a Probabilistic Data Structure. PLOS ONE 9:e101271.



## Weekly UPDATES

### Week 8 (20-24, 7, 2020)

```
- Competed the Kalamazoo Protocol
- Finished the Assembly of the SRR... 65, 66 files 
- Have the correct files in Boqueron

[1100.300613] Writing into stats file results/stats.txt...
[1113.346208] Writing into graph file results/LastGraph...
Final graph has 2156933 nodes and n50 of 23, max 682, total 26343081, using 0/15647163 reads
(roble3) [smares@boqueron assembly]$ ls -al
```
### Week 7: (13-17, 7, 2020)

- Completed a presentation for this paper:
https://academic.oup.com/gigascience/article/9/4/giaa028/5812700

- Finished the Kalamazoo protocol.
- Met with Dr. Humberto to talk about the next steps of the project
     * We are meeting more constantly this week
     * I am putting myself a goal to present papers to Humberto
     * Complete a prototype next week


### Week 6: (6-10, 7, 2020)

- Hackathon Week
- Completed a presentation for the Hackaton: 

https://github.com/sermare/Presentations-University-PR-2020/blob/master/Hackaton%20Presentation%202020.pdf


### Week 5: (29 6, 2020 - 3 7 2020)
- Re-routed the files to the correct directory
- Followed the procotol, but instead of using the Kalamazoo commands, I used the miniconda commands (Listed below)
- 29/06/2020 - Google Meet with Dr. Ortiz-Zuazaga
2:30 pm (CST)
- Quality Trimming and Filtering
- Running Digital Normalization
- Partial Partitioning 

- Completed the Quality Trimming and Filtering Sequences:

```
(roble3) [smares@boqueron trim]$ trimmomatic PE ../SRR492065_?.fastq s1_pe s1_se s2_pe s2_se ILLUMINACLIP:/home/humberto/smares/adapters/TruSeq3-PE.fa:2:30:10
(roble3) [smares@boqueron trim]$ ls
s1_pe  s1_se  s2_pe  s2_se
(roble3) [smares@boqueron trim]$ interleave-reads.py s*_pe > combined.fq
(roble3) [smares@boqueron trim]$ fastq_quality_filter -Q33 -q 30 -p 50 -i s1_se > s1_se.trim
(roble3) [smares@boqueron trim]$ fastq_quality_filter -Q33 -q 30 -p 50 -i s2_se > s2_se.trim
(roble3) [smares@boqueron trim]$ fastq_quality_filter -Q33 -q 30 -p 50 -i combined.fq > combined-trim.fq
(roble3) [smares@boqueron trim]$ extract-paired-reads.py combined-trim.fq
(roble3) [smares@boqueron trim]$ gzip -9c combined-trim.fq.pe > ../SRR492065.pe.qc.fq.gz
(roble3) [smares@boqueron assembly]$ cd trim
(roble3) [smares@boqueron trim]$ trimmomatic PE ../SRR492066_?.fastq s1_pe s1_se s2_pe s2_se ILLUMINACLIP:/home/humberto/smares/adapters/TruSeq3-PE.fa:2:30:10
TrimmomaticPE: Started with arguments:
 ../SRR492066_1.fastq ../SRR492066_2.fastq s1_pe s1_se s2_pe s2_se ILLUMINACLIP:/home/humberto/smares/adapters/TruSeq3-PE.fa:2:30:10
Using PrefixPair: 'TACACTCTTTCCCTACACGACGCTCTTCCGATCT' and 'GTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT'
ILLUMINACLIP: Using 1 prefix pairs, 0 forward/reverse sequences, 0 forward only sequences, 0 reverse only sequences
Quality encoding detected as phred33
Input Read Pairs: 4312505 Both Surviving: 4303266 (99.79%) Forward Only Surviving: 9238 (0.21%) Reverse Only Surviving: 0 (0.00%) Dropped: 1 (0.00%)
TrimmomaticPE: Completed successfully
(roble3) [smares@boqueron trim]$ interleave-reads.py s*_pe > combined.fq
final: interleaved 4303266 pairs
output written to block device
(roble3) [smares@boqueron trim]$ fastq_quality_filter -Q33 -q 30 -p 50 -i s1_se > s1_se.trim^C
(roble3) [smares@boqueron trim]$ fastq_quality_filter -Q33 -q 30 -p 50 -i combined.fq > combined-trim.fq
(roble3) [smares@boqueron trim]$ fastq_quality_filter -Q33 -q 30 -p 50 -i s1_se > s1_se.trim
(roble3) [smares@boqueron trim]$ fastq_quality_filter -Q33 -q 30 -p 50 -i s2_se > s2_se.trim
fastq_quality_filter: Premature End-Of-File (filename ='s2_se')
(roble3) [smares@boqueron trim]$ extract-paired-reads.py combined-trim.fq

DONE; read 6215133 sequences, 2662179 pairs and 890775 singletons
wrote to: combined-trim.fq.pe and combined-trim.fq.se
(roble3) [smares@boqueron trim]$ gzip -9c combined-trim.fq.pe > ../SRR492066.pe.qc.fq.gz
(roble3) [smares@boqueron trim]$ gzip -9c combined-trim.fq.se s1_se.trim s2_se.trim > ../SRR492066.se.qc.fq.gz
 
(roble3) [smares@boqueron trim]$ 
(roble3) [smares@boqueron trim]$ cd ..
(roble3) [smares@boqueron assembly]$ ls -l
total 1369096
-rw-r--r-- 1 smares humberto 686755040 Jun 29 17:20 SRR492065.pe.qc.fq.gz
-rw-r--r-- 1 smares humberto  78246257 Jun 29 18:11 SRR492065.se.qc.fq.qz
lrwxrwxrwx 1 smares humberto        44 Jun 29 16:09 SRR492065_1.fastq -> /home/humberto/smares/data/SRR492065_1.fastq
lrwxrwxrwx 1 smares humberto        44 Jun 29 16:09 SRR492065_2.fastq -> /home/humberto/smares/data/SRR492065_2.fastq
-rw-r--r-- 1 smares humberto 457219540 Jun 29 18:50 SRR492066.pe.qc.fq.gz
-rw-r--r-- 1 smares humberto  87946022 Jun 29 18:52 SRR492066.se.qc.fq.gz
lrwxrwxrwx 1 smares humberto        44 Jun 29 16:09 SRR492066_1.fastq -> /home/humberto/smares/data/SRR492066_1.fastq
lrwxrwxrwx 1 smares humberto        44 Jun 29 16:09 SRR492066_2.fastq -> /home/humberto/smares/data/SRR492066_2.fastq
```
-- Completed the Running Digital Normalization
(Normalizing read coverage):

```
normalize-by-median.py -k 20 -C 20 -N 4 -x 5e8 -p --savegraph normC20k20.kh *.pe.qc.fq.gz
normalize-by-median.py -C 20 -s normC20k20.kh -l normC20k20.kh *.se.qc.fq.gz
Error my trim data
filter-abund.py -V normC20k20.kh *.keep
for i in *.pe.qc.fq.gz.keep.abundfilt
do
   extract-paired-reads.py $i
done

Normalize down to C=5
normalize-by-median.py -C 5 -k 20 -N 4 -x 5e8 -s normC5k20.kh -p *.pe.qc.fq.gz.keep.abundfilt.pe
normalize-by-median.py -C 5 -s normC5k20.kh -l normC5k20.kh *.pe.qc.fq.gz.keep.abundfilt.se *.se.qc.fq.gz.keep.abundfilt
Compress and combine the files
gzip -9c SRR492065.pe.qc.fq.gz.keep.abundfilt.pe.keep > SRR492065.pe.kak.qc.fq.gz
gzip -9c SRR492066.pe.qc.fq.gz.keep.abundfilt.pe.keep > SRR492066.pe.kak.qc.fq.gz
and the single-ended files:
gzip -9c SRR492066.pe.qc.fq.gz.keep.abundfilt.se.keep SRR492066.se.qc.fq.gz.keep.abundfilt.keep > SRR492066.se.kak.qc.fq.gz
gzip -9c SRR492065.pe.qc.fq.gz.keep.abundfilt.se.keep SRR492065.se.qc.fq.gz.keep.abundfilt.keep > SRR492065.se.kak.qc.fq.gz
 - not found
Nothing was deleted past this point
```

--Ran (partially) Partitioning (Diving reads in disjoint sets that do not connect):

```
------
SIMPLE PARTITIONING

You will need the normC5k20.kh file from 2. Running digital normalization for this step. If you don’t have it, you can regenerate it like so:
load-into-counting.py -k 20 -N 4 -x 5e8 normC5k20.kh *.qc.fq.gz
do-partition.py -k 32 -x 1e9 --threads 4 kak *.kak.qc.fq.gz.abundfilt
head SRR492065.se.kak.qc.fq.gz.abundfilt.part

EXTRACTING THE PARTITIOONS INTO GROUPS
extract-partitions.py -X 100000 kak *.part
---
Separating groups into PE and SE

for i in kak*.fq
do
   extract-paired-reads.py $i
   name=$(basename $i .fq)
   mv ${name}.fq.pe ${name}.pe.fq
   mv ${name}.fq.se ${name}.se.fq
done

gzip *.pe.fq *.se.fq
----
Reinflating partitions (optional)¶

gunzip -c SRR49206?.?e.qc.fq.gz > all.fq
sweep-reads3.py -x 3e8 kak.group*.fq all.fq

(roble3) [smares@boqueron assembly]$ sweep-reads3.py
-bash: sweep-reads3.py: command not found
```

### Week 4: (22-26, 6, 2020)

  -- Realized I had to create a separate environment using Miniconda
  - Created Roble3 with the following packages: 
    Packages: khmer trimmomatic fastx_toolkit sra-tools (trimming reads of certain kinds of sequencing errors):
    
  - Download the files to used to test <https://www.ncbi.nlm.nih.gov/sra/?term=SRR492065> (SRR492065 and SRR492066)
  
```
(base) MBP-de-Sergio:~ sergiomares$ ssh smares@boqueron.hpcf.upr.edu
smares@boqueron.hpcf.upr.edu's password: 
Last login: Thu Jun 25 16:35:50 2020 from 74.195.246.210
-bash: warning: setlocale: LC_CTYPE: cannot change locale (UTF-8): No such file or directory
(base) [smares@boqueron ~]$ miniconda activate roble3 #El virtual Environment 
(roble3) [smares@boqueron ~]$ trimmomatic SE /home/humberto/smares/assembly/SRR492065.pe.qc.fq.gz OUT_SRR492056.pe.qc.fq.gz ILLUMINACLIP:/home/humberto/smares/adapters/TruSeq3-PE.fa:2:30:10 LEADING:2 TRAILING:2 SLIDINGWINDOW:4:2 MINLEN:25

TrimmomaticSE: Started with arguments:

 /home/humberto/smares/assembly/SRR492065.pe.qc.fq.gz OUT_SRR492056.pe.qc.fq.gz ILLUMINACLIP:/home/humberto/smares/adapters/TruSeq3-PE.fa:2:30:10 LEADING:2 TRAILING:2 SLIDINGWINDOW:4:2 MINLEN:25

Automatically using 1 threads

Using PrefixPair: 'TACACTCTTTCCCTACACGACGCTCTTCCGATCT' and 'GTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT'

ILLUMINACLIP: Using 1 prefix pairs, 0 forward/reverse sequences, 0 forward only sequences, 0 reverse only sequences

Error: Unable to detect quality encoding <---- Descarge el archivo equivacado??
 ```

### Week 3: (15-19, 6, 2020)
  - Signed up into the University of Puerto Rico High Performance Computing Facility.
  - Logged into Boqueron
  - Installed packages following the Kalamazoo website <https://khmer-protocols.readthedocs.io/en/v0.8.4/metagenomics/1-quality.html>
  
  
### Week 2: (8-12, 6, 2020)
  - Developed a plan for the project
  - Finished the Abstract for the Project
  - Worked in the workshop found at <http://claresloggett.github.io/python_workshops/kmer_counting.html>.
  - This workshop helped me further understand the scope of the project and the usage of these algorithms to use big data sets. 
  - Practice my for loops in Python 3 

### Week 1: (1-5, 6, 2020)
  - Took part on the Software Carpentry Workshops.
