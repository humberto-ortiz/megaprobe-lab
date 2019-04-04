Title: Omar Rosado Ramírez
Date: 2019-03-01
Modified: 2019-03-01
Slug: orosado
Category: People
Tags: python, python3, kevlar, kmers, mapping-free, de-novo, variants, framework

# Omar Rosado Ramírez

## Bio:
    Full-time problem solver and computer sience student.

## Contact info:
- e-mail: <omar.rosado1@upr.edu>
 - Github: <https://github.com/afrotonder>

# Research Goals

Learn some more python and submit at least 3 pull requests to the Kevlar project by the end of the semester.
  
# Weekly UPDATES

**<h3> WEEK 12: Abr1 - Abr5</h3>**

Got the manpage for kevlar setup. Once the development environment has been setup, 
the manpage can be insalled via the Makefile. By running make manpage you will now
get full details on the kevlar software. 

To activate the manpage, run:
    
    $ sudo make manpage

Now you should be able to run the following command and get the manpage for kevlar:

    $ man kevlar

Once im done with the new readme, I will submit my first pull request to the official
kevlar branch. 

To view these changes to kevlar, pull <a href='https://github.com/afrotonder/kevlar'>my branch </a> and enjoy.

**<h3> WEEK 11: Mar18 - Mar29</h3>**

While building the new README i realized how little i and most(i assume) developers
don't leave their editor or preffer to stay in it as much as possible. Considering that i
decided to hack up a UNIX man page for kevlar. When you type kevlar in your terminal 
you get the commands and usage synopsys, but not much to start using it without having
to go to the documentation, then the readme, then the documentation again. 

Started working on the manpage. Read up a bit on <a href='https://www.cyberciti.biz/faq/linux-unix-creating-a-manpage/'>
                                            how to create a UNIX manpage</a> 
and created a dummy to test it out.


**<h3> WEEK 10: Mar18 - Mar22</h3>**

Had very little time to work on the investigation this week. 
Had a two tests and two quizes, am still alive though. 


**<h3> WEEK 9: Mar11 - Mar15</h3>**

This week i focused on making my presentation and setting up everything i feel
the new readme should have.


**<h3> WEEK 8: Mar4 - Mar8</h3>**

This week I focused on reading the paper in depth and fixing some dependency issues.

After installing the package python-tk which has the module tkinter, the first error
disappeared and all tests pass. Kevlar is now up and running in my dev environment.

The second error is a warning stating that theres a deprecated module
being used to read a value. Will try to solve and report my results.

The README for the project is meh so I'm planning on giving it a tune-up and making it
readable for the common Joe. 

To see Kevlar in action I downloaded 3 simulated genome files that will 
represent the _proband_ of the project(child who's genome is subject of study and 
the experimental group of the project) and the child's parents(mother and father, both control group). This will be tested as soon as the actuall
tests pass.


**What does it mean to map reads from an individual to a reference genome?**

Kevlar doesn't rely on mapping reads to a reference genome. What this means is
that the action of comparing each read to a fully known reference genome to corroborate
it's integrity is not needed. 

WEEK 8 NOTES: https://github.com/afrotonder/biology_stuff/blob/master/kevlar/ORR8150_Report-Week8.md

    
**<h3>WEEK 7: Feb25 - Mar1</h3>**

Paper chosen: 'Kevlar: a mapping-free framework for accurate discovery of de novo variants' by Daniel S Standage, C Titus Brown, Fereydoun Hormozdiari ;

Began reading the paper and taking notes ;

Created virtual environment to begin running kevlar in my computer ;

Installed all of kevlar's dependencies so i can run and hopefully contribute to the program ;

Created a directory at https://github.com/afrotonder/biology_stuff/kevlar where i'll be submiting my weekly notes aside from the weekly report.

After installing all dependencies, a way to test Kevlar is provided and available by installing the extra
python package _pytest_. Running these tests produced a couple of errors indicating more dependencies are missing.
**produced error 1:**  
    E   ModuleNotFoundError: No module named 'tkinter' ;
**produced error 2:** 

/usr/local/lib/python3.6/dist-packages/kevlar/tests/test_dist.py:120: FutureWarning: read_table is deprecated, use read_csv instead.
data = pandas.read_table(distfile.name, sep='\t')

WEEK 7 NOTES: https://github.com/afrotonder/biology_stuff/blob/master/kevlar/ORR8150_Report-Week7.md 


**<h3>WEEK 6: Feb18 - Feb22</h3>**

This is my first week back at the lab, so I read up on sequence assembly and related subjects to refresh my memory.

No paper assigned yet ;