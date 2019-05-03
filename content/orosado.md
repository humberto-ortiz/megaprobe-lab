Title: Omar Rosado Ramírez
Date: 2019-03-01
Modified: 2019-03-01
Slug: orosado
Category: People
Tags: python, python3, kevlar, kmers, mapping-free, de-novo, variants, framework

# Omar Rosado Ramírez

## Bio:
    Full-time problem solver and computer science student.

## Contact info:
- e-mail: <omar.rosado1@upr.edu>
 - Github: <https://github.com/afrotonder>

# Research Goals

Learn some more python and submit at least 3 pull requests to the Kevlar project by the end of the semester.
  
# Weekly UPDATES

**<h3> WEEK 16: Abr29 - May3</h3>**

This week i tested kevlar on two of my machines. Although i got the project running on my low powered Asus,
my Macbook is having problems running the kevlar snakemake workflow.

The command shown in the README that installs all of kevlars dependencies fails when run on 
macOS due to snakemake. Installing snakemake with pip and pip3 on macOS fail for some odd reason.

After fiddling with the different python versions in the virtual environment and going through some errors, 
i have concluded that kevlar will need some tuning for macOS. 

Found some similar issues/solutions [here](https://github.com/googleapis/google-cloud-python/issues/3884), 
[here](https://github.com/Thriftpy/thriftpy2/commit/fd274b90775f777c96e013837117b0fbd448799e), and
[here](https://github.com/scikit-learn-contrib/py-earth/issues/191).

The users claim the problem is related to the cython package. A possible fix might be to delete all python instances
and only install python3.6, which i havent done.


**<h3> WEEK 15: Abr22 - Abr26</h3>**

Have been tweaking the README here and there. Fixed a few typos and added information that appears in certain
parts of the official [kevlar documentation](https://kevlar.readthedocs.io).

Since READMES should be precise, complete and not full of information that can misguide novice developers, 
I created a separate markdown file for some [frequently asked questions](https://github.com/afrotonder/kevlar/kevlar-faq.md) 
and another one which is an [offline version of the online documentation](https://github.com/afrotonder/kevlar/kevlar-cli-doc.md).


Since I'm basicaly done organizing kevlars documentation and am only adding miscellaneous data,
I moved to testing the app to add the missing examples from the manpage. 

Running the Kevlar snakemake is the  simplest way to run kevlar. 

I just deleted a directory called kevlar/kevlar/workflows/mark-I/Mask which contains the reference genome file used by kevlar (mask file).
At the beginning, this directory wasnt available. I thought that deleting it and re-running make would create the folder again, 
but that didnt happen. I created it by hand again and kevlar worked.

TODO: Must find out how the Mask directory gets there and add it to the README.

Ive been running kevlar from my personal laptop which is an old Asus with an i3 processor, 4GB RAM and an SSD. This should be enough for the
Snakemake workflow, since the processing the example data downloaded in the README should be able to run on a laptop in less than 5 minutes 
while consuming less than 200 Mb of RAM, as the [official docs say](https://kevlar.readthedocs.io/en/latest/quick-start.html), but it isnt.

Although it runs without making my computer fan cry, it doesnt take 5 minutes. It stalled after approximately
15 minutes running on my laptop and eventually froze the terminal. I use VSCode's integrated terminal(which is just running bash)
to work so i never have to leave the workspace. This shouldnt be a problem. 

TODO: Test the kevlar Snakemake workflow from my other two machines: one with an i5 processor, 8GB RAM and an SSD, and another one
with an i7 processor, 8GB RAM and 🤮 an HDD. Will post the outcome. 



**<h3> WEEK 14: Abr15 - Abr19</h3>**

This week i focused on finishing the README and specifically running the kevlar Snakemake Workflow Mark I. 

The kevlar snakemake workflow is the best and most productive way to use kevlar.
This workflow runs the given genomic sequence through the whole kevlar project, running
all commands listed in the kevlar-cli documentation .

*Added the snakemake package to the command that installs all kevlar dependencies.

Tested installing snakemake with pip and pip3. If you use pip, you will encounter the sad message below:

    DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7.
    Collecting snakemake
    Downloading https://files.pythonhosted.org/packages/e5/1a/0bede0c39c5a68ffa19c17c25e97cda08c7ffeef829477911309b6023c2d/snakemake-5.4.5.tar.gz (173kB)
    100% |████████████████████████████████| 174kB 1.5MB/s 
    Complete output from command python setup.py egg_info:
    At least Python 3.5 is required.

So to install snakemake you need to use pip3. Be encouraged to use python3 by default from now on so
your projects dont break all of the sudden next year. XP

UPDATE: Finished the new kevlar README. With this file, any new user should be able to install and 
user kevlar without having to move arround much.

Check out kevlars new [README](https://github.com/afrotonder/kevlar/blob/master/README.md)


**<h3> WEEK 13: Abr8 - Abr12</h3>**

This week i finished the manpage for the project. Some commands arrent specified in the 
official documentation so you'll see some commands followed solely by ?? .

Also, most commands dont have examples included. During my stay at the lab I will try to 
add as many as I can understand. If you clone the project, you can tweak it yourself
and add examples if you want to contribute. Remember that READMES, documentation, & HowTo's arrent a developers 
favorite passtimes. We mostly develop, make code work, make code better and then ugh need to document.
Contributing even as little as correcting grammar can take a load off of a developer or dev teams back.

UPDATE: The new README is almost done. Hopefully my work is clear and removes all questions
        from the road of a user. 

UPDATE: I had some troubles running the kevlar Snakemake workflow on my regular laptop(old boi) 
        so I have to test it on my mac.

[Pull here](https://github.com/afrotonder/kevlar) to get kevlar with a complete man page and a new README.


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

UPDATE: Started adding command details in manpage. It'll be a long man page, but will
        include everything a user would need to work with kevlar ;

UPDATE: Manpage almost done. A few commands and details missing before its complete ;

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