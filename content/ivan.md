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


 - The 2nd Semester 2016 workplan can be found at:

	-  <https://github.com/NacroKill/dmel-ercc-diff/blob/master/ILJR_2016_RISE_Workplan.pdf>

## UPDATE - 1st Semester 2015-2016

 - Finished cleaning original data sequences 
 	- (Code and description of cleaning process to be added later on...)
 - Used new "clean" data to re-run reference based assembly 
 	- Finished running TopHat and Cufflinks programs
 - Attempted to re-run denovo assembly using "clean" data:
 	- Finished running Trinity 
 		- Now moving on to RSEM and eXpress...

## Weekly UPDATE - 2nd Semester 2015-2016

 	- DISCLAIMER: All programs mentioned below were ran on PSC's Greenfield (R.I.P. BLACKLIGHT)
 		- List of PSC hardware: https://www.psc.edu/index.php/data-exacell/hardware-infrastructure

### Week 1: (18/Jan-24/Jan.):

	- Finished first section of RSEM (abundance estimation)
	- Reference assembly data ready 

### Week 2: (25/Jan-31/Jan.):

	- Attempted second section (gene expression analysis) using RSEM
	- Attempted abundance estimation and gene expression analysis using eXpress

### Week 3: (1/Feb-7/Feb):

	- Finished second section of RSEM (gene expression analysis), producing a heat map of 19 'new' differentially expressed genes
	- Attempted abundance estimation and gene expression analysis using eXpress

### Week 4: (8/Feb-14/Feb):

	- Postponing eXpress analysis (after encountering several errors with the module and supporting perl scripts)
	- Ran blastx searches of all 19 DE genes (later determined this to be the wrong BLAST program)
		- Found Birnavirus and Xvirus genes again...
		 		- Started working on old python script to determine if there are actual viral transcripts BLAST'ed DE genes

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


### Week 6: (22/Feb-28/Feb):

	- Meeting with Dr. Ricardo Gonzalez of the University of Puerto Rico, Medical Science Campus:
		- Focusing now on the "control" of my experiment, going to try to reproduce the figures/results of referenced based assembly of 'original paper'
	- Started taking the online harvard course on statistics and learning the R programming language: 
		- Looks fun: <https://www.edx.org/course/data-analysis-life-sciences-1-statistics-harvardx-ph525-1x>


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

### Week 8: (7/March-13/March):

	- Changed the supplimentary file containing the concentration information of ERCC genes: 
		- The .csv file was edited through VI in Command Line:
			- If viewed using Microsoft Office Excel, the first 2 lines changed:
				- FROM: 
					- ERCC,Subpool,GenBank[1],DNA,nt,%GC,MW,Pool 14,Pool 15^Mcontrol,,,,,,,nmol/µl,nmol/µl^MERCC-00012,A,DQ883670,Syn[2] ,994,51,"320,263",2.07E-05,2.07E-05^M
				- TO:
					- ERCC,Subpool,GenBank[1],DNA,nt,%GC,MW,Pool.14,Pool.15^MERCC-00012,A,DQ883670,Syn[2] ,994,51,"320,263",2.07E-05,2.07E-05^M

### Week 9: (14/March-20/March):

	- Used RStudio to develop some plots to attempt to reproduce the figures in Supplimentary data of the "paper". 
	- Used last Tuxedo (TopHat/Cufflinks) DE gene counts data to reproduce Figure 1 plot C
		- NOTE: x-axis is at a different range (10e-7 to 10e-1) and quite a lot of points are missing on our graph when compared to the original...

### Week 10: (21/March-27/March):

	- Spring break/Holy Week...  

### Week 11: (28/March-3/April):

	- Encountered some problems accesing my account on Greenfield. 
	- Talked with Humberto about my "reproduced" plot and how to best replicate Figure 1 plot E if plot C was not exactly identical to the "paper's"...
	- Deduced we are missing some DE genes in our referenced based assembly...

### Week 12: (4/April-10/April):

	- Denied access to Greenfield and emailed the PSC to address this issue.
		- 2 weeks later and still waiting on them to reopen my account...
	- Continuing my efforts to correctly establish the control of the experiment.
		- Switching to the MegaProbe Lab's resource: the Hulk supercomputer 
	- Developed some PBS scripts from memory on Hulk to pick up where I left off on Greenfield: reproducing the results from the "original paper".

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

### Week 14: (18/April-24/April):



