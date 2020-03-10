Title: Anelisse Dominicci Maura
Date: 2019-06-20
Slug: anelisse
Category: People
Tags: bioinformatics, newbie, roble

# Anelisse Dominicci Maura

## Contact info:
 - e-mail- <anelisse.dominicci@upr.edu>
 - LinkedIn-  <https://www.linkedin.com/in/anelisse-dominicci-maura-386554189/>

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
### Week 8: (22-26, 7, 2019)
- The load-graph script failed because it ran out of time.
- As we need to have results for the presentation that I have to give about what this summer was done and what we have achieved, we gave it a stop. 
- Therefore, we decided to export the data of the assemblies that we had found in IMG, and we decided to analyze them.
- We used R to analize the data, we found 2 domains, 274 between phylums and orders, and 508 families.
- We decide to took the 5 more represented family of each sample. We found out that the phylum that was more present in each sample was the Actinobacterias.
- We did plot with ggtree and ghitmap to represnt our results. <https://github.com/essilena/Analyzing-Roble>
- I did the presentation, with all we had done and all the results we got.

### Week 7: (15-19, 7, 2019)

- We are still waiting for the load graph finished.
- Also, I got the opportunity to assist to a conference of how to do abstracts for poster and the submission of a papers.
- I read a paper that could help us create a program to find bacteria’s that fix nitrogen in the soil. 
      
    Pierce, N. Tessa, et al. “Large-Scale Sequence Comparisons with Sourmash.” F1000Research, vol. 8, July 2019, p. 1006. DOI.org                  (Crossref), doi:10.12688/f1000research.19675.1.
- I read another paper that could help us recreate the assemblies that we found in the IMG, to understand what they found.
       
     Yu, G., Smith, D. K., Zhu, H., Guan, Y. and Lam, T. T.-Y. (2017) ggtree: an r package for visualization and
              annotation of phylogenetic trees with their covariates and other associated data. Methods Ecol Evol, 8: 28–36. doi:                     10.1111/2041-210X.12628
- I took a workshop with: Taylor Baum, Josefina Correa Menendez and Hector De Jesus-Cortes, called: Brains, Minds, and Machines Workshop.

### Week 6: (8-12, 7, 2019)

- We completed the Replicathon, and what we did is in the following link: <https://rpubs.com/essilena/512774>
- In the Replicathon with my partner Francisco Benitez, we created a copy of the repository of the Replicathon to ours and you can see it in the following link: <https://github.com/essilena/PR2019replicathon> 
- I earn a certificate of Statement of Acomplishment to Introduction of R!!!!!  
![Statement of Acomplishment, Introduction to R]({static}/images/certificate-introduction-to-R.png) 
- I practice through Data Camp the language R, to review what I had learn in the Workshops of the Software Carpentry the first week. All of this to be abble to apply it in the Data Reproducibility/Replicathon. 
- I updated the Research Summary

- We started with the Partition protocol, with the first step called: load-graph
```
#!/bin/bash
#SBATCH --mem-per-cpu=15000
#SBATCH --time=7-00:00:00
#SBATCH --job-name=load-graph
#SBATCH --mail-user=anelisse.dominicci@upr.edu
#SBATCH --mail-type=ALL
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32

# Load project
source /home/humberto/adominicci/miniconda3/etc/profile.d/conda.sh
conda activate roble

load-graph.py -k 25 -M 80G -T 32 roble SRR*.ka.fq
```


### Week 5: (1-5, 7, 2019)
- So the last command for interleave work, but when we try to run the script that we wrote to normalize it didnt recognized the samples as paired and neither the names of the files.
-This is because at the beggining we did fastq-dump to the samples, except for the 3rd one we used the update of fastq-dump that is fasterq-dump, because we wanted to explore if it was much better and faster than fastq-dump. So the samples run with fastq-dump where called: 
#### Example of sample #1 SRR5256888_1.qc.fq.gz 
```
@SRR5256888.1 1 length=150
CGAGACTCTTGCGCGCGGCGGCGTCGGACA
+SRR5256888.1 1 length=150
CCCFFFFFHHHHHJJJJJJJJGD@BDDDDD
@SRR5256888.2 2 length=150
GTCGCCTCTTCCGATCCAATTGCACAAGCA
+SRR5256888.2 2 length=150
CCCFFFFFHHHHHJJJJJJJJJJJJJJJJJ
```
- And the 3rd sample run with fasterq-dump was called:
#### Example of sample #3 SRR5256987_1.qc.fq.gz 
```
@SRR5256987.12.1 12 length=150
AGCTCCTCCCACCAGGTCGCAGCGCGACCGTCGAGCTCTCCGTAGACGCCGGTCGCCTCCTTCCGCTGATCGTCGACGAGCACGACCCCGGCGAACCCAACCCGCAGGAGCGAGGTCACCTCCCGAACGAGCGGCCGCGCCACG
+SRR5256987.12.1 12 length=150
1=DDFFFHFHHHJJJJIGIJJIGHIJIJJJJJJHHFFFFDEDDDDDDDDBDDBDDDDDBDDDDDDBDDDDDDDDBDDDDDBDDDDDDDDDDDDDDBBBDDDDB@>B@<<<89>@B>CCCDCBDD>BB.99<<@DBBB@<BDBBD
```
- The difference between them is the names since the first one is called: 
```
@ SRR5256888.1 1 length = 150 
```

