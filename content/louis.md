Title: Louis F. Gil Acevedo 
Date: 12-13-2017
Modified: 2-19-2017
Slug: louis
Category: People
Tags: de-novo de-bruijn

## Contact info:

 - e-mail - <louis-gil@live.com>
 - Github - <https://github.com/LouisGil/>

# Bio:
Hi Im Louis Im a Computer Science undergraduate student. Im interested in the beautiful merger of computer science and biology. It all started with [the fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number).

> Insert Quotes here


# Weekly Updates


### During this semester we'll be working on a shared transcript discovery tool that creates a de-bruijn graph from different transcripts in order to analyze differential expression.

###

###
### Week 9:
-Modifing the diferential expresion formula. Found to many outliars that the original formula was going to miss and miss repeent hence not only false negatives but false positives. The formula was adapted to the (kmer_A1-kmer_B1)+(kmer_A2-kmer_B2)/(kmer_A1+kmer_B1+kmer_A2+kmer_B2). The other aproach that was concluded for future work, was to test each node for diferential expression and using the treshold cut those off, this method may be very quick since it can be done from the creation of the graph.

### Week 8 :
-Corecting error made in the creation of the test files. I cut the fasta file instead of the transcipt file.

### Week 7 :
-Creating test file for testing diferential expression and treshold. Using flux simulator created two similar yeast derived organisms. This was done by using the crhomosome 4 of the yeast transcript file and the fasta file corespondin to the chromosome. The I created the similar organism by cuting half of the fasta file and re runing the fluxsimulator in order to create the second fastq file.

### Week 6 (7-12):
- Add Diferential Expresion to current vertion. Such that by a user set cuttoff point, links with a lower score than this will be deleted. 

### Week 3: (11-14/Dec)
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



