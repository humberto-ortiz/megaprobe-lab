Title: Frequently Asked Questions
Date: 2016-02-23
Modified: 2016-08-27
Slug: FAQ
Category: Projects
Tags: de-novo


FAQ:
====

1. **What is the aim of your research?**
    * The goals of our research are to validate and possibly improve Mutual's de Bruijn Graph comparison method to detect mutual contigs shared by two different organism.

2. **What have you found out so far?**
    * Comparing two different reads (Fastq files) from the same organism (Starlet Sea Anemone) with Mutual and running it's output with __NCBI's Blast__ against _NCBI_ and _JGI_ databases revealed that the transcrips identified by Mutual as similar sequences found in both organisms were correctly identified as Nemastotella Venectis (Starlet Sea Anemone). So at least we know although we are utilizing _de novo_ method to assemble the transcrips at least some of the genomic data manages to retain it's integrity.
      - Read quality had not been checked, edges had not been trimmed and illumina adapters were still present, which messed up some of the output.

3. **What can I do to reproduce your research?**
    * Follow the steps in this FAQ and the README file in this directory/repositories: <https://github.com/humberto-ortiz/megaprobe-lab/blob/master/content/Mutual_Files/Works>.
      - If you happen to encounter any problems during installation please suggest edits to the [Issues.md](https://github.com/humberto-ortiz/megaprobe-lab/blob/master/content/Mutual_Files/Works/Issues.md) file. _Include any steps taken to solve it._

4. **What software bundle are you using?**
    * Mutual,  which also requires both Velvet and Oases. We are also employing Bandage, Blast, Scythe, Sickle and FastQC.

5. **What is the role of each program?**

   * **_Velvet & Oases_** are employed to hash and graph an RNA sequence.
   * **_FastQC_** is used to verify quality of the data.
   * **_Blast_** is used to validate our output and also to directly compare sequences.
   * **_Bandage_** to visually graph contigs.
   * **_Scythe_** trims out the bases that contain adapter sequences.
   * **_Sickle_** trims out the bases from the reads that are identified to be of poor quality by the sequencer.

6. **Where can I get them or run them?**

   Git clone the following repositories:
    * Oases:  <https://github.com/dzerbino/oases.git>
    * Velvet: <https://github.com/dzerbino/velvet.git>
    * Bandage: <https://github.com/rrwick/Bandage.git>
    * Scythe: <https://github.com/vsbuffalo/scythe.git>
    * Sickle: <https://github.com/najoshi/sickle.git>
   Download and install:
    * Blast:  <http://www.ncbi.nlm.nih.gov/guide/howto/run-blast-local/>
    * FastQC: <http://www.bioinformatics.babraham.ac.uk/projects/fastqc/>
    * Mutual: <http://faculty.cse.tamu.edu/shsze/mutual/>

7. ** What can I do if I encounter problems during installation?**
    * There are a few things to try:
        1. Make sure to carefully follow the installation instructions in every readme file for each software. 
        2. Google the trouble or error code returned by the compiler.
        3. Visit the software developers website and try to figure out if anyone had the same issue before and how they solved it.
        4. Write an email to megaprobe-lab, explaining the issue in detail, so that we can try to help. 

8. **What should I do first after everything is installed?**
    * Get read data files in ".fastq" file format of the organisms you want to compare.

9. **Where can I get them?**
    * There are actually quite a few places where you can find RNA-Seq data, my suggestion is to google the name of the organism + "rna seq data".
        * _This does not guarantee good quality reads nor good information of where the reads came from, so be sure to pick a source you trust._
    * The data utilized in this repo can be found in:
        + Starlet Sea Anemone: <https://darchive.mblwhoilibrary.org/handle/1912/5613>

10. **Got the fastq files. What's next?**
    * Make a copy of them, remember not to edit the original ones.
    * Run the copies through FastQC to check the quality of the reads.

11. **The reads are of acceptable quality, now what?**
    * Now you need to quality control them:
        1. Remove adapters and trim edges utilizing Scythe(Remove Adapters) and Sickle(Trim EDGES).
        2. Run them through FASTQC
        3. Tweak paramenters and repeat until satisfied with the quality of the reads.

12. **Which should I do first?**
    * It's prefferable to fisrt remove adapters and then trim the edges. In other words first run scythe and then run sickle.

13. **How can I go about runing scythe?**
    * Understanding the quality of your input files is essential for this task, therefore run your input files through FASTQC.
    * Use the basic information to identify the adapter enconding an use it in your input for scythe.

14. **I've cleaned the data a few times but i'm still not happy with the results, what can I do?**
    * Look into digital normalization, Dr. C. Titus Brown has a few good articles about it so go check them out first.

15. **Ok, I'm happy with my data, what now?**
    * First run it through Velvet and Oases to create a De Bruijn graph for each organism you wish to compare.

16. **So, how do I do that?**
    * You should read the documentation for the programs but you can also use the [data_prep.sh scripts](./data_prep.sh) in this repo.
        * _If you encounter any problems please remember to report them in issues._

17. **Now I have a VelvetA & a VelvetB directories, and now Mutual right?**
    * Yes, again you should read the .... nevermind edit the [mutual.sh script](./mutual.sh) to your needs and then run it.

18. **Can I study the assembly, without running them through Mutual?**
    * Yes, just look through the files in VelvetA or VelvetB and maybe even graph them with Bandage.

19. **Mutual is done running, now what?**
    * Congratulations! Check the outputa.fa and outputb.fa files for the results of the comparison. Analyze the data and keep on improving the methods.

20. **Can I give any suggestions?**
    * No! Well actually yes and please do. Any comments or suggestions will be greatly appreciated.
