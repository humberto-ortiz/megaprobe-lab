Title: Frequently Asked Questions
Date: 2016-02-23
Modified: 2016-03-11
Slug: FAQ
Category: Projects
Tags: de-novo


FAQ:

1. What is the aim of your research?
    The goals of our research are to validate and possibly improve Mutual's de Bruijn Graph comparison method to detect mutual contigs shared by two different organism.

2. What have you found out so far?
	Comparing two different reads (Fastq files) from the same organism (Startle Sea Anemone) with mutual* and runnings its output with blast to NCBI's and JGI databases reavealed that the results were correctly identified as Nemastotella Venectis (Starlet Sea Anemone).  

	* Read quality had not been checked, edges had not been trimmed and illumina adapters were still present. 

3. What can I do to reproduce your research?
	Follow the steps in this FAQ and the README file in this directory.

4. What software bundle are you using?
    Mutual,  which also requires both Velvet and Oases.
    We are also employing Bandage, Blast, Scythe, Sickle and FastQC.

5. What is the role of each program?
    Velvet: is employed to hash and graph an RNA sequence.
    Oases:
    FastQC: is used to verify quality of input data.
    Blastn: to validate our output.
    Bandage: to visually Graph contigs.

6. Where can I get them or run them?
    Git clone the following repositories:
        Oases:  <https://github.com/dzerbino/oases>
        Velvet: <https://github.com/dzerbino/velvet>

    Download and install:
        Blast:  <http://www.ncbi.nlm.nih.gov/guide/howto/run-blast-local/>
        FastQC: <http://www.bioinformatics.babraham.ac.uk/projects/fastqc/>
        Mutual: <http://faculty.cse.tamu.edu/shsze/mutual/>

7. What can I do if I encounter problems during installation?
	There are a few things to try:
		1. Make sure to carefully follow the installation instructions in every readme file for each software. 
		2. Google the trouble or error code returned by the compiler.
		3. Visit the software developers website and try to figure out if anyone had the same issue before and how they solved it.
		4. Write an email to megaprobe-lab, explaining the issue in detail, so that we can try to help. 

8. What should I do first after everythings installed?
	Get fastq files of your desired organisms to compare.
		
9. Where can I get them?
	There are actually a few 	
10. Got the fastq files. What's next? 
	Run them through fastqc to check the quality of the reads.

11. The reads are of good quality, now what?
	Remove adapters and trim edges utilizing Scythe(Remove Adapters) and Sickle(Trim EDGES).

12. Which should I do first?
    It's prefferable to fisrt remove adapters and then trim the edges.
    In other words first run scythe and then run sickle.

13. How can I go about runing scythe?
    Understanding the quality of your input files is essential for this task, therefore run your input files through FASTQC.
    Use the basic information to identify the adapter enconding an use it in your input for scythe.

14. 
