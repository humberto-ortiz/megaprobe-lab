Glossary
========

_This glossary is intended to be an easy reference for terms commonly used in this repo._

# Graph theory related concepts:

 - De-Bruijng Graph: <https://en.wikipedia.org/wiki/De_Bruijn_graph>
    * In graph theory, an n-dimensional De Bruijn graph of m symbols is a directed graph representing overlaps between sequences of symbols. It has mn vertices, consisting of all possible length-n sequences of the given symbols; the same symbol may appear multiple times in a sequence. If we have the set of m symbols S:={s_1,...,s_m} then the set of vertices is:

 - V=S^n={(s_1,...,s_1,s_1),(s_1,...,s_1,s_2),...,(s_1,...,s_1,s_m),(s_1,...,s_2,s_1),...,(s_m,...,s_m,s_m)}.
    * If one of the vertices can be expressed as another vertex by shifting all its symbols by one place to the left and adding a new symbol at the end of this vertex, then the latter has a directed edge to the former vertex. Thus the set of arcs (aka directed edges) is E={((v_1,v_2,...,v_n),(v_2,...,v_n,s_i)) : i=1,...,m }.

 - De Bruijn sequence: <https://en.wikipedia.org/wiki/De_Bruijn_sequence>
	* In combinatorial mathematics, a k-ary De Bruijn sequence B(k, n) of order n,  is a cyclic sequence of a given alphabet A with size k for which every possible subsequence of length n in A appears as a sequence of consecutive characters exactly once. Each B(k, n) has length k^n. There are {(k!)^{k^(n-1)}} / {k^n} distinct De Bruijn sequences B(k, n).


  - Eulerian Path: <https://en.wikipedia.org/wiki/Eulerian_path>
	* In graph theory, an Eulerian trail (or Eulerian path) is a trail in a graph which visits every edge exactly once.



 - Hamiltonian path: <https://en.wikipedia.org/wiki/Hamiltonian_path>
	* In the mathematical field of graph theory, a Hamiltonian path (or traceable path) is a path in an undirected or directed graph that visits each vertex exactly once.


# DNA/RNA Sequencing (Bioinformatics) related terms:

 - k-mers: <https://en.wikipedia.org/wiki/K-mer>
	* The term k-mer typically refers to all the possible substrings of length k that are contained in a string. In computational genomics, k-mers refer to all the possible subsequences (of length k) from a read obtained through DNA Sequencing. The amount of k-mers possible given a string of length, L, is L-k+1 whilst the number of possible k-mers given n possibilities (4 in the case of DNA e.g. ACTG) is n^k. K-mers are typically used during sequence assembly, but can also be used in sequence alignment.

 - Contigs: <https://en.wikipedia.org/wiki/Contig>
	* A contig (from contiguous) is a set of overlapping DNA segments that together represent a consensus region of DNA. In bottom-up sequencing projects, a contig refers to overlapping sequence data (reads); in top-down sequencing projects, contig refers to the overlapping clones that form a physical map of the genome that is used to guide sequencing and assembly. Contigs can thus refer both to overlapping DNA sequence and to overlapping physical segments (fragments) contained in clones depending on the context.

"Type of data compression within the graphs. 20 consecutive and contiguous A's are represente just as one node A."

 - Non-model organisms: <http://www.nature.com/subjects/non-model-organisms>
	* Non-model organisms are organisms that have not been selected by the research community for extensive study either for historic reasons, or because they lack the features that make model organisms easy to investigate (e.g. they cannot grow in the laboratory, have a long life cycle, low fecundity or poor genetics).

 - Model organism: <https://en.wikipedia.org/wiki/Model_organism>
	* Saccharomyces cerevisiae, one of the most intensively studied eukaryotic model organisms in molecular and cell biology
