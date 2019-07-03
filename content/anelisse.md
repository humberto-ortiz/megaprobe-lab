Title: Anelisse Dominicci Maura
Date: 2019-06-20
Slug: anelisse
Category: People
Tags: bioinformatics, newbie, roble

# Anelisse Dominicci Maura

## Contact info:
 - e-mail- <anelisse.dominicci@upr.edu>

## Bio:

Hi, my name is Anelisse Dominicci Maura, Im an undergraduate studying Environmental Science,
but im starting to feel love for Computer Science.
So, im thinking on doing a minor in Programming.
Also, I like watching netflix and going to the beach.

## Research Goals

Being part of this internship and part of MegaProbe I hope to learn about bioinformatics.
And in this way, to be able to apply what I have learned to my future,
and eventually to be able to help people.

## Research Description

The project consists of analyzing 4-shotgun datasets of the microbial community in the rhizospheres,
from the *Tabebuia heterophylla* (that is a "roble").
This "robles" are located in 4 diffrent places in Puerto Rico:
Cabo Rojo, Guayama, Guánica,and Maricao,
and from 3 different type of soil: volcanic, karst and serpentine.

## Weekly UPDATES

### Week 4: (24-28, 6, 2019)
  -We had some trobles downloading the data, but we finally DID IT!!!
  -We run the command "fastq-dump", to compress the files.
  -Then we run "FASTQC" to see the quality of each samples.
```
#!/bin/bash
#SBATCH --mem-per-cpu=512
#SBATCH --time=48:00:00
#SBATCH --job-name=fastqc-qc
#SBATCH --mail-user=anelisse.dominicci@upr.edu
#SBATCH --mail-type=ALL
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8

# Load project
source /home/humberto/adominicci/miniconda3/etc/profile.d/conda.sh
conda activate roble

fastqc --threads=8 -outdir=trim *.qc.fq.gz
```
-Then we run "MULTIQC" to see the general quality of all samples.
-We decided to do a trim with quality of 5.
-Also eliminating the adapters, since in the reports the quality said that there was an overrepresented sequence.
```
#!/bin/bash
#SBATCH --mem-per-cpu=1024
#SBATCH --time=48:00:00
#SBATCH --job-name=Trimmomatic
#SBATCH --mail-user=anelisse.dominicci@upr.edu
#SBATCH --mail-type=ALL
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8

# Load project
source /home/humberto/adominicci/miniconda3/etc/profile.d/conda.sh
conda activate roble

# Delete any old orphan reads
rm -f orphans.qc.fq.gz

for filename in *_1.fastq.gz
do
  # first, make the base by removing fastq.gz
  base=$(basename $filename .fastq.gz)
  echo $base

  # now, construct the R2 filename by replacing R1 with R2
  baseR2=${base/_1/_2}
  echo $baseR2

 # finally, run Trimmomatic
  trimmomatic PE -threads 8 ${base}.fastq.gz ${baseR2}.fastq.gz \
    ${base}.qc.fq.gz s1_se \
    ${baseR2}.qc.fq.gz s2_se \
    ILLUMINACLIP:Combinados:2:40:15 \
    LEADING:5 TRAILING:5 \
    SLIDINGWINDOW:4:5 \
    MINLEN:25

  # save the orphans
  gzip -9c s1_se s2_se >> orphans.qc.fq.gz
  rm -f s1_se s2_se
done


Adapters:

>PrefixIndexR1
AGATCGGAAGAGCACACGTCTGAACTCCAGTCA
>PrefixIndexR2
AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT
>PrefixIndexR1rev
TGACTGGAGTTCAGACGTGTGCTCTTCCGATCT
>PrefixIndexR2rev
ACACTCTTTCCCTACACGACGCTCTTCCGATCT
```
-When this was fianlly done, we run again the "FastQC" and the "MULTIQC" and the reports WERE GREAT!!!! so we decided to start doing the assemblies with 3 differents assemblers.
-We used Megahit:
```
#!/bin/bash
#SBATCH --mem-per-cpu=15000
#SBATCH --time=48:00:00
#SBATCH --job-name=megahit
#SBATCH --mail-user=anelisse.dominicci@upr.edu
#SBATCH --mail-type=ALL
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8

# Load project
source /home/humberto/adominicci/miniconda3/etc/profile.d/conda.sh
conda activate roble

#echo ~/miniconda3/pkgs/megahit-1.0.3-0/megahit -1 $(ls *_1.qc.fq.gz | tr '\n' $

/home/humberto/adominicci/miniconda3/pkgs/megahit-1.0.3-0/megahit \
  -1 SRR5256888_1.qc.fq.gz,SRR5256985_1.qc.fq.gz,SRR5256987_1.qc.fq.gz,SRR52569$
  -2 SRR5256888_2.qc.fq.gz,SRR5256985_2.qc.fq.gz,SRR5256987_2.qc.fq.gz,SRR52569$
  -o megahit_out -t 8
```
-We also used PLASS:
```
#!/bin/bash
#SBATCH --mem-per-cpu=640
#SBATCH --time=48:00:00
#SBATCH --job-name=plass
#SBATCH --mail-user=anelisse.dominicci@upr.edu
#SBATCH --mail-type=ALL
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8

# Load project
source /home/humberto/adominicci/miniconda3/etc/profile.d/conda.sh
conda activate roble


plass assemble SRR*_[12].qc.fq.gz assembly.fas tmp

```
-And finally we used MetaSPAdes:
```
#!/bin/bash
#SBATCH --mem-per-cpu=16000
#SBATCH --time=48:00:00
#SBATCH --job-name=metaspades
#SBATCH --mail-user=anelisse.dominicci@upr.edu
#SBATCH --mail-type=ALL
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8

# Load project
source /home/humberto/adominicci/miniconda3/etc/profile.d/conda.sh
conda activate roble

metaspades.py -o metaspades_out --pe1-1 left.fq.gz --pe1-2 right.fq.gz
```
-The 3 assemblies failed, because they required more memory, than the one we put each script to make the assembly. So we did a "Digital Normalize" to reduce the data a little bit, so we can run all the assembler again. We did a first script and we forgot to put --gzip and --no-reformat (so when we runned again, it doesn't change the names of the sequences, nor check if they are paired sequences. So I put the script with the corrections:
```
#!/bin/bash
#SBATCH --mem-per-cpu=1024
#SBATCH --time=48:00:00
#SBATCH --job-name=interleave
#SBATCH --mail-user=anelisse.dominicci@upr.edu
#SBATCH --mail-type=ALL
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8

# Load project
source /home/humberto/adominicci/miniconda3/etc/profile.d/conda.sh
conda activate roble

for filename in *_1.qc.fq.gz
do
  # first, make the base by removing fastq.gz
  base=$(basename $filename _1.qc.fq.gz)
  echo $base

# finally, run interleave-reads.py
  interleave-reads.py --no-reformat --gzip -o ${base}.pe.qc.fq.gz ${baseR1}.qc.$
done

```
-So now we are waiting for that task to be over, to see if we can run the assemblers.
-Also during the week we found the assemblies of the project, done by others persons in IMG.

### Week 1: (3-7, 6, 2019)
  - I was doing the Software Carpentry Workshop.

### Week 2: (10-14, 6, 2019)
  - I was reading papers and protocols, to learn about the research and different programs we are going to use.
  - I wrote a research summary, like a proposal to know what are the next steps.

### Week 3: (17-21, 6, 2019)
  - We are downloading the data from NCBi, to Boqueron. We are still waiting.
