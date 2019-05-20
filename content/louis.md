Title: Louis F. Gil Acevedo 
Date: 12-13-2017
Modified: 4-20-2019
Slug: louis
Category: People
Tags: Cancer diff-hash de-novo de-bruijn

## Contact info:

 - e-mail - <louis-gil@live.com>
 - Github - <https://github.com/LouisGil/>

# Bio:
Hi Im Louis Im a Computer Science undergraduate student. Im interested in the beautiful merger of computer science and biology. It all started with [the fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number).

> Insert Quotes here Please!!!


# Weekly Updates

## Predicting cancer outcome using kmer differential expression

### Week 15-18 (21-17/May)
-Ran diffhash with the first 4 million lines of each sample
-Identified kmers only present in the tumor sample
-Calculated Fold Change from hashcounts (sumed 1 to every sample in order to eliminate the 0's in the divition)

### Week 11-14 (1-20/April)
-Ran using duplicates of my own files (test) in order to have multilple samples of each condition (seems fine)
-Ran using no duplicates (using test files). (This also seems fine, checked hashcounts and output fasta file)
-Running diffhash with real data 
-Looking into a tool used in kevlar for converting reads to kmers and substractic kmer's from the reference genome (this may make running diffhash faster by eliminating not novel data)

### Week 9-10 (10-31/March)
-Was trying to use kevlar 
-Currently using Sanquises version of diffhash
-Created a subset of my data fot testing diffhash

### Week 8 (3-8/March)
-Converted bam files to fastq
-Modifing diffhash to see if there are kmers that apear in the tumor sample (changed the reader to fastq)


### Week 7 (25-1/Feb)
-Very intensive test and project week no progress

### Week 6 (18-22/Feb)
-Recieved response from titus & contacted me with Sasha from the Personal Genome Proyect. I now have [data](https://my.pgp-hms.org/profile/huDCD45D).

### Week 5 (11-15/Feb)
-Prepare power point for presentation/Review of "Fast and accurate differential transcript usage by testing equivalence class counts"

-Ask Titus if he knows of any publicly available human cancer raw data (Tumor & Germline)

-Learn to use Deseq2

### Week 3 (28-1/Jan)
-Ran diff-hash on defaulf

### Week 1&2 (14-25/Jan)
-Establish what to do researsh on and read papers to back in shape

-Try to find publicly available raw fastq's of cancer patients

-Ir al workshop de Hector Corrada

### During this semester we'll be working on a shared transcript discovery tool that creates a de-bruijn graph from different transcripts in order to analyze differential expression.
___
###
### Week 9 (14-19/Feb):
-Modifing the diferential expresion formula. Found to many outliars that the original formula was going to miss and miss repeent hence not only false negatives but false positives. The formula was adapted to the (kmer_A1-kmer_B1)+(kmer_A2-kmer_B2)/(kmer_A1+kmer_B1+kmer_A2+kmer_B2). The other aproach that was concluded for future work, was to test each node for diferential expression and using the treshold cut those off, this method may be very quick since it can be done from the creation of the graph.

### Week 8 (21-26/Feb):
-Corecting error made in the creation of the test files. I cut the fasta file instead of the transcipt file.

### Week 7 (14-19/Feb):
-Creating test file for testing diferential expression and treshold. Using flux simulator created two similar yeast derived organisms. This was done by using the crhomosome 4 of the yeast transcript file and the fasta file corespondin to the chromosome. The I created the similar organism by cuting half of the fasta file and re runing the fluxsimulator in order to create the second fastq file.

### Week 6 (7-12/Feb):
- Add Diferential Expresion to current vertion. Such that by a user set cuttoff point, links with a lower score than this will be deleted. 

### Week 3: (11-15/Dec)
- Add kmer count to output file.
-[gfalint](https://github.com/sjackman/gfalint)
-[gfapy](https://github.com/ggonnella/gfapy)
-[exampple gfa 2](https://github.com/sjackman/gfalint/blob/master/examples/big1.gfa)

### Week 2: (4-8/Dec)
- Modify [dbg](https://github.com/pmelsted/dbg) to accept two files and check for contigs correctness.

### Week 1: (27/Nov-1/Dec)
- Attack plan, and establish goals
- Test [dbg](https://github.com/pmelsted/dbg) for correctness by running the same fasta file and check for difference, and check the dictionary used for correct kmer count.
- Read sugested papers
  - [Heuristic pairwise alignment of de Bruijn graphs](https://bmcgenomics.biomedcentral.com/articles/10.1186/1471-2164-16-S11-S5)
  - [Transcriptomic changes during regeneration of the central nervous system in an echinoderm](https://bmcgenomics.biomedcentral.com/articles/10.1186/1471-2164-15-357)
  - [Salmon provides accurate, fast, and bias-aware transcript expression estimates using dual-phase inference](https://www.biorxiv.org/content/early/2016/08/30/021592)



