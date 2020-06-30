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
After living in Mexico for 16 years, I had to leave my family behind to begin a new journey in the United States. 
Now, as a microbiology and biochemistry student-researcher, I am continuing my path to provide assistance to the 
communities that surround Oklahoma State University. Now, as part of the IQ BIO REU in the Univesristy of Puerto Rico Rio Piedras,
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


### Week 5: (29 6, 2020 - 3 7 2020)
- Re-routed the files to the correct directory
- Followed the procotol, but instead of using the Kalamazoo commands, I used the miniconda commands (Listed below)
- 29/06/2020 - Google Meet with Dr. Ortiz-Zuazaga
2:30 pm (CST)

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

### Week 4: (22-26, 6, 2020)

  -- Realized I had to create a separate environment using Miniconda
  - Created Roble3 with the following packages: 
    Packages: khmer trimmomatic fastx_toolkit sta-tools
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
Dr. Ortiz-Zuazaga recommended run this:

 ```
(roble3) [smares@boqueron ~]$ history | grep SRR492065
  133  java -jar /usr/local/bin/trimmomatic-0.30.jar PE ../SRR492065_?.fastq.gz s1_pe s1_se s2_pe s2_se ILLUMINACLIP:/usr/local/share/adapters/TruSeq3-PE.fa:2:30:10
  141  java -jar /home/humberto/smares/trimmomatic-0.30.jar PE ../SRR492065_?.fastq.gz s1_pe s1_se s2_pe s2_se ILLUMINACLIP:/home/humberto/smares/adapters/TruSeq3-PE.fa:2:30:10
  219  java -jar /home/humberto/smares/trimmomatic-0.30.jar PE ../SRR492065_?.fastq.gz s1_pe s1_se s2_pe s2_se ILLUMINACLIP:/home/humberto/smares/adapters/TruSeq3-PE.fa:2:30:10
  236  java -jar /home/humberto/smares/trimmomatic-0.30.jar PE ../SRR492065_?.fastq.gz s1_pe s1_se s2_pe s2_se ILLUMINACLIP:/home/humberto/smares/adapters/TruSeq3-PE.fa:2:30:10
  246  gzip -9c combined-trim.fq.pe > ../SRR492065.pe.qc.fq.gz
  255  gzip -9c combined-trim.fq.pe > ../SRR492065.pe.qc.fq.gz
  261  java -jar /home/humberto/smares/trimmomatic-0.30.jar PE ../SRR492065_?.fastq.gz s1_pe s1_se s2_pe s2_se ILLUMINACLIP:/home/humberto/smares/adapters/TruSeq3-PE.fa:2:30:10
  281  java -jar /home/humberto/smares/trimmomatic-0.30.jar PE ../SRR492065_?.fastq.gz s1_pe s1_se s2_pe s2_se ILLUMINACLIP:/home/humberto/smares/adapters/TruSeq3-PE.fa:2:30:10
  308  curl -o https://storage.googleapis.com/sra-pub-src-14/SRR492065/1-74-11-repeat.1.txt.gz
  314  ./fastq-dump -X 5 -Z SRR492065
  349  fastq-dump.2 -X 5 -Z SRR492065
  353  ./fastq-dump -X 5 -Z SRR492065
  365  ./fastq-dump.2 -X 5 -Z SRR492065
  366  ./fastq-load -X 5 -Z SRR492065
  367  ./fastq-dump.2 -X 5 -Z SRR492065
  376  ./fastq.dump -X 5 -Z SRR492065
  379  SRR492065./fastq-dump -X 5 -Z SRR492065
  380  ./fastq-dump -X 5 -Z SRR492065
  382  ./fastq-dump -X 5 -Z SRR492065
  386  ./fastq-dump -X 5 -Z SRR492065
  389  fastq-dump -X 5 -Z SRR492065
  390  fastq-dump SRR492065
  447  SRR492065.pe.qc.fq.gz
  448  trimmomatic SE /home/humberto/smares/assembly/SRR492065.pe.qc.fq.gz OUT_SRR492056.pe.qc.fq.gz ILLUMINACLIP:/home/humberto/smares/adapters/TruSeq3-PE.fa:2:0:15 LEADING:2 TRAILING:2 SLIDINGWINDOW:4:2 MINLEN:25
  449  trimmomatic SE /home/humberto/smares/assembly/SRR492065.pe.qc.fq.gz OUT_SRR492056.pe.qc.fq.gz ILLUMINACLIP:/home/humberto/smares/adapters/TruSeq3-PE.fa:2:30:10 LEADING:2 TRAILING:2 SLIDINGWINDOW:4:2 MINLEN:25
  459  trimmomatic SE /home/humberto/smares/assembly/SRR492065.pe.qc.fq.gz OUT_SRR492056.pe.qc.fq.gz ILLUMINACLIP:/home/humberto/smares/adapters/TruSeq3-PE.fa:2:30:10 LEADING:2 TRAILING:2 SLIDINGWINDOW:4:2 MINLEN:25
  461  history | grep SRR492065
(base) [smares@boqueron ~]$ 
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
