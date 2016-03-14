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
	- Started online harvard course on statistics and learning the R programming language: 
		- Looks fun: <https://www.edx.org/course/data-analysis-life-sciences-1-statistics-harvardx-ph525-1x>


