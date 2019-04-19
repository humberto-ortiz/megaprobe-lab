Title:Angel A. Sanquiche Sanchez
Date: 2016/08/25
Category:People
Tags:de-novo diffhash pepino erizo

# Bio:

- I'm a computer science student at the University of Puerto Rico Rio Piedras campus. As far as my programing skills are concerened I'm by no means an expert but at the very least I can say I can defend my self. I'm also a quiet person when in a conversation I'm not intricately knowledgeable about, but when I am I can speak volumes about it. Recently i've noticed I bite more than I can chew at times but I see those bites as a challange to edge out a win.

## Contact info:

- email - <angelsan720@gmail.com>
- institution email <angel.sanquiche@upr.com>
- github - <https://github.com/Angelsan720>

# Research Goals:

- Learn things in general.
- ~~Comprehend what bioinformatics are.~~ Learn more about bioinformatics (specially the bio part).
- Read up some explanatory papers in my free time
- Use free time to figure out how to get more free time.
- ~~By the time the semester is over, be able mto say I'm not wholly confused.~~ I'm only partially confused now.
- Expand my repitoir of skills in any way really.

## Weekly Updates:

## Spring 2019


### Status Update on the evolution of the proyect
- Originally diffhash ran on a sample dataset which I believe was using the 22nd human chromosome then it:
-- 1. Counted the kmer and wrote down how many times it appeared per file.
-- 2. Did a statistical analisys on how often a kmer appeared or not in condition A and condition B
-- 3. The output of the analisys is used to pull the reads containing the differentially expressed kmers.
-- 4. Assemble the reads.

- Step 1 and 2 were kept but optimized and generalized. The analisys can be tweaked to be more suited tom work with kmers. I have a suspicion that the analisys for kmers and whole reads might not really work for this properly.
- Step 3 can be removed. The kmers are the information that we need to assemble. Atleast in principle. The functionality of switching on and off can and should be switched on and off in the run script, but that is future work.
- Step 4 assembling was originally going to be done with Trinity but since these are very short reads Trinity doesnt work with these short reads. But Abyss does work with these short reads.
- Step 5 Annoting to see whether or not a specific sequence is expressed or not.