and the third sample:
```
@ SRR5256987.12.1 12 length = 150
```

- So in order to fix this we downloaded khmer, and we went to khmer tools, and modified the script called "interleave-reads.py" as followed: 

```
#!/home/humberto/adominicci/miniconda3/envs/roble/bin/python
# This file is part of khmer, https://github.com/dib-lab/khmer/, and is
# Copyright (C) 2011-2015, Michigan State University.
# Copyright (C) 2015, The Regents of the University of California.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials provided
#       with the distribution.
#
#     * Neither the name of the Michigan State University nor the names
#       of its contributors may be used to endorse or promote products
# 	 derived from this software without specific prior written
#       permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Contact: khmer-project@idyll.org
# pylint: disable=invalid-name,missing-docstring
""" 
Interleave left and right reads.

Take two files containing left & right reads from a paired-end sequencing run,
and interleave them.

% scripts/interleave-reads.py <R1> <R2> [ -o <outputfile> ]

By default, output is sent to stdou
"""

import screed
import sys
import textwrap
from khmer import __version__
from khmer.kfile import check_input_files, check_space
from khmer.khmer_args import sanitize_help, KhmerArgumentParser
from khmer.khmer_args import FileType as khFileType
from khmer.kfile import (add_output_compression_type, get_file_writer,
from khmer.utils import (write_record_pair, check_is_left, check_is_right,
                         check_is_pair)

try:
    from itertools import zip_longest
except ImportError:
    from itertools import izip_longest as zip_longest


def get_parser():
    epilog = """\
    The output is an interleaved set of reads, with each read in <R1> paired
    with a read in <R2>. By default, the output goes to stdout unless
    :option:`-o`/:option:`--output` is specified.

    As a "bonus", this file ensures that if read names are not already
    formatted properly, they are reformatted consistently, such that
    This reformatting can be switched off with the
    :option:`--no-reformat` flag.

    Example::

        interleave-reads.py tests/test-data/paired.fq.1 \\
                tests/test-data/paired.fq.2 -o paired.fq"""
    parser = KhmerArgumentParser(
  description='Produce interleaved files from R1/R2 paired files',
        epilog=textwrap.dedent(epilog))

    parser.add_argument('left')
    parser.add_argument('right')
    parser.add_argument('-o', '--output', metavar="filename",
                        type=khFileType('wb'),
                        default=sys.stdout)
    parser.add_argument('--no-reformat', default=False, action='store_true',
                        help='Do not reformat read names or enforce\
                              consistency')
    parser.add_argument('-f', '--force', default=False, action='store_true',
                        help='Overwrite output file if it exists')
    add_output_compression_type(parser)
    return parser


def main():
    args = sanitize_help(get_parser()).parse_args()

    check_input_files(args.left, args.force)
    check_input_files(args.right, args.force)
    check_space([args.left, args.right], args.force)

    s1_file = args.left
    s2_file = args.right

    print("Interleaving:\n\t%s\n\t%s" % (s1_file, s2_file), file=sys.stderr)

    outfp = get_file_writer(args.output, args.gzip, args.bzip)

    counter = 0
    screed_iter_1 = screed.open(s1_file)
    screed_iter_2 = screed.open(s2_file)
    for read1, read2 in zip_longest(screed_iter_1, screed_iter_2):
        if read1 is None or read2 is None:

            print(("ERROR: Input files contain different number"
                   " of records."), file=sys.stderr)
            sys.exit(1)

        if counter % 100000 == 0:
            print('...', counter, 'pairs', file=sys.stderr)
        counter += 1

        name1 = read1.name.split(" ")[0]
        name2 = read2.name.split(" ")[0]
        fields = name1.split(".")
        if (3 == len(fields)) :
           name1= ".".join(fields [:2])
        fields = name2.split(".")
        if (3 == len(fields)) :
           name2= ".".join(fields [:2])

        if not args.no_reformat:
            if not check_is_left(name1):
                name1 += '/1'
            if not check_is_right(name2):
                name2 += '/2'

            read1.name = name1
            read2.name = name2

            if not check_is_pair(read1, read2):
                print("ERROR: This doesn't look like paired data! "
                      "%s %s" % (read1.name, read2.name), file=sys.stderr)
                sys.exit(1)

        write_record_pair(read1, read2, outfp)

    print('final: interleaved %d pairs' % counter, file=sys.stderr)
    print('output written to', describe_file_handle(outfp), file=sys.stderr)
if __name__ == '__main__':
    main()
```
- This was to modify the name of the sample, in order to process and that at the end, all the names of each sample have the same format.
We commanded that the program split the name as follow @ SRRxxx.yy -yy- lengh = 150 and eliminate the part after the second period. The command that we modify is the following:
```
name1 = read1.name.split(" ")[0]
        name2 = read2.name.split(" ")[0]
        fields = name1.split(".")
        if (3 == len(fields)) :
           name1= ".".join(fields [:2])
        fields = name2.split(".")
        if (3 == len(fields)) :
           name2= ".".join(fields [:2])

```
- Then we include the modified script called "interleave-reads.py" in our script called: "interleve.sh":
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
# Load project
source /home/humberto/adominicci/miniconda3/etc/profile.d/conda.sh
conda activate roble

