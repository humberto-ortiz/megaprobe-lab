Title: De Novo Sequencing Project
Date: 2016-01-22
Modified: 2016-01-22
Slug: de-novo-project
Category: Projects
Tags: de-novo, Bioinformatics, Python, sequence assembly

## Introduction

Samples of DNA/RNA known as **sequences** can be used to understand
the information of nucleotides in biological structures. Small
fragments known as **reads** are produced from DNA by a **DNA
Sequencer**.  In the process of **sequence assembly** these fragments
can be joined in order to reconstruct a complete sequence of the
organism’s DNA. *De-novo*, meaning ”from the beginning”, refers to
sequence assembly done without a reference genome, and it is used when
trying to discover/reconstruct new genome sequences.

A common problem in sequence assembly can occur from errors in the
sequencing data used. Reads can contain one or more mismatches from
the original genome and could lead to inaccurate sequence
assemblies. In *de-novo* sequence assembly it becomes particularly
challenging, due to not having any reference to compare the reads with
and verify their integrity.

This project is a collaboration between
[Jose Agosto Rivera's Lab](https://www.researchgate.net/profile/Jose_Luis_Agosto),
[Pittsburgh Supercomputing Center](http://psc.edu/),
[RISE](http://brtcpr.com/rise/index.html), and
[MegaProbe]({filename}/pages/about.md).

## Red Brick Wall

As sequencing continues to produce more and more data for lower costs,
the analysis is falling behind the production of data, and new
techniques have to be devised. The following graph illustrates how
sequencing has far outstripped computational capacity.

![Cost per MB of sequence data]({static}/images/costperMb2015_4.jpg)

Wetterstrand KA. DNA Sequencing Costs: Data from the NHGRI Genome
Sequencing Program (GSP) Available at:
<http://www.genome.gov/sequencingcostsdata>. Accessed 2017-01-17.

## De Bruijn Graphs

To represent and assemble next-generation sequencing data, most
programs construct k-mer or De Bruijn graphs. Here's an example graph
for a simulated set of reads from a 1000 base pair sequence with some
sequencing errors (red dots).

![Small De Bruijn graph for 1000 base sequence]({static}/images/contig-0.png)

## Probabilistic structures

As the sequencing data continues to grow, it becomes infeasible to
completely store and process the full data set. We are looking at
probabilistic data structures to approximate the graphs, and allow
some biological questions to be answered.

The figure below represents a portion of a De Bruijn graph for a real
data set from Nematostella Embryonic Transcriptome (Starlet sea
anemone). <https://darchive.mblwhoilibrary.org/handle/1912/5613>

![Bandage graph of velvet/oases output.]({static}images/contigs_graph.png)

Some tools for hashing and probabilistic counting of k-mers have been
implemented in the khmer-tools suite.

Crusoe MR, Alameldin HF, Awad S et al. The khmer software package:
enabling efficient nucleotide sequence analysis
[version 1; referees: 2 approved, 1 approved with reservations]. F1000Research
2015, 4:900 (doi: 10.12688/f1000research.6924.1)


### Error-correction

K-mer hashing and counting can be used to efficently and effectively
remove sequencing errors from datasets. For example, all errors in the
first graph can be removed by selecting all k-mers that appear at
least twice in the data.

### Shared transcript prediction

The mutual software described in Fu S, Tarone AM, Sze SH. (2015)
Heuristic pairwise alignment of de Bruijn graphs to facilitate
simultaneous transcript discovery in related organisms from RNA-Seq
data. BMC Genomics 16:S5 predicts shared transcripts by searching for
sequences derived from two De Bruijn graphs that resemble each other.

In our lab we are working to directly determine shared structure from
two graphs, to speed up and improve the results of mutual.

### Differential expression

Current techniques for assesment of differential expression assemble
transcriptomes from RNAseq data, then count the abundance of each
transcript in a set of samples, and infer probabilities of
differential expression.

Can we instead infer differential expression directly from k-mer counts?

## Downstream analysis

### Regulatory network engineering

I have done some work on reverse-engineering gene regualtory networks
from microarray data. Ideally, given enough RNAseq data over a time
series, we should be able to infer regulatory relationships from the
collection of k-mer counts.
