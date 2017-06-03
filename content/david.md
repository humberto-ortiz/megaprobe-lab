Title: David John Ortiz Rivera
Date: 2016-09-02
Category: People
Tags: DGE, RNA Seq, Bioinformatics, Cave Fishes, Salmon, EdgeR

# Short Bio:
  
   Greetings, my name is David John Ortiz Rivera. I was born one august day in Bayamon, Puerto Rico, but raised in Morovis.
   Currently a 4th year undergrad student at the University of Puerto Rico, Rio Piedras. I'm primarily interested in programming, video games, music, films, and science (somewhat).
   In the future I like to be involved in the areas of hardware repair, cybersecurity, software engineering, videogame development, and web development.
# Contact:

  + e-mail: david.ortiz11@upr.edu
  + Github: https://github.com/kytrnd
  
# Research Goals:
  
  + Find if there is any gene convergence for 3 lineages of cave fishes (Stygi, Sino, Astyanax).
  + Find DGE using RNAseq from Salmon
  + Complete this semester's project

# Research Description:

### Phylogeny Project description:

+ Working under the supervision of Prof. Humberto Ortiz Zuazaga, Ricardo Betancourt,
  and Dahiana Arcila I was trying to find Diferential Expressions from different 
  species of fishes (Astyanax, Styygicthys, Sinocheilus) through data obtained from transcriptomics 
  to determine if there is any genetic convergence.

+ step 1 : de novo assembly on Stygicthys raw data files using Trinity.
+ step 2 : mapping our assembled files against 14,000 transcriptomes using bowtie2.
+ step 3 : obtain our sam output and convert it into quantification tables using RSEM.
+ step 4 : Visualize our DGE data to determine if there is any convergence between these species using eBseq or edgeR.
+ more on this here: https://github.com/kytrnd/Bioinformatics .
+ Quantification and Differential Expression of RNAseq with salmon (more on this soon):
++ http://2016-aug-nonmodel-rnaseq.readthedocs.io/en/latest/quantification.html.
  
# Weekly Reports:

## Second Semester (2016-2017)

### Weeks 29, 30, 31, 32, 33, 34, 35, & 36 (14th of April, 2017 to 9th of June, 2017)
  
  + Walter's script didn't work.
  + Managed to produce the MA plots for 2D, 6D & 20D post injury VS uninjured (norm)
    by creating my own scripts.
  + All that is left is to analyze my results, make sure that this is all I need to write my official report.
  + Started to write my draft report, will be done in a week or two.
  + Met with Dahiana to see if we could finish our fish project, but have not heard any more from her.
  + Have not yet met with my PI, will figure that out very soon. 
  + Weekly progress for the 8 weeks, I'd say about 20/100.

