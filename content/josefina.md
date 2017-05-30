Title: Josefina Correa Menendez
Date: 2016-08-26 
Category: People 
Tags: de-novo

# Biography

My name is Josefina Correa. I am an undergraduate Biology major at the University of Puerto Rico, Rio Piedras campus; 
I am also taking computer science courses with the goal of completing a dual concentration. I am a member of the IDI-BD2K program
(Increasing Diversity in Big Data to Knowledge), an initiative that seeks to train students in the adequate use of large quantities of data for producing coherent quantiative analysis within the context of Biomedical Informatics. This semester I will be working with Dr. Ortiz and Dr. García-Arrarás on a project pertaining to *de-novo* sequencing.

# Contact

* e-mail: josefina.correa@upr.edu
* Github: https://github.com/josefinacmenendez

# Project Description

This project aims to assemble and annotate transcripts from H. glaberrima.

# Weekly Reports	  	
## Second semester


## Week 20: 5/29/17- 5/4/17

I modified DatatubeV2's color scheme to red-black-green.
The code has been updated in [global.R](https://github.com/josefinacmenendez/DatatubeV2/commit/7e0fd12f8f4c750e1c97b3554ab8174a4d79f542). 

## Week 19: 5/22/17- 5/28/17

The new version of Datatube is ready. The code can be found [here](https://github.com/josefinacmenendez/DatatubeV2).

## Week 18: 5/15/17- 5/21/17

I finished building the ranked list and am updating Datatube_Heatmap's code to add new features.

## Week 17: 5/8/17 - 5/14/17

*Ibid*, week 16.

## Week 16: 5/1/17 - 5/7/17

I am still working on building the ranked list. It should be up shortly. 

## Week 15: 4/24/17 - 4/31/17

I have been working on building a ranked list of differential expression to be able to find contigs with a great degree of differential expression more easily.

## Week 14: 4/17/17 - 4/23/17

Inspired by Dr. Corrada-Bravo's talk, I have been working on improving Datatube's visualization components to include the differential expression number on each color block.

## Week 13: 4/10/17 - 4/16/17

I assembled the transcript families and I am re-running BLAST on both directions; I added a parameter to specify the output to be in XML format, which can be parsed using BioPython:

```
from Bio.Blast import NCBIXML
blast_records = NCBIXML.parse(result_handle)
```

## Week 12: 4/3/17 - 4/9/17

I am working on figuring out a way to parse the blast2.6 output and be able to determine the homologies and orthologies.
This [tutorial](http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc93) will be useful.

## Week 11: 3/27/17 - 4/2/17

I created a conda environment and installed the latest version of blast:

```
module load anaconda
conda create -n blast2.6 python=2.7
source activate blast2.6
cd /home/josefina/.conda/envs/blast2.6/
wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.6.0+-x64-linux.tar.gz
tar zxvpf ncbi-blast-2.6.0+-x64-linux.tar.gz
cp ncbi-blast-2.6.0+/bin/* bin/
```

I formatted the contigs and the mouse reference sequences as databases:

```
makeblastdb -in mouse.protein.faa -dbtype prot -out mouse.protein.faa
makeblastdb -in combined_transcripts_cleaned_fasta_cap_contigs.fasta -dbtype nucl -out combined_transcripts_cleaned_fasta_cap_contigs.fasta 
```

I used the following commands to run blast on both directions:

```
tblastn -query mouse.protein.faa -db combined_transcripts_cleaned_fasta_cap_contigs.fasta -evalue 1e-3 -num_threads 8 -out mouse.x.pepino
blastx -query combined_transcripts_cleaned_fasta_cap_contigs.fasta -db mouse.protein.faa -evalue 1e-3 -num_threads 8 -out pepino.x.mouse
```
The aligned sequences can be found in /data/josefina/blast2.6/

## Week 10: 3/20/17 - 3/26/17

I wrote a python script, [map_contigs.py](https://github.com/josefinacmenendez/de-novo-seq/blob/master/map_contigs.py), to parse .fasta and .csv files, and to extract the sequence from a .fasta file and append it to a .csv file. This script was necessary because shmlast does not include the sequence in its output, it only includes the contig name. The script can also be used to parse other .fasta files with transcript IDs (such as those produced by the Eel-Pond protocol), and fetch the corresponding ID.

Usage:

```
python map_contigs.py --fasta_1 combined_transcripts_cleaned_fasta_cap_contigs.fasta --csv_file combined_transcripts_cleaned_fasta_cap_contigs.fasta.x.mouse.protein.faa.crbl.csv 

```
Output:

```
combined_transcripts_cleaned_fasta_cap_contigs.fasta.x.purpuratus.protein.faa.seq.csv
```

This output can be parsed for fetching the corresponding transcript ids:

```
python map_contigs.py --fasta_1 pepino_on_mouse.fasta.annot --csv_file combined_transcripts_cleaned_fasta_cap_contigs.fasta.x.purpuratus.protein.faa.seq.csv

```

## Week 9: 3/13/17 - 3/19/17

I ran shmlast's conditional reciprocal best hits against both mouse and *S. purpuratus* databases as follows:
```
module load anaconda
source activate shmlast

shmlast crbl -q combined_transcripts_cleaned_fasta_cap_contigs.fasta -d purpuratus.protein.faa --n_threads 8

shmlast crbl -q combined_transcripts_cleaned_fasta_cap_contigs.fasta -d mouse.protein.faa --n_threads 8
```

The output is available at /data/josefina/shmlast

The output includes the contig ID and a unique identifier. I will be using the contig ID to fetch the corresponding transcript, since the output does not include the transcript. Since the output annotates the transcripts, this can serve as a supplementary annotation database to the one already in blastkit. I'd have to see which ones are already included in the previous annotations.

## Week 8: 3/6/17 - 3/12/17

Since transcript families group transcripts by their shared sequence, I have been reading papers about de-brujin graphs to understand CTB's methos for creating transcript families.

# Week 7: 2/27/17 - 3/5/17

I have been preparing the shmlast presentation for the journal club.

## Week 6: 2/20/17 - 2/26/17
Current task: get the contig ids given a file with new ids and the corresponding transcript.  
  
I created a new script: [get_contig_names.py](https://github.com/josefinacmenendez/eel-pond/blob/master/get_contig_names.py). 
This script takes as input two .fasta files, one with the contig ids and another one with the new names. It uses SeqIO to parse the files and generates two dictionaries. The dictionary with the contig ids has as keys the contig ids and the transcripts as values. The dictionary with the new names has the transcripts as keys and the new names as values. This can be done because the relation between the set of names and the set of transcripts is one-to-one. The script then fetches the corresponding new name given a contig as key by searching through common transcript sequences. It generates as output a table with the new names in the first column and the corresponding contig ids in the second column. 

Note: the length of the output file is equal to the length of the input file with the new ids.

## Week 5: 2/13/17 - 2/19/17
Current task: get the contig ids given a file with new ids and the corresponding transcript.  
  
I edited [annotate_seqs.py](https://github.com/josefinacmenendez/eel-pond/blob/master/annotate_seqs.py) to fetch the contig ids after blasting the annotated transcripts against the original assembly (which only has the contig ids and the transcript). I will be working on improving this implementation of blast during the next week.

I also edited a local copy of rename-with-partitions.py on the server to create new names that have the contig names. However, this may not be the best solution to the problem.

## Week 4: 2/6/14 - 2/12/17
I edited the annotate-seqs.py script (now [annotate_seqs.py](https://github.com/josefinacmenendez/eel-pond/blob/master/annotate_seqs.py)) and the [namedb.py](https://github.com/josefinacmenendez/eel-pond/blob/master/namedb.py) scripts to allow for parsing relevant file-names of different organisms for annotation. Prior to this, the 'mouse.namedb' filename was built-in to namedb.py. This scripts are on Hulk and also on my fork of the eel-pond repository.

annotate_seqs.py now takes three more arguments:

```
parser.add_argument('file_name') #i.e. purpuratus.namedb
parser.add_argument('full_name') #i.e. purpuratus.namedb.fullname
parser.add_argument('refseq')    #i.e. purpuratus.protein.faa
...
file_name =str(args.file_name)
full_name =str(args.full_name)
refseq = str(args.refseq)
```
These files are inherited and parsed by namedb.py by importing annotate_seqs.py as a module; the pararsed files are then passed to annotate_seqs.py as needed.
```
import annotate_seqs as annotate
mouse_namedb = annotate.file_name
mouse_namedb_fullname = annotate.full_name
mouse_protein_faa = annotate.refseq
fp = open('mouse.namedb')
is_ncbi = cPickle.load(fp)
mouse_names = cPickle.load(fp)
fp.close()

mouse_fullname = cPickle.load(open('mouse.namedb.fullname'))
mouse_seqs = screed.ScreedDB('mouse.protein.faa')
```
namedb.py could be incorporated into annotate_seqs.py; however, this short script is likely also used by other scripts in the eel-pond tutorial and therefore inheritance usage is useful.

I also installed shmlast on Hulk.

```
curl -O https://raw.githubusercontent.com/camillescott/shmlast/master/environment.txt
conda create -n shmlast --file environment.txt 
source activate shmlast
pip install shmlast
```
## Week 3: 1/30/17 - 2/5/17
I spent some time this week working on the manuscript.
I also worked on mapping the contigs from two different assemblies from the same transcriptome data to aid in comparing differential expression based on the Datatube GUI.

The two assemblies are:     
(1) combined_transcripts_cleaned_fasta_cap_contigs.fasta (assembled using The Eel-pond mRNA-seq Protocol)     
(2) Hglaberrima_RNC_transcriptome_Contigs.fasta.zip (assembled by [Vladimir Mashanov](dx.doi.org/10.1186/1471-2164-15-357))     

Mapping contig ID's from two different assemblies from the same data:

```
import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser(description = "reads two .fasta files")
parser.add_argument("--fasta_1", help = ".fasta file 1", required = True)
parser.add_argument("--fasta_2", help = ".fasta file 2", required = True)

args = parser.parse_args()

fasta_1 = args.fasta_1
fasta_2 = args.fasta_2

def get_contig_dict(fasta_file):
        contig_dict = {}
        with open(fasta_file, 'rU') as handle:
                for record in SeqIO.parse(handle, 'fasta'):
                        contig_dict[str(record.seq)] = record.id
        return contig_dict

def map_ids(dict1, dict2):
        mapped_ids = []
        differ_ids = 0
        for key in dict1.keys():
                if key in dict2.keys():
                        mapped_ids.append( [dict1[key], dict2[key] ] )
                        print mapped_ids
                        if dict1[key] != dict2[key]:
                                differ_ids += 1
                else:
                        mapped_ids.append( [dict1[key] , "NA" ] )

        if differ_ids  == 0:
                mapped_ids.insert( 0 , ['Different_Ids' , differ_ids] )
        return mapped_ids

contig_dict_1 = get_contig_dict(fasta_1)
contig_dict_2 = get_contig_dict(fasta_2)
mapped_contig_ids = map_ids(contig_dict_1, contig_dict_2)

for item in mapped_contig_ids:
        print item

```



The assembled contigs were downloaded from [this paper](dx.doi.org/10.6070/H4PN93J1).

## Week 2: 1/23/17 - 1/29/17
I have been working on revising the initial submission of a manuscript that I helped write during last summer's internship at U. Pitt's DBMI.

The original submission can be found [here](dx.doi.org/10.12688/f1000research.9364.1). I am listed in the acknowledgements section.

##Week 1: 1/16/17 - 1/22/17
I re-ran The Eel-Pond mRNAseq Protocol on Hulk after the server was re-established. I made some adjustments to some scripts to annotate the contigs using the S. purpuratus ref-seq.
The following commands were used:

Make a virtual environment and installing the necessary tools to make transcript families and annotate the assembly
```
module load anaconda
conda create -n eel-pond python=2.7
source activate eel-pond
```
Install screed
```
cd /home/josefina/.conda/envs/eel-pond/share
git clone https://github.com/ged-lab/screed.git
cd screed
git checkout protocols-v0.8.3
python setup.py install
```
Install khmer
```
cd /home/josefina/.conda/envs/eel-pond/share
git clone https://github.com/ged-lab/khmer.git
cd khmer
git checkout protocols-v0.8.3
make
echo 'export PYTHONPATH=$PYTHONPATH:/home/josefina/.conda/envs/eel-pond/share/khmer' >> ~/.bashrc
source ~/.bashrc
```
Install Blast Legacy v 2.2.24
```
cd /home/josefina/.conda/envs/eel-pond/bin
curl -O ftp://ftp.ncbi.nlm.nih.gov/blast/executables/legacy/2.2.24/blast-2.2.24-x64-linux.tar.gz
tar xzf blast-2.2.24-x64-linux.tar.gz
cd bin
mv blast-2.2.24 ../BLAST/
mv blast-2.2.24-x64-linux.tar.gz ../BLAST/
cd ../BLAST/
cp blast-2.2.24/bin/* /home/josefina/.conda/envs/eel-pond/bin
cp -r blast-2.2.24/data /home/josefina/.conda/envs/eel-pond/blast-data
```

Modify the path of some scripts:
```
cd share/eel-pond
nano make-uni-best-hits.py
nano make-reciprocal-best-hits.py
echo 'added sys.path.inser(0, '/home/josefina/.conda/envs/eel-pond/blastkit/lib') to make-reciprocal-best-hits.py and make-uni-best-hits.py'
```



Build transcript families
```
echo 'Starting from step 5: Building Transcript Families using Blast2'
python /home/josefina/.conda/envs/eel-pond/share/khmer/scripts/do-partition.py -x 1e9 -N 4 --threads 4 pepino combined_transcripts_cleaned_fasta_cap_contigs.fasta
python /home/josefina/.conda/envs/eel-pond/share/eel-pond/rename-with-partitions.py pepino combined_transcripts_cleaned_fasta_cap_contigs.fasta.part
```

Blast the contigs
```
mv combined_transcripts_cleaned_fasta_cap_contigs.fasta.part.renamed.fasta.gz pepino_combined_transcripts_renamed.fasta.gz
gunzip pepino_combined_transcripts_renamed.fasta.gz
formatdb -i pepino_combined_transcripts_renamed.fasta -o T -p F
for file in mouse.1.protein.faa.gz mouse.2.protein.faa.gz mouse.3.protein.faa.gz; do curl -O ftp://ftp.ncbi.nih.gov/refseq/M_musculus/mRNA_Prot/${file}; done
gunzip mouse.[123].protein.faa.gz
cat mouse.[123].protein.faa > mouse.protein.faa
formatdb -i mouse.protein.faa -o T -p T
```

```
screen -S BLASTALL_1
Ctrl A D #to unattach screen
blastall -i mouse.protein.faa -d pepino_combined_transcripts_renamed.fasta -e 1e-3 -p tblastn -o mouse.x.pepino -a 8 -v 4 -b 4
```
```
screen -S BLASTALL_2
blastall -i pepino_combined_transcripts_renamed.fasta -d mouse.protein.faa -e 1e-3 -p blastx -o pepino.x.mouse -a 8 -v 4 -b 4
Ctrl A D #to unattach screen
```
```
python /home/josefina/.conda/envs/eel-pond/share/eel-pond/make-namedb.py mouse.protein.faa mouse.namedb
python -m screed.fadbm mouse.protein.faa
```

Calculate homologies and orthologies
```
python /home/josefina/.conda/envs/eel-pond/share/eel-pond/make-uni-best-hits.py pepino.x.mouse pepino.x.mouse.homol
python /home/josefina/.conda/envs/eel-pond/share/eel-pond/make-reciprocal-best-hits.py pepino.x.mouse mouse.x.pepino pepino.x.mouse.ortho
```

Format the mouse refseq data
```
python /home/josefina/.conda/envs/eel-pond/share/eel-pond/annotate-seqs.py pepino_combined_transcripts_renamed.fasta pepino.x.mouse.ortho pepino.x.mouse.homol
```

Blast the contigs against S. purpuratus ref-seq
```
cd ../pepino.on.purpuratus/
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/invertebrate/Strongylocentrotus_purpuratus/representative/GCF_000002235.4_Spur_4.2/GCF_000002235.4_Spur_4.2_protein.faa.gz
gunzip GCF_000002235.4_Spur_4.2_protein.faa.gz
formatdb -i GCF_000002235.4_Spur_4.2_protein.faa -o T -p T
formatdb -i combined_transcripts_cleaned_fasta_cap_contigs.renamed.fasta -o T -p F

screen -S BLASTX
blastall -i combined_transcripts_cleaned_fasta_cap_contigs.renamed.fasta -d GCF_000002235.4_Spur_4.2_protein.faa -e 1e-3 -p blastx -o pepino.x.purpuratus -a 8 -v 4 -b 4
Ctrl A D

screen -S TBLASTN
blastall -i GCF_000002235.4_Spur_4.2_protein.faa -d pepino_db -e 1e-3 -p tblastn -o purpuratus.x.pepino -a 8 -v 4 -b 4
Ctrl A D
```

```
python /home/josefina/.conda/envs/eel-pond/share/eel-pond/make-namedb.py GCF_000002235.4_Spur_4.2_protein.faa purpuratus.namedb
python -m screed.fadbm GCF_000002235.4_Spur_4.2_protein.faa
```

Obtain homologies and orthologies using the S. purpuratus ref-seq

```
python /home/josefina/.conda/envs/eel-pond/share/eel-pond/make-uni-best-hits.py pepino.x.purpuratus pepino.x.purpuratus.homol
python /home/josefina/.conda/envs/eel-pond/share/eel-pond/make-reciprocal-best-hits.py pepino.x.purpuratus purpuratus.x.pepino pepino.x.purpuratus.ortho
  
```

Edit the namedb.py script to allow for parsing purpuratus.namedb
```
nano /home/josefina/.conda/envs/eel-pond/share/eel-pond/namedb.py
```
Format GCF_000002235.4_Spur_4.2_protein.faa as purpuratus.namedb
```
python /home/josefina/.conda/envs/eel-pond/share/eel-pond/make-namedb.py GCF_000002235.4_Spur_4.2_protein.faa purpuratus.namedb
python -m screed.fadbm GCF_000002235.4_Spur_4.2_protein.faa
```
Annotate the sequences using the S. purpuratus ref-seq
```
python /home/josefina/.conda/envs/eel-pond/share/eel-pond/annotate-seqs.py pepino_db pepino.x.purpuratus.ortho pepino.x.purpuratus.homol
```


## First semester
## Week 16: 12/04/16 - 12/05/16

annotate-seqs.py was fixed; the changes are documented on the forks humberto-ortiz/eel-pond and josefinacmenendez/eel-pond

However, when attempted with the pepino data, no hits are found for the following reason: no orthologies or homologies are found. I found that on the previous step (building transcript families) rename-with-partitions.py was building a name with a space between > NAME instead of building it >NAME; I fixed this, but this did not correct the problem. It's as if blastparser is not parsing the data into make-uni-best-hits.py or make-reciprocal-best-hits.py.

## Week 15: 11/28/16 - 12/4/16

I attempted the eel-pond procedure locally, but obtained no hits when running annotate-seqs.py

I also familiarized myself with using git hub via the command line.

The following steps describe how to get started with git hub using the command line:

1. Configure the repository
2. Create a copy of the repository on a local directory
3. Add a file (also works for editing a file)
4. Commit the file
5. Push the file
6. Check the status

```
git config --global user.email "EMAIL"
git config --global user.name "USERNAME"
git clone http://github.com/USERNAME/REPOSITORY.git
cd REPOSITORY
git add FILENAME
git commit -m "MESSAGE"
git push
```

To remove the file, input:

```
git pull FILENAME
```

To add all files in a directory:

```
git add . 
```
OR
```
git add -A
```

## Week 14: 11/21/16 - 11/27/16

I attempted the procedure using data from S. purpuratus, taken from ftp://ftp.ncbi.nih.gov/genomes/Strongylocentrotus_purpuratus/protein/ and obtained no hits. 

I also attempted to run the tutorial using the canned blasts and the Nemastotella transcriptome, and yet obtained no hits.
I downloaded the BLAST version 2.2.26 and used formatdb instead of makeblastdb to format the mouse and the nemastotella data.
This [BLAST version](https://ftp.ncbi.nlm.nih.gov/blast/executables/legacy/2.2.26/) was installed according to directions detailed [here](https://github.com/ctb/blastkit). Rather than using virtualenv, a conda environment (named blastkit) was used. However, no hits were obtained when annotating the transcripts. 

## Week 13: 11/14/16 - 11/20/16

Annotating transcript families

[The Eel Pond mRNAseq Protocol](https://khmer-protocols.readthedocs.io/en/latest/mrnaseq/6-annotating-transcript-families.html) was used.


Downloading from NCBI RefSeq Mouse database to /data/josefina/DATATUBE/mRNAseq/data/refSeqMouse/:
```
(blastkit)[josefina@hulk annotations_2]$ for file in mouse.1.protein.faa.gz mouse.2.protein.faa.gz mouse.3.protein.faa.gz
(blastkit)[josefina@hulk annotations_2]$ 	do 
(blastkit)[josefina@hulk annotations_2]$ 	wget "ftp://ftp.ncbi.nlm.nih.gov/refseq/M_musculus/mRNA_Prot/${file}"
(blastkit)[josefina@hulk annotations_2]$ 	done
```
decompressing files
```
(blastkit)[josefina@hulk annotations_2]$ gunzip mouse.[123].protein.faa.gz
(blastkit)[josefina@hulk annotations_2]$ cat mouse.[123].protein.faa > mouse.protein.faa
```
formating files using makeblastdb instead of formatdb:
files are in /data/josefina/DATATUBE/mRNAseq/annotations/
```
(blastkit)[josefina@hulk annotations_2]$ makeblastdb -in mouse.protein.faa -dbtype prot

Building a new DB, current time: 11/15/2016 12:29:19
New DB name:   mouse.protein.faa
New DB title:  mouse.protein.faa
Sequence type: Protein
Keep Linkouts: T
Keep MBits: T
Maximum file size: 1000000000B
Adding sequences from FASTA; added 76419 sequences in 6.85848 seconds.

(blastkit)[josefina@hulk annotations_2]$ makeblastdb -in combined_transcripts_cleaned_renamed_pepino.fa -dbtype nucl

Building a new DB, current time: 11/15/2016 13:51:19
New DB name:   combined_transcripts_cleaned_renamed_pepino.fa
New DB title:  combined_transcripts_cleaned_renamed_pepino.fa
Sequence type: Nucleotide
Keep Linkouts: T
Keep MBits: T
Maximum file size: 1000000000B
Adding sequences from FASTA; added 63218 sequences in 8.16066 seconds.
```
running blastx
```
(blastkit)[josefina@hulk annotations_2]$ blastx -db mouse.protein.faa -query combined_transcripts_cleaned_renamed_pepino.fa \ -evalue 1e-3 -num_threads 8 -num_descriptions 4 -num_alignments 4 -out pepino.x.mouse

```
running tblastn
```
(blastkit)[josefina@hulk annotations_2]$ tblastn -db combined_transcripts_cleaned_renamed_pepino.fa -query \
mouse.protein.faa -evalue 1e-3 -num_threads 8 -num_descriptions 4 -num_alignments 4 -out mouse.x.pepino
```
Several warnings were observed wen running tblastn due to short sequences in the mouse RNA-seq data:

```
Warning: lcl|Query_2936 gi|9256636|ref|NP_061348.1| 60S ribosomal protein L41 [Mus musculus]: Warning: Could not calculate ungapped Karlin-Altschul parameters due to an invalid query sequence or its translation. Please verify the query sequence(s) and/or filtering options

(blastkit)[josefina@hulk annotations_2]$  grep -n "9256636" mouse.protein.faa
18946:>gi|9256636|ref|NP_061348.1| 60S ribosomal protein L41 [Mus musculus]

(blastkit)[josefina@hulk annotations_2]$  grep -A 1 "9256636" mouse.protein.faa
>gi|9256636|ref|NP_061348.1| 60S ribosomal protein L41 [Mus musculus]
MRAKWRKKRMRRLKRKRRKMRQRSK
```
The following commands use scripts from the [The Eel Pond mRNAseq Protocol](https://github.com/ctb/eel-pond) by Dr. Titus Brown.

Screed was downloaded into the virutal environment using 'pip install screed'.

Putative homology (best BLAST hit) and orthology (reciprocal best hits) were calculated:

```
(blastkit)[josefina@hulk annotations_2]$ python ../eelpond_scripts/make-uni-best-hits.py pepino.x.mouse pepino.x.mouse.homol
(blastkit)[josefina@hulk annotations_2]$ python ../eelpond_scripts/make-reciprocal-best-hits.py pepino.x.mouse mouse.x.pepino pepino.x.mouse.ortho
```

The mouse RNA-seq data was re-formatted:
```
(blastkit)[josefina@hulk annotations_2]$ python ../eelpond_scripts/make-namedb.py mouse.protein.faa mouse.namedb
(blastkit)[josefina@hulk annotations_2]$ python -m screed.fadbm mouse.protein.faa
```
Annotation was attempted using the following commands:
```
(blastkit)[josefina@hulk annotations_2]$ python ../eelpond_scripts/annotate-seqs.py \ combined_transcripts_cleaned_renamed_pepino.fa pepino.x.mouse.ortho pepino.x.mouse.homol 
Scanning sequences -- first pass to gather info
... 0
... 25000
... 50000
second pass: annotating
... x2 0
... x2 25000
... x2 50000
----
63217 sequences total
0 annotated / ortho
0 annotated / homol
0 annotated / tr
0 total annotated

annotated sequences in FASTA format: combined_transcripts_cleaned_renamed_pepino.fa.annot
annotation spreadsheet in: combined_transcripts_cleaned_renamed_pepino.fa.annot.csv
annotation spreadsheet with sequences (warning: LARGE): combined_transcripts_cleaned_renamed_pepino.fa.annot.large.csv
```

## Week 12: 11/07/16 - 11/13/16

Building transcript families:

Ran the fifth step of [The Eel Pond mRNAseq Protocol](https://khmer-protocols.readthedocs.io/en/mrnaseq/index.html) locally.
Failed attempts to reproduce this protocol on Hulk were made and the following was learned:

* gcc version 5.4.0 or greater is required
* installing khmer using pip install khmer and running do-partition.py results in the following error:
```
terminate called after throwing an instance of 'std::ios_base::failure'

what(): basic_ios::clear
```
The following commands worked:
```
module load gcc/5.4.0
module load anaconda
conda create --name khmer_tools python
source activate khmer_tools
cd /home/josefina/.conda/envs/khmer_tools

git clone https://github.com/dib-lab/khmer.git
make install-dependencies
make
./setup.py install --user

cd /data/josefina/DATATUBE/partitions_on_hulk

python do-partition.py -x 8e9 -N 4 --threads ${THREADS:-1} pepino 

combined_transcripts_cleaned_fasta_cap_contigs.fa.gz 
rename-with-partitions.py pepino combined_transcripts_cleaned_fasta_cap_contigs.fa.gz.part

mv combined_transcripts_cleaned_fasta_cap_contigs.renamed.fasta.gz \
	combined_transcripts_renamed.fa.gz

```
## Week 11: 10/31/16 - 11/06/16

Building transcript families:

Ran the fifth step of [The Eel Pond mRNAseq Protocol](https://khmer-protocols.readthedocs.io/en/mrnaseq/index.html).
I attempted to run this on Hulk by using the following commands:
```
[josefina@hulk khmer_venv]$ module load gcc
[josefina@hulk khmer_venv]$ module load anaconda
[josefina@hulk khmer_venv]$ conda create -n khmer python
[josefina@hulk khmer_venv]$ . activate khmer
(khmer)[josefina@hulk khmer_venv]$ pip install khmer
```
However, when running the script do-partition.py, the following error came up:

```
(khmer)[josefina@hulk khmer_venv]$ do-partition.py

Traceback (most recent call last):
  File "/home/josefina/.conda/envs/khmer/bin/do-partition.py", line 46, in <module>
    import khmer
  File "/home/josefina/.conda/envs/khmer/lib/python2.7/site-packages/khmer/__init__.py", line 42, in <module>
    from khmer._khmer import Countgraph as _Countgraph
ImportError: /usr/lib64/libstdc++.so.6: version `GLIBCXX_3.4.20' not found (required by /home/josefina/.conda/envs/khmer/lib/python2.7/site-packages/khmer/_khmer.so)
```
It seems there is some sort of incompatibility with the gcc version recquired to run this, and the gcc version installed on Hulk.

```
(khmer)[josefina@hulk khmer_venv]$ gcc --version
gcc (GCC) 4.4.7 20120313 (Red Hat 4.4.7-17)
Copyright (C) 2010 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```
However, it appears that the loaded gcc version is up to date:
```
(khmer)[josefina@hulk khmer_venv]$ module list
Currently Loaded Modulefiles:
  1) gcc/6.2.0   2) anaconda

```
I created a virtual environment locally and installed khmer as follows, and did not obtain the previous error when inputting 'do-partition.py':
```
josefina@josefina-Q552UB:~/virtual_environments$ sudo apt-get update
josefina@josefina-Q552UB:~/virtual_environments$ sudo apt-get -y install screen git curl gcc make g++ python-dev \ > unzip default-jre pkg-config libncurses5-dev r-base-core r-cran-gplots python-matplotlib python-pip \   
> python-virtualenv sysstat fastqc trimmomatic fastx-toolkit bowtie samtools blast2

josefina@josefina-Q552UB:~/virtual_environments$ gcc --version
gcc (Ubuntu 5.4.0-6ubuntu1~16.04.2) 5.4.0 20160609
Copyright (C) 2015 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.


josefina@josefina-Q552UB:~/virtual_environments$ python2.7 -m virtualenv khmer_venv
josefina@josefina-Q552UB:~/virtual_environments$ source khmer_venv/bin/activate
(khmer_venv) josefina@josefina-Q552UB:~/virtual_environments$ pip install khmer
(khmer_venv) josefina@josefina-Q552UB:~/virtual_environments$ do-partition.py
|| This is the script do-partition.py in khmer.
|| You are running khmer version 2.0
|| You are also using screed version 0.9
||
|| If you use this script in a publication, please cite EACH of the following:
||
||   * MR Crusoe et al., 2015. http://dx.doi.org/10.12688/f1000research.6924.1
||   * J Pell et al., http://dx.doi.org/10.1073/pnas.1121464109
||
|| Please see http://khmer.readthedocs.org/en/latest/citations.html for details.

usage: do-partition.py [-h] [--version] [--ksize KSIZE] [--n_tables N_TABLES]
                       [-U UNIQUE_KMERS] [--fp-rate FP_RATE]
                       [--max-tablesize MAX_TABLESIZE | -M MAX_MEMORY_USAGE]
                       [--threads THREADS] [--subset-size SUBSET_SIZE]
                       [--no-big-traverse] [--keep-subsets] [-f]
                       graphbase input_sequence_filename
                       [input_sequence_filename ...]
do-partition.py: error: too few arguments

```

## Week 10: 10/24/16 - 10/28/16

Made the following updates to [Datatube_Heatmap](https://github.com/josefinacmenendez/Datatube_Heatmap):

* The list of contigs can be accessed on <https://josefinacmenendez.shinyapps.io/Datatube_Heatmap/> . To do so, type the contig name, or any letter that might be in that name (i.e. G for the Gypsy contigs).   
* The generated heatmap can be exported as a pdf  
* The differential expression data is now processed on global.R

## Week 9: 10/17/16- 10/21/16

Made the following updates to [Datatube_Heatmap](https://github.com/josefinacmenendez/Datatube_Heatmap):

* corrected error messages
* improved image scaling
* the full list of contigs can be accessed through R studio, but not through shinyapps.io; this will be fixed soon
  
## Week 8: 10/10/16- 10/14/16

Set up a repository for the shiny app built for showing the heatmaps:

* <https://github.com/josefinacmenendez/Datatube_Heatmap>

The shiny app is functional. However, the following issues will be addressed this week:

*  Parsing the full set of contigs into the selectizeInput list crashes the app
*  There are several error messages that should be substituted with prompt messages

## Week 7: 10/3/16 - 10/7/16

Worked on writing an R script for plotting heatmaps using differential gene expression for H. glaberrima data:
The data is available on Hulk. I also spent some time becoming familiar with Shiny. I will be developing an app to view the heatmaps in a more user-friendly and interactive way.
```{R}
#set the working directory to wherever the data is and read the three files accordingly.
setwd("C:/Users/Josefina/Google Drive/Coursework/Megaprobe/Datatube")
library(gplots)

nvs2 <- read.csv("N_vs_day2_whole_list.csv")
nvs12<- read.csv("N_vs_day12_whole_list.csv")
nvs20<- read.csv("N_vs_day20_whole_list.csv")

contig.number <- nvs2$id

nvs2.log2Foldchange <- nvs2$log2FoldChange
nvs12.log2Foldchange<- nvs12$log2FoldChange
nvs20.log2Foldchange<- nvs20$log2FoldChange

dge_pepino <- cbind(nvs2.log2Foldchange,nvs12.log2Foldchange,nvs20.log2Foldchange)
dge_pepino <- as.matrix(toHeatmap)
colnames(dge_pepino) <- c("Day2","Day12","Day20")
rownames(dge_pepino) <- contig.number
library(functional)
#Remove "Inf", "-Inf", and "NA"
dge_pepino <- dge_pepino[apply(dge_pepino, 1, Compose(is.finite, all)), , drop=FALSE]

####GET ALL HEATMAPS####
maxSize = dim(dge_pepino)[1]

startPoint = 1
endPoint = 20
while(startPoint < maxSize)
{
  heatmap.2(dge_pepino[c(startPoint:endPoint),], trace = "none", col = redblue(20), main = startPoint);
  startPoint = startPoint + 20;
  endPoint = endPoint + 20;
  if(endPoint > maxSize)
  {
    endPoint = maxSize;
  };
}

write.csv(dge_pepino, "pepino_deg.csv", row.names = TRUE)
```

## Week 6: 9/26/16 - 9/30/16
## Week 5: 9/19/16 - 9/23/16

## Week 4: 9/12/16 - 9/16/16
I set up the virtual machine with the necessary tools to run the assembly:

* Downloaded git from <https://git-scm.com/download/win>

* Created virtual machine with Ubuntu 16.04 OS following the instructions detailed on   
<https://aws.amazon.com/getting-started/tutorials/launch-a-virtual-machine/>

* Used Git Bash to install the base image containing trimommatic and khmer tools using the following commands as detailed on <http://2016-aug-nonmodel-rnaseq.readthedocs.io/en/latest/install.html>

    - Boot a recent Ubuntu on Amazon (wily 15.10 image or later)
    - Log in as user ‘ubuntu’.
    - Run the following commands:
```
      sudo apt-get -y update && sudo apt-get -y install r-base python3-matplotlib libzmq3-dev python3.5-dev
      texlive-latex-extra texlive-latex-recommended python3-virtualenv trimmomatic fastqc python-pip python-dev bowtie samtools zlib1g-dev ncurses-dev
      
      sudo pip install -U setuptools khmer==2.0 jupyter jupyter_client ipython pandas
```

## Week 3: 9/05/16 - 9/09/16
I have been familiarizing myself with the project, reading what has been published on the matter by Mashanov *et. al.*:
<http://www.biomedcentral.com/1471-2164/15/357>

## Week 2: 8/29/16 - 9/02/16
Dr. Ortiz, Dr. García-Arrarás and I met to discuss the biological intrinciacies of the *de-novo* sequencing project.
We discussed the biological aspects of the project and detailed the following goals for this semester:

* Use Vladimir's Databank as a database to search for homologies between other species 
* Search for differential gene expression among reads
* Produce a new assembly to expand the databank and include the transcriptome of reads for the regenerated and normal intestine of *H. glaberrima*

## Week 1: 8/22/16 - 8/26/16

First lab meeting today. I am excited to learn more about my project.