A model organism is a non-human species that is extensively studied to understand particular biological phenomena, with the expectation that discoveries made in the organism model will provide insight into the workings of other organisms. Model organisms are in vivo models and are widely used to research human disease when human experimentation would be unfeasible or unethical. This strategy is made possible by the common descent of all living organisms, and the conservation of metabolic and developmental pathways and genetic material over the course of evolution. Studying model organisms can be informative, but care must be taken when extrapolating from one organism to another.

	In researching human disease, model organisms allow for better understanding the disease process without the added risk of harming an actual human. The species chosen will usually meet a determined taxonomic equivalency to humans, so as to react to disease or its treatment in a way that resembles human physiology as needed. Although biological activity in a model organism does not ensure an effect in humans, many drugs, treatments and cures for human diseases are developed in part with the guidance of animal models. There are three main types of disease models: homologous, isomorphic and predictive. Homologous animals have the same causes, symptoms and treatment options as would humans who have the same disease. Isomorphic animals share the same symptoms and treatments. Predictive models are similar to a particular human disease in only a couple of aspects, but are useful in isolating and making predictions about mechanisms of a set of disease features.

 - Transcriptome: <https://en.wikipedia.org/wiki/Transcriptome>
	* The transcriptome is the set of all messenger RNA molecules in one cell or a population of cells. There are two general methods of inferring transcriptomes. One approach maps sequence reads onto a reference genome, either of the organism itself (whose transcriptome is being studied) or of a closely related species. The other approach, de novo transcriptome assembly, uses software to infer transcripts directly from short sequence reads.

 - De novo transcriptome assembly: <https://en.wikipedia.org/wiki/De_novo_transcriptome_assembly>
	* De novo transcriptome assembly is the method of creating a transcriptome without the aid of a reference genome. Examining non-model organisms can provide novel insights into the mechanisms underlying the "diversity of fascinating morphological innovations" that have enabled the abundance of life on planet Earth. In animals and plants, the "innovations" that cannot be examined in common model organisms include mimicry, mutualism, parasitism, and asexual reproduction. De novo transcriptome assembly is often the preferred method to studying non-model organisms, since it is cheaper and easier than building a genome, and reference-based methods are not possible without an existing genome. The transcriptomes of these organisms can thus reveal novel proteins and their isoforms that are implicated in such unique biological phenomena.

  - Reference genome: <https://en.wikipedia.org/wiki/Reference_genome>
    * A reference genome (also known as a reference assembly) is a digital nucleic acid sequence database, assembled by scientists as a representative example of a species' set of genes. As they are often assembled from the sequencing of DNA from a number of donors, reference genomes do not accurately represent the set of genes of any single person.

 - RNA-Seq: <https://en.wikipedia.org/wiki/RNA-Seq>
	* RNA-seq (RNA sequencing), also called whole transcriptome shotgun sequencing (WTSS), is a technology that uses the capabilities of next-generation sequencing to reveal a snapshot of RNA presence and quantity from a genome at a given moment in time.


 - Single-nucleotide polymorphism (SNPs): <https://en.wikipedia.org/wiki/Single-nucleotide_polymorphism>
	*A single nucleotide polymorphism or simple nucleotide polymorphism, often abbreviated to just SNP (pronounced snip; plural snips), is a variation in a single nucleotide which may occur at some specific position in the genome, where each variation is present to some appreciable degree within a population (e.g. >1%).

	For example, at a specific base position in the human genome, it may be that in most individuals the base C appears there; but in a minority of individuals, the base A appears at that position instead. There is an SNP at this specific base position, and the two possible nucleotide variations - C or A - are said to be alleles for this base position. Although in this example and most SNPs so far discovered there are only two different alleles, there are also triallelic SNPs in which three different base variations may coexist within a population.	

Coverage information: <>






# Software related terms:
Mutual:

Example:
	velveth /home/israel/velvetA 25 librariesA
	velvetg /home/israel/velvetA -read_trkg yes
	oases /home/israel/velvetA -cov_cutoff 3
	velveth /home/israel/velvetB 25 librariesB
	velvetg /home/israel/velvetB -read_trkg yes
	oases /home/israel/velvetB -cov_cutoff 3
	mutual prefixa=/home/israel/velvetA prefixb=/home/israel/velvetB kmera=25 kmerb=25 blast_path=/home/israel/blast-2.2.24


Velvet: <https://en.wikipedia.org/wiki/Velvet_assembler>
	The Velvet algorithm uses de Bruijn graphs to assemble transcripts. In simulations, Velvet can produce contigs up to 50-kb N50 length using prokaryotic data and 3-kb N50 in mammalian bacterial artificial chromosomes (BACs). These preliminary transcripts are transferred to Oases, which uses paired end read and long read information to build transcript isoforms.

velveth = velvet hash
	This command helps to construct the data set (hashes the reads) for velvetg and includes information about the meaning of each sequence files.
		
	Example: $ velveth velvetA 25 -short -fmtAuto velvetA/0Hour_ATCACG_L002_R1_001.fastq.gz

velvetg = velvet grap
	This command builds the de Bruijn graph from the k-mers obtained by velveth and runs simplification and error correction over the graph. It then extracts the contigs. After running velvetg a number of files are generated. Most importantly, a file of contigs contains the sequences of the contigs longer than 2k, where k is the word-length used in velveth.	

	Example: $ velvetg velvetA

Oases:

Blast:


Trinity:
	Trinity first divides the sequence data into a number of de Bruijn graphs, each representing transcriptional variations at a single gene or locus. It then extracts full-length splicing isoforms and distinguishes transcripts derived from paralogous genes from each graph separately. Trinity consists of three independent software modules, which are used sequentially to produce transcripts:

		1- Inchworm assembles the RNA-Seq data into transcript sequences, often generating full-length transcripts for a dominant isoform, but then reports just the unique portions of alternatively spliced transcripts.
		2- Chrysalis clusters the Inchworm contigs and constructs complete de Bruijn graphs for each cluster. Each cluster represents the full transcriptional complexity for a given gene (or a family or set of genes that share a conserved sequence). Chrysalis then partitions the full read set among these separate graphs.
		3- Butterfly then processes the individual graphs in parallel, tracing the paths of reads within the graph, ultimately reporting full-length transcripts for alternatively spliced isoforms, and teasing apart transcripts that corresponds to paralogous genes.
