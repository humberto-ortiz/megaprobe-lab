Title: Josefina Correa Menendez
Date: 2016-08-26 
Category: People 
Tags: de-novo

#Biography

My name is Josefina Correa. I am an undergraduate Biology major at the University of Puerto Rico, Rio Piedras campus; 
I am also taking computer science courses with the goal of completing a dual concentration. I am a member of the IDI-BD2K program
(Increasing Diversity in Big Data to Knowledge), an initiative that seeks to train students in the adequate use of large quantities of data for producing coherent quantiative analysis within the context of Biomedical Informatics. This semester I will be working with Dr. Ortiz and Dr. García-Arrarás on a project pertaining to *de-novo* sequencing.

#Contact

* e-mail: josefina.correa@upr.edu
* Github: https://github.com/josefinacmenendez

#Project Description

*TBA*

#Weekly Reports
##Week 11: 10/31/16 - 11/05/16

Attempting to annotate H. glaberrima contigs from Vladimir's data:

```{R}
#Step 5
#Ran the following commands and added the following script to /josefina/bin 
cd ${HOME}/bin
wget https://raw.githubusercontent.com/dib-lab/khmer/master/scripts/do-partition.py
chmod u+x do-partition.py
#do-partition.py requires khmer. 
#I attempted to install khmer but the command 'apt-get' could not be found...
```

##Week 10: 10/24/16 - 10/28/16

Made the following updates to Datatube_Heatmap at <https://github.com/josefinacmenendez/Datatube_Heatmap>:

* The full list of contigs can be accessed on <https://josefinacmenendez.shinyapps.io/Datatube_Heatmap/> . To do so, type the contig name, or any letter that might be in that name (i.e. G for the Gypsy contigs).   
* The generated heatmap can be exported as a pdf  
* The differential expression data is now processed on global.R

##Week 9: 10/17/16- 10/21/16

Made the following updates to Datatube_Heatmap at <https://github.com/josefinacmenendez/Datatube_Heatmap>:

* corrected error messages
* improved image scaling
* the full list of contigs can be accessed through R studio, but not through shinyapps.io; this will be fixed soon
  
##Week 8: 10/10/16- 10/14/16

Set up a repository for the shiny app built for showing the heatmaps:

* <https://github.com/josefinacmenendez/Datatube_Heatmap>

The shiny app is functional. However, the following issues will be addressed this week:

*  Parsing the full set of contigs into the selectizeInput list crashes the app
*  There are several error messages that should be substituted with prompt messages

##Week 7: 10/3/16 - 10/7/16

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

##Week 6: 9/26/16 - 9/30/16
##Week 5: 9/19/16 - 9/23/16

##Week 4: 9/12/16 - 9/16/16
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

##Week 3: 9/05/16 - 9/09/16
I have been familiarizing myself with the project, reading what has been published on the matter by Mashanov *et. al.*:
<http://www.biomedcentral.com/1471-2164/15/357>

##Week 2: 8/29/16 - 9/02/16
Dr. Ortiz, Dr. García-Arrarás and I met to discuss the biological intrinciacies of the *de-novo* sequencing project.
We discussed the biological aspects of the project and detailed the following goals for this semester:

* Use Vladimir's Databank as a database to search for homologies between other species 
* Search for differential gene expression among reads
* Produce a new assembly to expand the databank and include the transcriptome of reads for the regenerated and normal intestine of *H. glaberrima*

##Week 1: 8/22/16 - 8/26/16

First lab meeting today. I am excited to learn more about my project.
