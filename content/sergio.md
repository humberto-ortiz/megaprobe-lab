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


## Weekly UPDATES

### Week 3: (15-19, 6, 2020)
  - Signed up into the University of Puerto Rico High Performance Computing Facility.
  - Logged into Boqueron
  - Installed packages following the Kalamazoo website <https://khmer-protocols.readthedocs.io/en/v0.8.4/metagenomics/1-quality.html>
  -- Realized I had to create a separate environment using Miniconda
  - Created Roble3 with the following packages: 
   - khmer trimmomatic fastx_toolkit sta-tools
  - Download the files to used to test <https://www.ncbi.nlm.nih.gov/sra/?term=SRR492065> (SRR492065 and SRR492066)
  - Ran Trimmomatic with the files
  
 ```
(base) MBP-de-Sergio:~ sergiomares$ ssh smares@boqueron.hpcf.upr.edu
smares@boqueron.hpcf.upr.edu's password: 
Last login: Thu Jun 25 16:35:50 2020 from 74.195.246.210
-bash: warning: setlocale: LC_CTYPE: cannot change locale (UTF-8): No such file or directory
(base) [smares@boqueron ~]$ activate roble3 #El virtual Environment 
(base) [smares@boqueron ~]$ history | grep SRR492065
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
  
### Week 2: (8-12, 6, 2020)
  - Developed a plan for the project
  - Finished the Abstract for the Project
  - Worked in the workshop found at <http://claresloggett.github.io/python_workshops/kmer_counting.html>.
  - This workshop helped me further understand the scope of the project and the usage of these algorithms to use big data sets. 
  - Practice my for loops in Python 3 

### Week 1: (1-5, 6, 2020)
  - Took part on the Software Carpentry Workshops.
