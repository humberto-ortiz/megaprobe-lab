Title: Ivan L. Jimenez Ruiz
Date: 2016-01-22
Slug: Ivan
Category: People
Tags: de-novo

## Bio:

 Hi! 
 My name is Ivan Jimenez and I am a senior Computer Science undergrad at the University of Puerto Rico, Rio Piedras Campus (UPRRP). I'm currently working as a paid researcher for the RISE (Research Initiative for Scientific Enhancement) program at the UPRRP. My project at the Megaprobe-Lab focuses on comparing and contrasting denovo and reference-based assemblies of RNA-sequenced data. 

 For more info on my background as a researcher, please check out my (possibly-not-up-to-date) biosketch by clicking the link below:

 - BIOSKETCH: <https://github.com/NacroKill/dmel-ercc-diff/blob/master/Biographical_Sketch_ILJR.pdf>

## Contact info:

 - e-mail - <ivanjimenezruiz@yahoo.com>
 - Github - <https://github.com/Nacrokill/>

## Project DESCRIPTION:

 - 'Project site': <https://github.com/NacroKill/dmel-ercc-diff>
 
 	-  Includes weekly reports from Summer 2015 Internship at the Pittsburgh Supercomputing Center (PSC)...

 - The 2nd Semester 2015-2016 workplan can be found at:

	-  <https://github.com/NacroKill/dmel-ercc-diff/blob/master/ILJR_2016_RISE_Workplan.pdf>



## Weekly UPDATE - 1st Semester 2016-2017

 - DISCLAIMER: All programs mentioned below were ran on Megaprobe Lab's supercomputer: Hulk
 	
### Week 5: (5/Sept-11/Sept):

 - Fixed the R script to fix (reproduce correctly) [plot 2], used kmer_size=15 now.

 - Reproducing plot E of original paper using de novo results for 936 and 935: [plot 6]

 - Must meet with Dr. Ricardo Gonzalez again to discuss the next step.
 	- Possibly involving ROC curves...

### Week 4: (29/Aug-4/Sept.):

 - Ran Trinity using SRR039935 18 times: "kmer_size" set to 13,14,...,30.

 - Ran BLAST against all Trinity references for all 18 different kmer_sizes of this file

 - Created R script to produce barplot [plot 4] with ERCC retention values for SRR039935, "kmer_size" of 16 had the highest retention...

 - Ran RSEM for Trinity run of 935 with kmer_size equal to 16 

 - Must replicate plot E using de novo assembly results of 936 and 935 files, using their best individual kmer_size parameter results


### Week 3: (22/Aug-28/Aug.):

 - Ran Trinity using SRR039936 21 times: "kmer_size" set to 11,12,13,14,...,31.
 	- Trinity runs where kmer_size was set to 11 and 12 did not execute (failure: kmer_size too small)
 	- Simply using 18 assembly results, Trinity run with kmer_size set to 13-30.

 - Ran BLAST against all Trinity references for all 21 different kmer_sizes of this file, just in case.

 - Created R script to produce barplot [plot 3] with ERCC retention values for SRR039936, "kmer_size" of 15 had the highest retention among the 18 runs...
 	- Must fix [plot 2]...
 		- Must rerun Rscript to recreate this plot using correct kmer_size=15 results

 - Ran RSEM for Trinity run of 936 with kmer_size equal to 15 

 - Reproduced plot E [plot 5] using reference based assembly results of 936 and 935 files

### Week 2: (15/Aug-21/Aug.):

 - Met with Dr. Ricardo Gonzalez at University of Puerto Rico Medical Science Campus to discuss previous results (discuss 2 plots: ref based [plot 1] and de novo [plot 2] assembly of SRR039936)

 - On the right track: replicate plots C and E of Figure 1 of "original paper" using both de novo and reference based assemblies.
 	- Before continuing with de novo: 
 		- Must create bar plots [plots 3 and 4] to show ERCC retention using different values for Trinity parameter "kmer_size"
 			- Use best kmer_size for de novo assembling both SRR039936 and SRR039935 in order to replicate plot E 

### Week 1: (8/Aug-14/Aug.):

 - So far: 
 	- switched to Megaprobe Lab's supercomputer called Hulk 
 	- Cufflinks, Trinity (with kmer_size equal to 20) and RSEM have been run on SRR039936 (100% ERCC file)
 	- replicated plot C using reference based and de novo approach [plots 1 and 2 respectivelly].
 		- Used R script for plot 1
 		- Needed to run BLAST on Trinity results for plot 2...

 - Need to tackle reproducing plot E with both types of assemblies as soon as possible...




