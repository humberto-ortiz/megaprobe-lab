Title: Israel O. Dilán Pantojas
Date: 2016-01-22
Modified: 2016-01-30
Slug: israel
Category: People
Tags: de-novo


# Bio:

 I confess my crimes against humanity and Eleutherodactylus coqui races alike, for I have vanquished the furious lab frog.
 > Now, I am become Death, the destroyer of worlds.
    J.R. Oppenheimer

## Contact info:

 - e-mail - <israelodilan@gmail.com>
 - Github - <https://github.com/Omig12/>


[![Seriously!](https://s-media-cache-ak0.pinimg.com/564x/2e/b4/63/2eb4631511b658d831ee851538d0673b.jpg)] 

# Research Goals

  Create and Analyse correctly obtained De Bruijn graphs from de novo sequence assemblies utilizing mutual.

## Weekly UPDATE

### Week 1: (19-22/Jan)

 - Started reading up on de novo sequencing and familiarizing with the terms used around it.

### Week 2: (25-29/Jan)

 - Installed required programs (velvet/oases) to test out mutual.
 - Aquired Sample Data Set of Nematostella Embryonic Transcriptome (Starlet sea anemone). <https://darchive.mblwhoilibrary.org/handle/1912/5613>
 - Working on glossary of Bioinformatics related terms.
 - Continued reading up on de novo sequences, mutual/velvet/oases and de Bruijn Graph assembly of short reads.
 - Test ran mutual.

### Week 3: (1-5/Feb)

 - Initiated test running of mutual on local (DELL Inspiron 7548) machine, utilizing sample Sea Anemone Dataset. 
    - Estimated run-time: 72 hour.
    - Expected output: A transcript with very long contigs due to the high similarity of the two test organisms.
    - Results: Two empty output files. >:'(
    - Possible issues: Computer might not meet requirements to performs such heavy work very efficiently.
    - Path of action: Proceeded to move operations elsewhere, The University of Puerto Rico's Computer Science Department very own Hulk. 
 - Rest of the week(get it?) due too health problems.

### Week 4: (8-12/Feb)
 - Setting up Hulk server to run mutual. (Still missing velvet)
    - Battled with Hulk to run mutual.
    - Led to a crash :'( after two days of work.
 - Finally got it down, ran mutual and got some output.
 - Initiated analyzing phase, todo:
    - Verify Mutual's output utilizing blast <http://blast.ncbi.nlm.nih.gov/Blast.cgi> and blastn <http://genome.jgi.doe.gov/pages/blast-query.jsf?db=Nemve1> 
    - Clean up initial data by removing adapters using Sickle and Scythe <http://bioinformatics.ucdavis.edu/research-computing/software/>.
    - Visualize mutual ouputs with the help of bandage <https://github.com/rrwick/Bandage>.
 - Started working on a more readable and reproductible version of the documentation for this reasearch. 

### Week 5: (15-20/Feb)
 - Worked on creating research documentation and a research log:
    - Wrote FAQ to help ease the reproduction of this research.
 - Experienced many issues syncing local and remote git repo.
 - Verified Mutual's output using two different blast services both returned correctly identified nemastotella similarity.
 - Verified Quality of input files using FastQC, file are very high quality reads.
 - Todo:
    - Visualize contigs using Bandage.
    - Trim illumina adapters from input sequences.

### Week 6: (22-26/Feb)
 - Fougth with git and github's repos in an effort to sync files, failed.
    - Switching strategy: Prioritizing some file to be copied and leaving other ones behind stored only locally in both hulk and personal machine.
 - Installed Scythe and Sickle.
 - Graphed Contigs from velvet's Lastgraph utilizing Bandage.
 - Local Computer's Ubuntu OS broke  (RIP) :'(  Thankfully to prior advice given in a lab meeting, had created multiple back ups of research data.
 - Read a few more papers concerning bioinformatics and its history.

![Bandage graph of velvet/oases output.]({filename}images/contigs_graph.png)
![Starlet Sea Anemone for comparisson.] (http://www.kahikai.org/images/embryology_development/nv.jpg)

### Week 7: (29/Feb-4/Mar)
 - Reinstalled Ubuntu. :'D (So shinny!)
 - Updated Weekly.
 - Many a exams this week.
 - Began reading "The Cartoon Guide To Genetics" by Larry Gonick & Mark Wheelis.
 - Analyse best way to compare outputs from velvet/oases and mutual.
    - Options:
        - Find a way to graph mutuals output compare graphs with velvet's.
            - Also posibly compare with output of other that does analysis between multiple organisms.
        - Utilize blast to compare each contig.
        - Utilize clustel to compare contig alingment.
 - Still to do:
    - Remove Adapters with Scythe.
    - Trim edges with Sickle.

### Week 8: (7-11/Mar)
 - Git repo is finally in order. :)
 - Finally got to quality trimming:
    - Needed Illumina Adapters FASTA files to remove adapters, found them in Trimmomatic source code. <http://www.usadellab.org/cms/?page=trimmomatic>
    - Helpful note utilize FastQC to help determine how to quality control your reads. Especially figuring out the encoding.
    - Apparently scythe supports gunzipped fastq files.
 - Finally removed Adapters
 - Finally trimmed Edges
 - Created quality reports using FASTQC for each step.
 - To do:
    - Verify if quality can be further improved.
    - Re-run mutual with clean data and graph outputs
    - Close to source code examination.

### Week 9: (14-18/Mar)
 - Ran clean data through Velvet/Oases.
 - Graphed Output of Organism A.
    - Noticeable results on graph.
 - Preparing to run files on mutual.
 - Student assembly paralized work.

![Bandage graph of velvet/oases output.]({filename}images/NewContigs_graph.png)

### Week 10: (21-25/Mar)
 - Holy Week/Spring break.

### Week 11: (28/Mar-1/Apr)
 - Utilized Bandage to create a few graphs of interesting contiguous nodes.
 - Experimented a few forms of output including GFA extensions to graph.
 - Started reading up on parsers for fasta/fastq files. Using Biostars <https://www.biostars.org/p/710/> Guides  and Nacrokill's <https://github.com/NacroKill/dmel-ercc-diff/blob/master/Tophat_Birnavirus_Confirmer_2.0.py> parsers for referrence.
 - Taking a bit of a break many exams this and the next week.

### Week 12: (4-8/Apr)
 - Many evaluations this week also :'(, worked mostly on preparing a bioinformatics presentation that aids in explaining Mutual's Heuristic Pairwise Alignment algorithm implementation.
 - Was corrected by profesor need to parse Velvelt's lastgraph file (that is to say it's De-Bruijn graph), not the fasta/fastq file.
 - Good news everyone! Found a lastgraph parser in writen Ruby. Bad news everyone! I don't understand ruby. :{
 - Tried to ran Mutual but The Hulk(server) is down.
 - To do:
    - Turn to Velvet/Oases De-Bruijn parser.
    - Need to run clean data on Hulk.

### Week 13: (11-15/Apr)
 - Hulk got back up (still has some fight left).
 - Ran Mutual twice simultaneously:
  - A) With the purpose of comparing organism's A (input velvet/oases output [velvetA]) De-Bruijn graph with organism's B (input velvet/oases output [velvetB]) De-Bruijn graph after the data had been cleaned with sickle and scythe.
  - B) With the purpose of comparing organism's A with organism's A (self comparison) expecting duplicate output from Mutual (outputa.fa = outputb.fa).
 - Created a database using Blast's formatdb on Mutual's output (outputa.fa) to compare other .fa files against it.
 - Blasted through Mutual's output (outputa.fa) database against Velvet's ouput (contigs.fa)
 - Blasted through Mutual's output (outputa.fa) database against Mutual's ouput (outputb.fa)
 
### Week 14: (18-22/Apr)
 - Started working on LastGraph parser in python:
    - Reads file
    - Finds NODE
        - Appends to list
    - Finds ARC
- To do:
  - Write all contigs obtained from De-Bruijn
  - Determine format for output