### Week 13:(8/04/19)-(12/04/19)
- Abyss worked. I have a reconstructed sequence. Now I need to see wether or not it aligns to the secuence from the standard pipeline. Now to annotate with dammit.
- dammit wont annotate the diffdata :(.

### Week 12:(1/04/19)-(5/04/19)
- Trinity wont play ball with the kmers.
- Ive adjusted diffhash to accept a kmer size parameter. Ive also spruced up the code a bit. Julia still takes time to load heavy packages.
- A size of 25 wont work either.
- The kevlar paper uses Abyss https://github.com/bcgsc/abyss to assemle Ill look into using it instead.

### Week 11:(25/03/19)-(29/03/19)
- Now they tell me I cant annotate the raw reads.
- I need to assemble the sequence from the diffhash output. Humberto recomends passing it through the pipeline like the normal data.
- The data wont run through the pipeline. something about interweaving but nothing will budge.
- The topic of the lab meeting "Kevlar" generates the target sequence from kmers instead of the normal reads. I could use this instead of the complete reads to assemble.
- Ill see if trinity works with short reads.

### Week 10:(18/03/19)-(22/03/19)
- With escamron protocol and diffhash both executed to completion next we need to verify if diffhash actually found the differentially expressed sequences or not.
- We will do reciprocal best blast hit on the data and well use a tool called 'dammit' https://github.com/dib-lab/dammit to do the it.
- Dammit installation as specified by https://eel-pond.readthedocs.io/en/latest/5-annotating.html requires packages that are incompatible with each other through conda.
- Installing through bioconda. Boquerons DNS is increasing enviroment solving for conda by a factor of several hours. Bioconda also takes significantly more than the average conda package channel. Got home and conda hasnt finished solving the enviroment. Friday morning, no lab meeting since its a day off. Conda hasn't finished, starting to losing hope.
- Moved to hulk at 9:00 AM Friday, installation finished by 1:00 PM same day. Screw bioconda.
- Next weeks goal is to do the comparison or atleast start it.

### Week 9:(11/03/19)-(15/03/19)
- Since Trinity doesnt want to play ball I'll try getting diffhash working in boqueron.
- Compiling R is a pain.
- OK Trinity worked, dont ask me why cause I dont know why nor how but it works.
- Next week to complete the protocol.

### Week 8:(04/03/19)-(08/03/19)
- Moving some data to boqueron to run escambron protocol to get data to compare to the output of diffhash.
- Starting escambron protocol and the working pipeline is a bit broken.
- Oh Trinity my old friend is causing problems.

### Week 7:(25/02/19)-(01/03/19)
- Too busy studying for statistics and doing the statistics proyect.

### Week 6:(18/02/19)-(22/02/19)
- Finished the patchwork run on the non-trivial data.
- Wrapped the code to run in sequence.
- Initial results show a size reduction of an order of magnitud when switching between the any filter and the all filter.
- Next goal clean up the code formalize a benchmark and parralelize.

### Week 5:(11/02/19)-(15/02/19)
- Started to rewrite diffhash to utilize a dataframe because its apparently usefull.
- I'm starting to believe the meme posted on the lab door about code working when the proffesor is in proximity of the terminal. I copied the same block of text from stackoverflow
- Further testing will be pushed to next week. Stuff happened.

### Week 4:(04/02/19)-(08/02/19)
- I merged showhash and diffhash since they are meant to run concurrently. This reduces the sample run time significantly since the biosequences package is only loaded once.
- Next weeks goal is to add filter-reads to the execution line and run with our non trivial test data at the machine in the lab

### Week 3:(25/01/19)-(01/02/19)
- I'm continuing reading up on julia and testing it out. IMO julia is still a bit undercooked but it still seems fun.
- I've set up a development branch for the code to push independant of the original origin branch.
- The code runs to comletion independant of one another.

### Week 2:(21/01/19)-(25/01/19)
- I'm no longer a total stranger to julia and the project isn't too complexicated. Goals for next week is to make sure the code runs to completion and then generalize and paralelize the code.

### Week 1:(14/01/19)-(18/01/19)
- I'll be working of diffhash https://github.com/humberto-ortiz/diffhash seems to be a very interesting peice of code. According to the proffesor the main its interesting is that its written in julia and, according to Humberto, since julia 1.0 came out not long ago this is the perfect chance to try it out.

## Spring 2017

### Week 11:(07/04/17)-(14/04/17)
- Progress is still minimal..
- Decided to pick up an old personal project in the mean time. Its nature might very well help me understand what I need to do.

### Week 12?:(12-06-17)-(16-06-16)
- World is back to normal.
- Started technical report and cleaning up work.
- uploaded everything to github and updated previous link.(https://github.com/Angelsan720/RandomThings/tree/master/research%20winter%202016%20-%20summer%202017)
- Looking into future work to keep myself busy

### Week 11:(31/03/17)-(07/04/17)
- Tried to add the tweak for the script (ran into a near exponential growth problem).
- Talked to kevin about how he was to use the script.
- Usage of the script "$ python sourmash-compare-v1.2.py file_A file_B" and outputs a file named "file_A-in-file_B.txt".
- Still in my existencial crisis though I still will try and modify the original code.

### Week 10:(24/03/17)-(31/03/17)
- Went to see the power rangers movie wasnt a complete dissapointment to my childhood.
- Since rewriting the code for sourmash wouldve been rather imposible for my level of skill decided to do something more crude.
- Finished a working version of the comparing script https://github.com/Angelsan720/RandomThings/blob/master/research%20winter%202016%20-%20summer%202017/sourmash-compare-v1.2.py
- Planning on adding some more funtionality but for now this will do.
- Reached an existential crisis and dont know what to do.
- For now staying at home while the angry mobs manifest themselves.

### Week 9:(17/03/17)-(24/03/17)
- Trying alternative by brute force comparing every sequence in both organisms using sourmash.
- If it compares in less than two days Ill call it a success.
- Fun note university is going on strike soon. Heres hoping they dont burn the buildings to the ground. 

### Week 8:(10/03/17)-(17/03/17)
- Work put on backburner for Assignmet on other classes. Programing hardware is fun..... said no one.
- Also laptop charger magicaly stayed at home.

### Week 7:(03/03/17)-(10/03/17)
- New problem have to modify sourmash to return the name of the sequence that has a correspondence greater than 99.5%.
- New problem sourmash is actually a python wrapper for C.
- I am terrified.

### Week 6:(24/02/17)-(03/03/17)
- Comparison worked. Found sequences that were 99.9% similar on both files. Problem I dont know which sequences those are.

### Week 5:(17/02/17)-(24/02/17)
- Huzaaaa trinity didnt explode
- Have two ~150MB files with data. Still assuming this is the data I want.
- Tweeking comparing script to work with the data.

### Week 4:(10/02/17)-(17/02/17)
- Trinity is finally behaving.
- Setting up scripts for final run with some tools to check the actual run time and the total cpu time.
- Queued trinity to run over the weekend

### Week 3:(03/02/17)-(10/02/17)
- Requested a java update on loretta since trinity demanded it.
- A bit more tweaking needed for the commands to run correctly.

### Week 2:(27/01/17)-(03/02/17)
- Managed to actually compare things, The samples say nemastotella is +90% the same as pepino
- Tried to run Trinity on a bulkier machine..... if gave ultra cryptic error codes

### Week 1:(23/01/17)-(27/01/17)
- Read up on sourmash
- Needed to figure out how to compute a so called 'sig' file

## Fall 2016
### Week 16:(25/11/16)-(02/12/16)
- Read a bit on Sourmash for the comparisons
- Reaserch put on hold for finals
### Week 16:(18/11/16)-(25/11/16)
- Trinity thoroughly chewd up both creatures and returned two beautiful fasta files
### Week 16:(11/11/16)-(18/11/16)
- Spoke to a lab member and we talked about doing a sample run for the sake of continuing forward until we got a better machine
- Feed Trinity a sample of both Nemastotela and Pepino

### Week 16:(11/11/16)-(18/11/16)
- Appartently we need a bigger boat I mean computer
- Spent a few days thinking of workarounds

### Week 15:(04/11/16)-(11/11/16)
- Trinity spat out Pepino due to lack of memory
- Asked Humberto if there was a bigger machine available

### Week 14:(28/11/16)-(04/11/16)
- Trinity failed due to lack of memory
- Pepino finished normalizing
- Feed pepino to Trinity

### Week 13:(24/10/16)-(28/10/16)
- Compiled trinity from source.
- Feed Nemastotella to the new trinity.
- Feed Pepino to the normalizer.
- Prays it works

### Week 12:(24/10/16)-(28/10/16)
- Continued to have problems with the script
- Managed to get the script working.
- Normalized Nemastotella dataset.
- Tried to run Trinity on Nemastotella unsuccesfully.
- Ran the cucumber through normalization

### Week 11:(17/10/16)-(21/10/16)
- Spoke with proffesor about the error.
- Fix the problem and began running the trimmer.
- Began the normalizationn step.


### Week 10:(10/10/16)-(14/10/16)
- Commenced the pipeline on boqueron.
- Re ran trimming unsuccesfully.
- Spent the rest of the week troubleshooting.

### Week 9:(03/10/16)-(07/10/16)

- Left digital normalization to run through the weekend.
- Find out that the reason why trinity is failing is because some of the data is corrupt.
- Theorize that simply loading the data into memory , sorting it and doing a binary search through it will be quick enough.
- Move from Hulk to a machine the university has for high performance computing called boqueron.
- Redownload the data at boqueron



### Week 8:(26/09/16)-(30/09/16)
- Feeling better attempted to run trinity multiple times, all failures.
- Put the trinity run on the backburner started to think of solutions for the second part.
- Friday had a major epiphany, stp thinking of these things as the representations of sequences and look at them for what they are sequences of length n made of a random assortment of four letters. (I know that theres some cases where the explisit similarity is false but the sequences are the same but thats a job another day and it can be added to the search parameters.)

### Week 7:(16/09/16)-(23/09/16)
- Monday was great. Went to the dentist and he riped out my left wisdom teeth.
- Spent the next two days in pain. 
- Friday I fought with Trinity once more.
- Quote for the week "It hurts to laugh"

### Week 6:(12/09/16)-(16/09/16)
- Had most of the data cut up.
- Made a digital normalization script to work on the data.
- Ran in thinking it would finish up promplty, it didnt.
- Left the script working on all the data.
- This update was made sept 20

### Week 5:(05/09/16)-(09/09/16)
- Finished the trimmomatic script, left it to run.
- Found out some data didnt download correctly.
- Hulk crashed something about the home directory being filled with sequences.
- Re-download data and re ran trimmomatic on some files that required more cutting.
- Hulk crashed atleast once more, maybe two times.
- Gave up on progress till Hulk felt helpful.
- This update was made sept 20

### Week 4:(29/08/16)-(02/09/16)

- Successfully ran the example given by -http://khmer.readthedocs.io/en/v2.0/user/examples.html-. Khmertools work at the very least.
- Read up on the FASTA and FASTQ formats. Khmer tools can read both. Khmer tools gives problems with large read samples. Best used for small Illumina output.
- Unsuccessfully tried to generate a script to log the start and end date of mutuals run time. More focus needed.

### Week 3:(22/08/16)-(26/08/16)

- Informed that I needed to now generate a De Bruijin graph from a given rna sequence.
- Research partner informs me that I need to make a weekly report on what I've done every week.
- Get told that Velvet/Oasis generates a De Bruijin graph from a sequence.
- Speak to professor to clear confusion.
- Confusion cleared, were gonna use Khmer tools -http://khmer.readthedocs.io/en/v2.0/- and posibly trinity -https://github.com/trinityrnaseq/trinityrnaseq/wiki- to generate the graph.
- Created a place holder weekly report to post to be replaced later (if you see this it means I've replaced it).
- Install Khmer tools on Hulk the lab server Ive been granted access to.
- Next week read up khmer tools and trinity in detail. 

### Week 2:(15/08/16)-(19/08/16)

- Read up on bioinformatics algorithms.
- Read the sample code the professor sent me.
- Start reading up on multithreaded in C++.
- Start reading on how to extend C++ code to python.

### Week 1:(8/08/16)-(12/08/16)

- Learn what thing I need to do.
- Start expanding vocabulary.
- Learn what on earth is a k-hmer.