## Weekly UPDATE - 2nd Semester 2015-2016

 - DISCLAIMER: All programs mentioned below were ran on PSC's Greenfield (R.I.P. BLACKLIGHT)
 	- List of PSC hardware: https://www.psc.edu/index.php/data-exacell/hardware-infrastructure

 - GENERAL SMALL NOTES:
	- Sickle directory (after running scythe) must be made writable (chmod +w).
	- ALWAYS double check the permissions if your program fails.
		- Fastq/fasta data files must be made executable (chmod +x).
	- When converting from .fastq to .fasta to feed to Trinity: conversion (using fastx) toolkit discards any reads with any N's (unknown base)
		- For now, we are keeping these reads, using the -n parameter of fastq_to_fasta to do so.
		- One-liner to convert 936 file for example, ran:
			- $ ./fastq_to_fasta -n -Q 33 -i /home/ivan/data_files/quality_filtering/sickle_result/SCY_TRIM__SRR039936.fastq -o /home/ivan/data_files/quality_filtering/sickle_result/SCY_TRIM__SRR039936.fasta
			- $ ./fastq_to_fasta -n -Q 33 -i /home/ivan/data_files/quality_filtering/sickle_result/SCY_TRIM__SRR039458.fastq -o /home/ivan/data_files/quality_filtering/sickle_result/SCY_TRIM__SRR039458.fasta 
				- Ran this one-liner for all scytrim files: 936, 935, 933, 458, 460.
					- Then ran: $ chmod +x /home/ivan/data_files/quality_filtering/sickle_result/SCY_TRIM__SRR039*
	- When making all plots on my computer, the directory RStudio saves them to is: 
		- /Users/ivanjimenez/Desktop/CLASES/INTERNSHIPS/BIOINFO\ INTERNSHIP\ FILES/RESULTS/newresults/reproducing_paper_results/reproducing_paper_results/moved_now_to_hulk/tuxedo_tophat_cufflinks_scytrim936/.
			- moving all plots to new directory: 
				- /Users/ivanjimenez/Desktop/CLASES/INTERNSHIPS/BIOINFO\ INTERNSHIP\ FILES/RESULTS/newresults/reproducing_paper_results/reproducing_paper_results/moved_now_to_hulk/Plots/.
	- After running Trinity, made a directory called "logs" in the output directory to move the .log .out and .error files into.

 - Partial download list for program versions used:
	- wget http://hannonlab.cshl.edu/fastx_toolkit/fastx_toolkit_0.0.13_binaries_Linux_2.6_amd64.tar.bz2
  	- wget https://github.com/trinityrnaseq/trinityrnaseq/archive/v2.2.0.zip
	- wget http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.6.2/sratoolkit.2.6.2-ubuntu64.tar.gz

### Week 15: (25/April-1/May):

 - Trial-running Trinity v2.2.0 on 936 to reproduce plotC:
	- NOTE: The following parameters are just the preliminary one's we chose to alter, need to double-check with Ricardo if these are all/some/none of the correct parameters to use.
		- #### Inchworm and K-mer counting-related options ####
          	- $ --min_kmer_cov <int>          :min count for K-mers to be assembled by Inchworm (default: 1)
				- Changed this parameter to 2, to minimize the number of sequence errors that are accepted in the execution of this phase.
			- $ --KMER_SIZE <int>             :kmer length to use (default: 25)  max=32
				- Changing to 15 (for first run) (Humberto says this is a "magic" parameter: too low and we get too many matches and run out of memory; too high and we do not get enough matches). 
				- On his orders: running trinity 4 times with this set to 15, 20, 25 and 30 respectively. We will then recreate plotE with all 4 Trinity runs and then choose the one that most closely matches.
 			- $ --SS_lib_type <string>        :Strand-specific RNA-Seq read orientation. if paired: RF or FR, if single: F or R.   (dUTP method = RF) See web documentation.

