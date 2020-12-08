# Python Final Project/ Quiz Game
Jose Amaya  <br />
Course: CIS-153-O1A <br />
Revision 1 <br />
Date: 12/08/2020

## What is the idea?
The idea is to run a python quiz program using random math with random numbers and general questions which will be scored and graded according to NECC standards.
The goal is to use mutiple functions/modules (but not limited to) random, math and beautiful soup as well as libraries and tuples.

## How does it work?
1. The program will start presenting a menu with options of the type of questions to answer.
      * Mutiple math problem with random numbers
      * General trivia questions
2.  Based on the right or wrong answer, a shuffle of words from two differnt tuples will generate.
      * For the right answer, tuple1 wiil randomly print out "Great!", "Awesome!", etc. as an exmaple.
      * For the wrong answer, tuple2 will randomly print out "Sorry!", "Nope!", etc. as an example.
3. Based on the total correct answer, the average will be calculated to print out the percentage and the grade for the quiz.
4. Using beautifulsoup and a customized .html file, the program will parse through the urlf to printout specific line(s) as a closing statement at the end of the quiz.