### Weeks 25, 26, 27, & 28 (17th of March, 2017 to 14th of April, 2017)

  + Data was normalized. Size went from 80G to 26G while using k = 20.
  + Single-end assembly using Trinity, done.
  + Walter created some scripts for indexing and quantifying using Salmon
  , but I had to troubleshoot and correct them multiple times.
  + Managed to get the Salmon index of the assembled pepino transcriptome using k = 31.
  + Ran the quantifying script using quasi mapping, recieved a warning from Salmon saying
  that some percentage (can't remember) wasn't able to map, due to k size.
  + Re-ran indexing and quantifying scripts, this time with k = 21, no warnings this time.
  + Salmon ran very fast, indexing I'd say took maybe 5 minutes while quantifying 12 files one after another
  took 20-25 mins.
  + With the 12 count files all that is left is visualize the data.
  + Extracted the name and count columns from each 12 files, to create 12 corresponding. These can be used as input for edgeR.
  + Got stuck trying to use Titu's script, but managed to produce the MDS of the 12 files and the MA plot of 2 random groups.
  + Consulted with Prof. Ortiz and now that we have the group data, we can create the MA plots of 2D, 6D & 20D post injury VS uninjured (norm). There are other groups that I don't know how to visualize, hopefully will find out eventually.
  + Walter is currently doing the MA plot scripts.
  + Almost done.
  + Weekly progress for the 4 weeks, I'd say about 60/100.

### Week 24 (10th of March, 2017 to 17th of March, 2017)

  + Re-trimmed data.
  + Hopefully normalizing by tuesday & assembling by wednesday.
  + Weekly progress rating 0/100.

### Week 23 (3rd of March, 2017 to 10th of March, 2017)

  + Still troubleshooting pipeline.
  + Normalizing script seems to be the most troublesome.
  + Weekly progress rating 0/100.

### Week 22 (24th of February, 2017 to 3rd of March, 2017)

  + Gave my paper presentation.
  + Recieved pipeline, started modifying it for our data but it didn't work.
  + Troubleshooting pipeline, no luck.
  + Weekly progress rating 0/100.

### Week 21 (17th of February, 2017 to 24th of February, 2017)
  
  + Reading Salmon paper.
  + Waiting on partner to create a pipeline for the data.
  + Weekly progress rating 0/100.

### Week 20 (10th of February, 2017 to 17th of February, 2017)

  + Downloaded multiple versions of the raw data (12 files in total, around 83GB).
  + Suspicious size between the data that was in NCBI and the one downloaded on hulk.
  + Trimmed all 12 files, only reduced the total size to 80GB. Not sure if it's good or bad.
  + Waiting on lab partner for data normalizing scripts.
  + Dissecting the salmon paper as we speak.
  + Weekly progress rating 60/100.

### Week 19 (3rd of February, 2017 to 10th of February, 2017)

  + Completed the Titus' tutorial on Salmon.
  + Started reading Salmon titled Salmon: Accurate, Versatile and Ultrafast Quantification from RNA-seq Data using Lightweight-Alignment.
  + Weekly progress rating 20/100.

### Week 18 (27th of January, 2017 to 3rd of February, 2017)

  + Updated my markdown.
  + Started reading Titus' workshop on DGE using Salmon.
  + Installed Salmon
  + Weekly progress rating 20/100.

### Week 17 (20th of January, 2017 to 27th of January, 2017)

  + Nothing.
  + Weekly progress rating -100/100.

### Week 16 (18th of January, 2017 to 20th of January, 2017)

  + Nothing.
  + Weekly progress rating -100/100.

##First Semester (2016-2017)

### Week 15 (2nd of December, 2016 to 9th of December, 2016)

  + STILL have not heard from instructor on what will be my next step.
  + Nothing.
  + Weekly progress rating -100/100.

### Week 14 (25th of November, 2016 to 2nd of December, 2016)

  + Have not heard from instructor on what will be my next step.
  + Nothing.
  + Weekly progress rating -100/100.

### Week 13 (18th of November, 2016 to 25th of November, 2016)

  + Moved data to instructor's cluster for mapping and quantification using Bowtie-2 & RSEM.
  + Tried some scripts, no luck. Waiting on problems to be investigated.
  + Weekly progress rating 1/100.

### Week 12 (11th of November, 2016 to 18th of November, 2016)

  + Changing our current mapping/quantification method (hopefully for the best).
  + Encountered problems with our mapping method for reasons unknown.
  + Weekly progress rating 0/100. 
  
### Week 11 (4th of November, 2016 to 11th of November, 2016)

  + Mapping using Bowtie-2, created only 2 files (out of 5).
  + Weekly progress rating 40/100. 

### Week 10 (28th of October, 2016 to 4th of November, 2016)

  + Currently re-running all my scripts to avoid corrupted data.
  + All scripts produced a Trinity.fasta file.
  + Waiting on my instructor for further work.
  + Some extra website work :(.
  + Weekly progress rating 30/100.

### Week 9 (21st of October, 2016 to 28th of October, 2016)
  
  + Analyzed some read statistics withthe use of Transrate. Some flags popped up (low mapping percentege, size of largest contig).
  + Technical report
  + Website duty
  + Weekly progress rating 45/100.
  
### Week 8 (14th of October, 2016 to 21st of October, 2016)
  
  + Started running the remaining scripts + re-ran the first 2 individuals.
  + Currently waiting on first individual assembly to finish.
  + Re-Running fastq-dump scripts.
  + Weekly progress rating 100/100 (My work here is done, everything else is frosting on the cake).

### Week 7 (7th of October, 2016 to 14th of October, 2016)
  
  + Troubleshooting error with Individual03. Turns out that Trinity needed a large amount of RAM (256G).
  + Started running the following scripts: Individual03, Tissue01.
  + Weekly progress rating 70/100.

### Week 6 (30th of September, 2016 to 7th of October, 2016)
  
  + Ran first Trinity script in hulk using screen commands. It was somewhat a success.
  + Started scripts for Individual02 & Individual03. Succeded only with Individual02.
  + Weekly progress rating 30/100. 

### Week 5 (23rd of September, 2016 to 30th of September, 2016)
  
  + Installed Trinity in my Makaira directory (with the help of Humberto) to avoid further problems.
  + Moved my data to HULK.
  + Weekly progress rating 20/100. 

### Week 4 (16th of September, 2016 to 23rd of September, 2016)
  
  + Makaira's Trinity kept encountering errors due to the lack of plugins.
  + Managed to download 2 Astyanax and 4 Cave/Surface fish Transcriptome files for future work.
  + Power outtage suspended all lab work after Wednesday.
  + Weekly progress rating 20/100.

### Week 3 (9th of September, 2016 to 16th of September, 2016)
  
  + Finally met with instructor (important).
  + Took Trinity tutorial.
  + I was given data and a reference script to start assembly.
  + Created 7 scripts based on reference script and tinkering.
  + Created additional script to download cavefish and surface fish data from SRA.
  + Sadly, Trinity needs some plugins installed and SRA needs to be installed on Makaira
     for me to be able to use my scripts.
  + Weekly progress rating 30/100. 

### Week 2 (2nd of September, 2016 to 9th of September, 2016)
  
  + Instructor was absent this week.
  + Introduced to an Exon Capture project I'll be working on in the future.
  + Sadly no progress (again).

### Week 1 (26th of August, 2016 to 2nd of September, 2016):
  
  + Recieved instructions to start gathering 'raw data' on different
      species of cave fishes.
  + Obtained data from NCBI, currently waiting on confirmation from
      my instructor if it's correct to proceed with assembling.
  + Sadly no progress.