### Week 14: (18/April-24/April):

 - Reproduced PlotC with SRR039936 original and scythed/trimmed fastq data. (scytrim plot is slightly better)
	- DISCOVERY: In the original paper, they did NOT multiply by length on the x-axis.
		- Because the paper describes this file (SRR039936) as being made up of 100% ERCC, and we are comparing these to the complete ERCC genome, the length  
		- Proof: Using the Supplimentary table 1... ERCC-00073 dot that they mention in plot: concentration = 8.09E-8 and length = 603. 
			- This concentration * length would be = 0.0000487827 = 4.9E-5 which is not the same as what they show in plotC: ~1E-7
			- From my plots, we can see that all points on plotC were not multiplied by the supposedly corresponding ERCC length.  

 - NOTE: When running TopHat v:1.0.13, delete (in my case) the first 2 lines that make up an incorrect "header" created by TopHat. For Cufflinks (new or old), the header for a .sam file is important... Still have not found the infamous parameter in either program to ignore headers in output/input respectively: 
	- Must work on my google-fu...
	- TopHat added these 2 lines to the .sam output file:
		- @HD	VN:1.0	SO:sorted
		- @PG	TopHat	VN:1.0.13	CL:./tophat -p 8 -o /home/ivan/hulk_cleaning/reproducing_paper_results/tuxedo_tophat_cufflinks_scytrim936/Tuxedo/output_tophat_scytrim936_ercc -g 1 -I 999999999 --segment-length 18 /home/ivan/ercc_reference/ercc_genome /home/ivan/data_files/quality_filtering/sickle_result/SCY_TRIM__SRR039936.fastq
	- Used samtools to view the .sam files where this error took place and used the following command to discard these first 2 incorrect header lines from our file:
		-   $	tail -n +3 accepted_hits.sam > new_accepted_hits.sam
		-	$	mv accepted_hits.sam ./incorrect_header_accepted_hits.sam
		-	$	mv new_accepted_hits.sam ./accepted_hits.sam

### Week 13: (11/April-17/April):

 - On Hulk:
	- Ran Scythe and Sickle on SRR039936.fastq
	- Attempting to fix the amount of genes with abundance estimates discarded by TopHat-2.0.13 and Cufflinks-2.2.1...
		- 26 genes missing in final plot: 6 missing in the .sam/.bam file after running TopHat, 20 in the FPKM's found to be significant after running Cufflinks)
	- Successfully running some programs not yet made into modules:
		- FastQC (no --help command for info on how to run and prints a java error if the binary is ran with no input file)
		- SamTools
		- Tuxedo suite (Bowtie, TopHat and Cufflinks - all 3 recent versions and the versions used in "original paper")
		- RNA fastq/fasta quality filtering programs (Scythe and Sickle)

### Week 12: (4/April-10/April):

 - Denied access to Greenfield and emailed the PSC to address this issue.
	- 2 weeks later and still waiting on them to reopen my account...
 - Continuing my efforts to correctly establish the control of the experiment.
	- Switching to the MegaProbe Lab's resource: the Hulk supercomputer 
 - Developed some PBS scripts from memory on Hulk to pick up where I left off on Greenfield: reproducing the results from the "original paper".

### Week 11: (28/March-3/April):

 - Encountered some problems accesing my account on Greenfield. 
 - Talked with Humberto about my "reproduced" plot and how to best replicate Figure 1 plot E if plot C was not exactly identical to the "paper's"...
 - We deduced that we are missing some DE genes in our referenced based assembly...

### Week 10: (21/March-27/March):

 - Spring break/Holy Week...  

### Week 9: (14/March-20/March):

 - Used RStudio to develop some plots to attempt to reproduce the figures in Supplimentary data of the "paper". 
 - Used last Tuxedo (TopHat/Cufflinks) DE gene counts data to reproduce Figure 1 plot C
	- NOTE: x-axis is at a different range (10e-7 to 10e-1) and quite a lot of points are missing on our graph when compared to the original...

### Week 8: (7/March-13/March):

 - Changed the supplimentary file containing the concentration information of ERCC genes: 
	- The .csv file was edited through VI in the Command Line:
		- The first 2 lines (header changed) were modified to facilitate the procedure of accessing the entire columns directly while working in RStudio. The lines now read as follows:
			- BEFORE: 
				- ERCC,Subpool,GenBank[1],DNA,nt,%GC,MW,Pool 14,Pool 15^Mcontrol,,,,,,,nmol/µl,nmol/µl^MERCC-00012,A,DQ883670,Syn[2] ,994,51,"320,263",2.07E-05,2.07E-05^M
			- AFTER:
				- ERCC,Subpool,GenBank[1],DNA,nt,%GC,MW,Pool.14,Pool.15^MERCC-00012,A,DQ883670,Syn[2] ,994,51,"320,263",2.07E-05,2.07E-05^M