for filename in *_1.qc.fq.gz
do
  # first, make the base by removing fastq.gz
  base=$(basename $filename _1.qc.fq.gz)
  echo $base

  # now, construct the R2 filename by replacing R1 with R2
  baseR2=${base}_2
  baseR1=${base}_1
  echo $baseR2

 # finally, run interleave-reads.py
  ./interleave-reads.py -o ${base}.pe.qc.fq.gz ${baseR1}.qc.fq.gz ${baseR2}.qc.fq.gz
done
```
- This way all the samples look the following way:
```
#### Example of sample #1 SRR5256888.pe.qc.fq

@SRR5256888.1/1
CGAGACTCTTGCGCGCGGCGGCGTCGGACA
+
CCCFFFFFHHHHHJJJJJJJJGD@BDDDDD
@SRR5256888.1/2
AAGGCCCGTGACAGCCACGAGCTTATCGTCGATGGCTAGTTCGCCCGTCACCTTGAAGAAGGGCTGGCTGTAGTAATACGAGGCCTGCTCGCGCTCGGACTTCTTGCTGAAGCCGCCTTCGCCCTGCAGCACCAGCGGACGATC
+
CCCFFFFFHHHHHJJJJJJJJIJJJJJJIJJIIJIJJIIGHIIIJJGHHFBDEFACEEEEDDDDDDDDDDBCDCCDCCCDDDDDDDDDDCDDDDDDDD>BDDDDDCCD@CCACDDDD@@C?BDD>ABCCCDDB88A>9@<>9<B

```
- Therefore, we decided to run the normalize script "normalize-by-median.py":
```
#!/bin/bash
#SBATCH --mem-per-cpu=15000
#SBATCH --time=100:00:00
#SBATCH --job-name=normalize
#SBATCH --mail-user=anelisse.dominicci@upr.edu
#SBATCH --mail-type=ALL
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8

# Load project
source /home/humberto/adominicci/miniconda3/etc/profile.d/conda.sh
conda activate roble

normalize-by-median.py -k 20 -C 20 --max-memory-usage 64G -p --savegraph normC2$normC20k20.ct --report report.txt --report-frequency 1000000 *.pe.qc.fq
```
- Right now, we are waiting for those results, and we thinking that our next step should be to do a partition (which is what we will probably do) or run the assemblies again (Megahit, PLASS and MetaSPAdes).

### Week 4: (24-28, 6, 2019)
  - We had some trobles downloading the data, but we finally DID IT!!!
  - We run the command "fastq-dump", to compress the files.
  - Then we run "FASTQC" to see the quality of each samples.
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
- Then we run "MULTIQC" to see the general quality of all samples.
- We wanted to explore if in the samples there were adapters so we run the following script:
To explore what different adapters were present in the samples we run the script:

```
front=GATCGGAAGAGCACACGTCTGAACTCCAGTCAC
end=ATCTCGTATGCCGTCTTCTGCTTG

#zgrep -o -e "${front}......${end}" $*

zcat $* | sed -n 's/.*GATCGGAAGAGCACACGTCTGAACTCCAGTCAC\(......\)ATCTCGTATGCCGT$$TGCCGTCTTCTGCTTG.*/\1/p'
```

- After that we decided to do a trim, with quality of 5. 
- Also eliminating the adapters, since in the reports the quality said that there was an overrepresented sequence.
- Note: the Comnbinados file is the adapters that we found.
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
- When this was fianlly done, we run again the "FastQC" and the "MULTIQC" and the reports WERE GREAT!!!! so we decided to start doing the assemblies with 3 differents assemblers. 
- We used Megahit:
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
- We also used PLASS:
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
- And finally we used MetaSPAdes:
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
- The 3 assemblies failed, because they required more memory, than the one we put each script to make the assembly. So we did a "Digital Normalize" to reduce the data a little bit, so we can run all the assembler again. We did a first script and we forgot to put --gzip and --no-reformat (so when we runned again, it doesn't change the names of the sequences, nor check if they are paired sequences. So I put the script with the corrections:
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
- So now we are waiting for that task to be over, to see if we can run the assemblers.
- Also during the week we found the assemblies of the project, done by others persons in IMG.



### Week 3: (17-21, 6, 2019)
  - We are downloading the data from NCBi, to Boqueron. We are still waiting.
  
### Week 2: (10-14, 6, 2019)
  - I was reading papers and protocols, to learn about the research and different programs we are going to use.
  - I wrote a research summary, like a proposal to know what are the next steps.

### Week 1: (3-7, 6, 2019)
  - I was doing the Software Carpentry Workshop.
