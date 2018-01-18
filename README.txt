REQUIREMENTS:
1) Python version 3.6.1 (in Pycharm)
2) Install the libraries as mentioned under TASK 1 and TASK 2 in Pycharm

How To Setup:

Use any IDE, example: Pycharm.

1) Download Pycharm.
2) Go to File -> Settings -> Project -> Project Interpreter
3) Click on the "+" sign on the rightmost side, "+" sign is in light green colour,
   to install the required libraries as mentioned, if not already installed.
4) Copy the program to Pycharm and run.

OR

If using the terminal:

1) Go to the folder where the source code with the py extension exists.
2) Type python <filename>.py
      Eg: python Source_code_for_task_1.py
          python Source_code_for_task_2.py

NOTE: If using Terminal, python environment must be setup for the terminal commands to work. 

Task 1:

Libraries used:
1) import requests 
2) import time     
3) from collections import deque 
4) from bs4 import BeautifulSoup

Maximum depth reached : Depth 2. (Crawler stops crawling at depth 2 as it finds 1000 unique urls and saves these urls in the next depth, i.e., in depth 3)

Execution Time:

1) If politeness policy not followed, outputs in 15-30 seconds.
2) If politeness policy followed, time required to output is around 1 hour.

Task 2:

Libraries used:

1) import requests
2) import time
3) from collections import deque
4) from bs4 import BeautifulSoup
5) import nltk
6) import re

Maximum depth reached : Depth 6. (Crawler stops as it does not find any url to crawl)

NOTE: On line number 43, replace the keyword with whatever keyword you want to check.
      On line number 29, replace the word <rain> with the keyword you want to check in the regular expression

Execution Time:

1) If politeness policy not followed, outputs in around 1 minute.
2) If politeness policy followed, time required to output is around 1 hour.

REFERENCES USED FOR SOLVING THIS ASSIGNMENT:

1]YOUTUBE TUTORIAL LINKS REFERRED FOR UNDERSTANDING OF THE CONCEPT:

a) https://www.youtube.com/watch?v=jCBbxL4BGfU&list=PL6gx4Cwl9DGA8Vys-f48mAH9OKSUyav0q&t=142
b) https://www.youtube.com/watch?v=pLHejmLB16o

2]STACK-OVERFLOW AND TUTORIALSPOINT REFERRED FOR PYTHON PROGRAMMING SYNTAXES AND ALSO FOR UNDERSTANDING FEW CONCEPTS, like application of breadth-first-search
  a) https://www.tutorialspoint.com/python/string_find.htm
  and many such more links....