### Week 7: (29/Feb-6/March):

 - Documenting correct ERCC.fa to be used...
	- Found at: 
		<https://raw.githubusercontent.com/ririzarr/encodeRNAseqEvaluation/master/spikein.fasta>
			- Supplimentary tableS1 of original paper indicates: 
				"[1] There were multiple disagreements between the GenBank entries and the resequenced RNAs.  See the supplementary alignment file for corrected sequences."
					- The file that is being referenced can be found at: 
						<http://genome.cshlp.org/content/suppl/2011/07/18/gr.121095.111.DC1/ERCC_genbank_alignments.txt>
							- NOTE: Here we can see the result of running the genbank ERCC queries. The subjects (taken as results) are the "multiple disagreements" and are the ones used from here on out. The only diffence I found was with ERCC-00007...  
	- Using a corresponding .gtf file for this ERCC_genome.fa file
		- Found at:
			<https://github.com/ririzarr/encodeRNAseqEvaluation/blob/master/spikein_gene.gtf>
				- NOTE: When downloading this gtf file from the site, please note that additional genes that are not used in our project are added at the end of the file (phiX174, VATG3, etc.). It is important to note that we modified the file after downloading it to remove the lines that describe these genes (last line in our file is now describing ERCC-00171).
				- CHANGE the 5th row of this gtf file to coincide with what was mentioned in the NOTE section above (length of ERCC-00007 was changed).
	- Ran Bowtie/TopHat/Cufflinks for using ERCC_reference genome and gtf files.
		- New parameter added: $ -g 1
			- In the original paper's methodology "ran Bowtie with parameters: -m 1 -v 2"... but because we use Bowtie INSIDE TopHat implementing the --bowtie1 flag for TopHat, we must find and set the same flags/parameters. Following the documentation, the -v 2 parameter is set by default and the value passed through the -g parameter in TopHat sets is used in the -k and -m parameter for bowtie1.
				- The -v parameter sets the possible mismatches allowed in the comparisons...
				- "Specifying -m 3 instructs bowtie to refrain from reporting any alignments for reads having more than 3 reportable alignments."...
					- This example was taken from: <http://bowtie-bio.sourceforge.net/manual.shtml#the-bowtie-aligner>
	
 - Finished Week1 of the online harvard course on statistics and learning the R programming language (Weeks 2-4 left).

### Week 6: (22/Feb-28/Feb):

 - Meeting with Dr. Ricardo Gonzalez of the University of Puerto Rico, Medical Science Campus:
	- Focusing now on the "control" of my experiment, going to try to reproduce the figures/results of referenced based assembly of 'original paper'
 	- Started taking the online harvard course on statistics and learning the R programming language: 
		- Looks fun: <https://www.edx.org/course/data-analysis-life-sciences-1-statistics-harvardx-ph525-1x>

### Week 5: (15/Feb-21/Feb):

 - Ran blastx searches of all 19 DE genes (later determined this to be the wrong BLAST program)
	- Added results to the 'project site'
		- Found Birnavirus and Xvirus genes again...
			- Converted my previous python script to determine if any of the 19 differentially expressed genes appear in Birnavirus and Xvirus genome
		 		- Uploaded python script to project site, code can be found at:  <https://github.com/NacroKill/dmel-ercc-diff/blob/master/Tophat_Birnavirus_Confirmer_2.0.py>
 - Ran nucleotide blast searches of all 19 DE genes 
	- Added results to the 'project site'
	- Re-read paper on synthetic spike-in standards ('original paper')
		- Found at: <http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3166838/>

### Week 4: (8/Feb-14/Feb):

 - Postponing eXpress analysis (after encountering several errors with the module and supporting perl scripts)
 - Ran blastx searches of all 19 DE genes (later determined this to be the wrong BLAST program)
	- Found Birnavirus and Xvirus genes again...
		- Started working on old python script to determine if there are actual viral transcripts BLAST'ed DE genes

### Week 3: (1/Feb-7/Feb):

 - Finished second section of RSEM (gene expression analysis), producing a heat map of 19 'new' differentially expressed genes
 - Attempted abundance estimation and gene expression analysis using eXpress

### Week 2: (25/Jan-31/Jan.):

 - Attempted second section (gene expression analysis) using RSEM
 - Attempted abundance estimation and gene expression analysis using eXpress

### Week 1: (18/Jan-24/Jan.):

 - Finished first section of RSEM (abundance estimation)
 - Reference assembly data ready 

## UPDATE - 1st Semester 2015-2016

 - Finished cleaning original data sequences 
 	- (Code and description of cleaning process to be added later on...)
 - Used new "clean" data to re-run reference based assembly 
 	- Finished running TopHat and Cufflinks programs
 - Attempted to re-run denovo assembly using "clean" data:
 	- Finished running Trinity 
 		- Now moving on to RSEM and eXpress...


