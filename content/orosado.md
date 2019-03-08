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

**<h3>WEEK 6: Feb18 - Feb22</h3>**

    This is my first week back at the lab, so I read up on sequence assembly and related subjects to refresh my memory.

    No paper assigned yet ;
    
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
